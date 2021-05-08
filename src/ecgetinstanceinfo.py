import boto3
from botocore.config import Config


class EcGetinstanceinfo:

    def run(self):

        client = boto3.client('ec2', region_name=self.region)
        list1 = [self.Instanceids]
        InstanceIds=[
                list1,
            ],
            DryRun=self.dryrunEnabled,
            MaxResults=123,
            NextToken='string')
       

        return Myec2
