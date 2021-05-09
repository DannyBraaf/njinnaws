import boto3


class Execute:

  def run(self):
      print("Searching for instances in region: "+self.region+" in the state: "+ self.instancestate)
      ec2 = boto3.resource('ec2', region_name=self.region)
      dict1 = []
      instances = ec2.instances.filter(
          Filters=[{'Name': 'instance-state-name', 'Values': [self.instancestate]}])

      for instance in instances:
          print(self.region, instance.id, instance.instance_type, instance.vpc.id, instance.subnet.id,
                instance.state['Name'], instance.public_ip_address, instance.private_ip_address, instance.architecture, instance.launch_time)
          dict2 = [instance.id, self.region, instance.instance_type, instance.vpc.id, instance.subnet.id, instance.state['Name'], instance.public_ip_address, instance.private_ip_address, instance.architecture, instance.launch_time]
          # print(dict1)
          dict1.append(dict2)
       
      if not dict1:
            print("No instances found in region: "+self.region+" in the state: "+ self.instancestate)
      return dict1