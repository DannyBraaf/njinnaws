import boto3


class Execute:

    def run(self):

        client = boto3.client('ec2', region_name=self.region)
        Myec2 = client.describe_instances(
            InstanceIds=[
                self.Instanceids
            ],
            DryRun=self.dryrunEnabled
        )

        return Myec2
