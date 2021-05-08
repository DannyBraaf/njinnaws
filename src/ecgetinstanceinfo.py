import boto3


class EcGetinstanceinfo:

    def run(self):

        ec2 = boto3.resource('ec2')
        response = ec2.describe_instances(
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
