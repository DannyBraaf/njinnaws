import boto3
from botocore.config import Config


class Execute:

    def run(self):

        ec2 = boto3.resource('ec2', region_name=self.region)

        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': [self.instancestate]}])
        for instance in instances:
            print(instance.id, instance.instance_type)

        return instances instance.instance_type
