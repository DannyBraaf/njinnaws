import boto3


class Execute:

  def run(self):

      ec2 = boto3.resource('ec2', region_name='eu-west-1')
      dict1 = []
      instances = ec2.instances.filter(
          Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

      for instance in instances:
          print(instance.id, instance.instance_type, instance.vpc.id, instance.subnet.id,
                instance.state['Name'], instance.public_ip_address, instance.private_ip_address, instance.architecture, instance.launch_time)
          dict2 = [instance.id, instance.instance_type, instance.vpc.id, instance.subnet.id,
                instance.state['Name'], instance.public_ip_address, instance.private_ip_address, instance.architecture, instance.launch_time]
          # print(dict1)
          dict1.append(dict2)
         
      return dict1



x.update(d)