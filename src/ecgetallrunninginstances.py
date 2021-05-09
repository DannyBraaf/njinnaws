import boto3
from botocore.config import Config


class Execute:

    def run(self):

        ec2 = boto3.resource('ec2')
        list1 =  ec2.instances.all()

        return list1
