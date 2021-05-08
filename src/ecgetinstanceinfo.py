import boto3


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
            DryRun=True | False,
            MaxResults=123,
            NextToken='string'
        )

        return response
