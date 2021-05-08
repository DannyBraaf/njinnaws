import boto3
from botocore.config import Config

class EcGetinstanceinfo:

    def run(self):



        my_config = Config(
            region_name=self.region,
            signature_version='v4',
            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )


        client = boto3.client('ec2')
        response = client.describe_instances(
            Filters=[
                {
                    'Name': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            InstanceIds=[
                self.Instanceids,
            ],
            DryRun=self.dryrunEnabled,
            MaxResults=123,
            NextToken='string'
        )

        return response
