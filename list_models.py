import os
import pprint
from dotenv import load_dotenv
import boto3


#Load environment variables from the .env file
load_dotenv()

#Assign environment variables to Python variables
region = os.getenv('region')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_session_token = os.getenv('aws_session_token')

# Initialize the boto3 client using the variables
bedrock_boto3 = boto3.client(
    'bedrock',
    region_name=region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# List all models
def list_models():
    models =[models['modelId'] for models in bedrock_boto3.list_foundation_models()['modelSummaries']]
    pprint.pprint(models)
    
list_models()




