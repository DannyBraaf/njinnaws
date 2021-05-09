import boto3
from botocore.config import Config


class Execute:

    def run(self):

         ec2 = boto3.resource('ec2')
         for instance in ec2.instances.all():
         print (instance.id , instance.state)
    
    
        return ec2.instances.all()
