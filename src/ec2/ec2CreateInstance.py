import boto3
class Ec2CreateInstance:
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
ImageId=self.imageId,
    MaxCount=self.MaxCount,
    MinCount=self.MinCount,
    DryRun=self.dryrunEnabled,
    KeyName=self.KeyName,
    SecurityGroupIds=[
        self.secGroup
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
    CreditSpecification={
        'CpuCredits': 'CpuCredits'
    },
    EbsOptimized=self.EbsOptimizedenabled,
    # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationSpecification.html
    # Open = Adds Instance to any existing Reserved Capacity that is available
    # None = Runs as On-Demand instance (First Come First Served)
    CapacityReservationSpecification={
        'CapacityReservationPreference': self.CapacityReservationPreference
    },
    UserData="""self.userData""",
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

time.sleep(20)

#while instances[0].public_ip_address = '':
#       print(instances[0].public_ip_address) 
#       time.sleep(10)
#       instances[0].update()sdfsdfdf

instances[0].reload()
PublicIpAddress = instances[0].public_ip_address
privateIpAddress = instances[0].private_ip_address
#while PublicIpAddress != 'none':
#    instances[0].reload()
#    time.sleep(10)
#    print(PublicIpAddress)
#    PublicIpAddress = instances[0].public_ip_address
    



result = {'instanceid':instanceid, 'PublicIpAddress':PublicIpAddress, 'privateIpAddress':privateIpAddress}
print(PublicIpAddress)
print(instanceid)
print(result)


