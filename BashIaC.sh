//Aqui por el tiempo no alcance a implementar los output de cada script para que se envien como paramatro a cada script

aws cloudformation create-stack --stack-name vpc --template-body file://VPCySubNet.yml --parameters NombreVPC=Ejemplo
aws cloudformation create-stack --stack-name bd --template-body file://RDSMySql.yml --parameters Owner=Eliel,VPC=Ejemplo,PrivateSubnet1=NombreSubnet,PrivateSubnet2=NombreSubnet
aws cloudformation create-stack --stack-name ec2 --template-body file://Ec2.yml --parameters KeyName=Llave, InstanceType=t3.nano, SSHLocation=0.0.0.0/0