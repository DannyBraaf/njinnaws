import boto3
from botocore.config import Config


class EcGetinstanceinfo:

    def run(self):

        client = boto3.client('ec2', region_name=self.region)
        Myec2 = client.describe_instances(
            InstanceIds=[
                self.Instanceids
            ],
            DryRun=self.dryrunEnabled,
            NextToken='string')
       

        return Myec2
