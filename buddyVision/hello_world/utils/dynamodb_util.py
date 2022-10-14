from logging import Filter
import boto3
from datetime import date
from dateutil.relativedelta import relativedelta
from boto3.dynamodb.conditions import Key, Attr
from botocore.config import Config
from botocore.exceptions import ClientError, ConnectTimeoutError

class DynamoDBUtility():
  """
  Responsible to manage access for dynamodb.
  """

  def __init__(self, table_name: str):
    try:
      session = boto3.session.Session()
      region_name = session.region_name

      endpoint_url = f'https://dynamodb.{region_name}.amazonaws.com/'
      self._client = boto3.client(
          'dynamodb',
          endpoint_url=endpoint_url
      )

      ddb = boto3.resource(
          'dynamodb',
          endpoint_url=endpoint_url,
          config=Config(
              connect_timeout=5,
              read_timeout=15,
              retries={'max_attempts': 3}
          )
      )

      self.__table_name = table_name
      self.__table = ddb.Table(table_name)
      
      print("AAAAAAAA")

    except (ClientError, ConnectTimeoutError) as e:
      raise e

  @property
  def table(self):
    return self.__table

  @property
  def client(self):
    return self._client
  def get_record(self):
    try:
      response_sensors = self.table.scan(
        FilterExpression=Attr('device_id').eq("22")
      )
      print(f"data:{response_sensors}")
      return response_sensors
    except (ClientError, ConnectTimeoutError) as e:
      raise e
    except KeyError as exc:
      raise exc
    except Exception as e:
        raise e