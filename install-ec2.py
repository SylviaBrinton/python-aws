#Python Program for creating a connection
import boto3

#Function for connecting to EC2
ec2 = boto3.client('ec2',
				'ap-south-1',
				aws_access_key_id='AKIAV2P2BS5DHCMQNNB7',
				aws_secret_access_key='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')

#Function for running instances
conn = ec2.run_instances(InstanceType="t2.micro",
						MaxCount=1,
						MinCount=1,
						ImageId="ami-02d55cb47e83a99a0")
print(conn)
