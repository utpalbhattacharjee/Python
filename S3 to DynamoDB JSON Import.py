import json
import boto3
s3client = boto3.client('s3')
ddbclient = boto3.resource('dynamodb')
def lambda_handler(event, context):
    bucketname = event['Records'][0]['s3']['bucket']['name']
    jsonfilename = event['Records'][0]['s3']['object']['key'].strip()
    print(bucketname)
    print(jsonfilename)
    jsonobject = s3client.get_object(Bucket=bucketname,Key=jsonfilename)
    jsonfilereader = jsonobject['Body'].read()
    jsonDict = json.loads(jsonfilereader)
    print(jsonDict)
    table = ddbclient.Table('whizlabs_company_table')
    table.put_item(Item=jsonDict)
    return {
        'statusCode': 200,
        'body': json.dumps('JSON Data Imported')
    }
