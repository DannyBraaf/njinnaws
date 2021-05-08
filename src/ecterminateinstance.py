import boto3


class EcTerminateInstance:

    def run(self):

ec2 = boto3.resource('ec2')

list1 = [self.Instanceids]
ec2.instances.filter(InstanceIds = list1).terminate()


    return list1