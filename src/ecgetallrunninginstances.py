import boto3


class Execute:
   

ec2 = boto3.resource('ec2', region_name='eu-west-1')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type, instance.vpc.id, instance.subnet.id,
          instance.state['Name'], instance.public_ip_address, instance.private_ip_address, instance.architecture, instance.launch_time)
    dict1 = {"instance_id"   : instance.id,
            "instance_type" : instance.instance_type,
            "instance_vpc_id" : instance.vpc.id,
            "instance_subnet_id" : instance.subnet.id,
            "instance_state" : instance.state['Name'],
            "instance_public_ip_address" : instance.public_ip_address,
            "instance_private_ip_address" : instance.private_ip_address,
            "instance_architecture" : instance.architecture,
            "instance_launch_time" : instance.launch_time}
    #print(dict1)
    
    return dict1
    
