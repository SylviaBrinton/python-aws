import boto3
 
ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
	    InstanceIds=[
        'i-057e9ad0d4b3625e3',
    ],
)