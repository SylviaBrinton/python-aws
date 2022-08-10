#Python Program for creating a connection
import boto3

ec2 = boto3.client('ec2',
				'us-east-1',
				aws_access_key_id='AKIAV2P2BS5DHCMQNNB7',
				aws_secret_access_key='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')

#This function will describe all the instances
#with their current state
response = ec2.describe_instances()
print(response)
