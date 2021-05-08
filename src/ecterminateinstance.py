import boto3
from botocore.config import Config


class EcTerminateInstance:

    def run(self):
        my_config = Config(
            region_name=self.region,
            signature_version='v4',
            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )

        ec2 = boto3.resource('ec2')
        list1 = [self.Instanceids]
        ec2.instances.filter(InstanceIds=list1).terminate()

        return list1
