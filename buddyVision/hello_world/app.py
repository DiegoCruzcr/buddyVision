import json
from utils.dynamodb_util import DynamoDBUtility
import os

# import requests
class SensorsData:

    def getConnection(self):
        self.table_name = os.getenv("TABLE_NAME")
        db_client = DynamoDBUtility(self.table_name)
        return db_client

    def getSensorsDataintoDB(self):
        client = self.getConnection()
        response = client.get_record()
        return response



def lambda_handler(event, context):
  sensors_data = SensorsData()
  headers = {'Content-type': 'application/json'}
  lambda_response = {}
  if context:
    pass
  try:
    item = sensors_data.getSensorsDataintoDB()
    lambda_response = {
      'statusCode': 200,
      'body': json.dumps(item),
      'headers': headers
    }
  except Exception as e:# pylint: disable=broad-except
    raise e
  return lambda_response
