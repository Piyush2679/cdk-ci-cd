from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2
)

class MyVpcCdkStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "MyVpc",
                           max_azs=2,  # Number of availability zones
                           cidr="10.0.0.0/16",
                           subnet_configuration=[
                               ec2.SubnetConfiguration(
                                   name="PublicSubnet",
                                   subnet_type=ec2.SubnetType.PUBLIC,
                                   cidr_mask=24
                               ),
                               ec2.SubnetConfiguration(
                                   name="PrivateSubnet",
                                   subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                                   cidr_mask=24
                               )
                           ]
                           )
