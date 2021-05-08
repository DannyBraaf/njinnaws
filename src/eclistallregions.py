import boto3
from botocore.config import Config

class Execute:

    def run(self):
        

        ec2 = boto3.resource('ec2',region_name=self.region)
        
      # List all regions
        client = boto3.client('ec2')
        regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        
        return regions