import boto3


class Execute:

    def run(self):

        client = boto3.client('elb', region_name=self.region)
        sslcert = self.SSLCertificateId
        if not sslcert:
            response = client.create_load_balancer(
                LoadBalancerName=self.name,
                Listeners=[
                    {
                        'Protocol': self.Protokol,
                        'LoadBalancerPort': self.LoadBalancerPort,
                        'InstanceProtocol': self.InstanceProtocol,
                        'InstancePort': self.InstancePort
                   
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
                Scheme=self.Scheme
            )
        else:
            response = client.create_load_balancer(
                LoadBalancerName=self.name,
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
                Scheme=self.Scheme
            )

        return response
