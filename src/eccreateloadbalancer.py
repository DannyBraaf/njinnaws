import boto3


class Execute:

    def run(self):

        ec2 = boto3.resource('ec2', region_name=self.region)

      # List all regions
        client = boto3.client('ec2')
        response = client.create_load_balancer(
              LoadBalancerName='string',
              Listeners=[
                          {
                              'Protocol': self.Protokol,
                              'LoadBalancerPort': self.LoadBalancerPort,
                              'InstanceProtocol': self.InstanceProtocol,
                              'InstancePort': self.InstancePort,
                              'SSLCertificateId': self.SSLCertificateId
                          },
                      ],
                      AvailabilityZones=[
                          self.AvailabilityZones,
                      ],
                      Subnets=[
                          self.subnet,
                      ],
                      SecurityGroups=[
                          self.SecurityGroups,
                      ],
                      Scheme=self.Scheme)
                
               return response  
      
      
      
      
      
      
