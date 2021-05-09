import boto3
from botocore.config import Config


class Execute:

    def run(self):

        ec2 = boto3.client('ec2', region_name=self.region)
     
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': [self.instancestate]}])
    
        return instances
