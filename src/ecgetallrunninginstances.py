import boto3
from botocore.config import Config


class Execute:

    def run(self):

        ec2 = boto3.resource('ec2')
        list1 = ""
        for instance in ec2.instances.all():
         list1 += instance.id + instance.state 

        return list1
