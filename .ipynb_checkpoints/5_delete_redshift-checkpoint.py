# Load python libraries 
import boto3
import time
import pandas as pd
import os

# Load configuration file
from configparser import ConfigParser
config = ConfigParser()
config.read_file(open('dwh.cfg'))

# Load variables from configuration file
KEY=config.get('AWS','key')
SECRET= config.get('AWS','secret')
DB_HOST = config.get("CLUSTER","HOST")
DB_ROLE_NAME = config.get("CLUSTER", "DB_ROLE_NAME")

# Need AWS Key and Secret for IAM to do this with programmatic access

# Create Redshift client
from boto3 import client
redshift = client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET)

# Create IAM Client
from boto3 import client

iam = client('iam',aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     region_name='us-west-2'
                  )

# Delete Redshift resources
try:
    redshift.delete_cluster( ClusterIdentifier=DB_HOST,  SkipFinalClusterSnapshot=True)
except Exception as e:
    print(e)
    
# Remove roles and policies
iam.detach_role_policy(RoleName=DB_ROLE_NAME, PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
iam.delete_role(RoleName=DB_ROLE_NAME)


