#!/usr/bin/env python3.7
# list EC2 instaces based on region and tag

import sys
import boto3
#from botocore.exceptions import ClientError

region = sys.argv[1]
group = sys.argv[2]
instance_tag = sys.argv[3]
f_hosts = open('/tmp/hosts','w')
f_ahosts = open('/tmp/ahosts','w')

with f_ahosts:
    f_ahosts.write(f"[{group}]\n")
ec2 = boto3.resource('ec2', region_name=region)

for instance in ec2.instances.all():
    for tag in instance.tags:
        if tag['Value'] == instance_tag:
            #print (tag['Value'])
            instanceId = instance.id
            instanceIntIP = instance.private_ip_address
            f_hosts = open('/tmp/hosts','a')
            f_ahosts = open('/tmp/ahosts','a')
            print(f"Adding instance \'{instanceId}\', to the \'{group}\' due to the {tag} tag")
            with f_hosts:
                f_hosts.write(f"{instanceIntIP}\t{instanceId}\n")
            with f_ahosts:
                f_ahosts.write(f"{instanceId}\n")
