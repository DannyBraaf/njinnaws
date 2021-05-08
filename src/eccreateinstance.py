import boto3


class EcCreateInstance:

    def run(self):

        ec2 = boto3.resource('ec2')

        # create a new EC2 instance
        instances = ec2.create_instances(
            ImageId=self.imageId,
            MaxCount=self.MaxCount,
            MinCount=self.MinCount,
            DryRun=self.dryrunEnabled,
            KeyName=self.KeyName,
            SecurityGroupIds=[

                self.SecGroup

            ],
            InstanceType=self.InstanceType,
            Placement={
                'Tenancy': 'default'
            },
            Monitoring={
                'Enabled': self.MonitoringEnabled
            },
            DisableApiTermination=False,
            InstanceInitiatedShutdownBehavior=self.InstanceShutdownbehavior,
            EbsOptimized=self.EbsOptimizedenabled,
            # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationSpecification.html
            # Open = Adds Instance to any existing Reserved Capacity that is available
            # None = Runs as On-Demand instance (First Come First Served)
            CapacityReservationSpecification={
                'CapacityReservationPreference': self.CapacityReservationPreference
            },
            UserData="""""",
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'VolumeSize': self.VolumesizeinGB,
                        'DeleteOnTermination': self.DeleteVolumeonTerminationenabled,
                        'VolumeType': 'gp2'
                    }
                }
            ]
        )

        instanceid = instances[0].instance_id
        instances[0].wait_until_running()

        instances[0].reload

        instances[0].reload()
        PublicIpAddress = instances[0].public_ip_address
        privateIpAddress = instances[0].private_ip_address     
        return {"instanceid": instanceid,"PublicIpAddress":PublicIpAddress,"privateIpAddress" : privateIpAddress}
