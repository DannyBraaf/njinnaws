import boto3
from botocore.config import Config

class EcGetinstanceinfo:

    def run(self):


        client = boto3.client('ec2',region_name=self.region)
        Myec2=client.describe_instances(InstanceId=self.Instanceids)
        print(Myec2)     

        return Myec2
