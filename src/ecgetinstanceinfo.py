import boto3
from botocore.config import Config

class EcGetinstanceinfo:

    def run(self):






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
                'self.Instanceids',
            ],
            DryRun=self.dryrunEnabled,
            MaxResults=123,
            NextToken='string'
        )

        return response
