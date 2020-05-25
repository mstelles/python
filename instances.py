#!/usr/local/bin/python3
# list EC2 instances based on the "regions" file
# format:
# region:code:r53ID:city:

import boto3

file = open("regions","r")

for line in file:
  reg=line.split(":")[0]
  regname=line.split(":")[3]
  li=reg.strip()
  if not li.startswith("#"):
    client = boto3.client('ec2', region_name=reg)

    response = client.describe_instances()

    for r in response['Reservations']:
      for i in r['Instances']:
        if i :
          try:
            #print (boto3.Session().get_credentials().access_key)
            #print (boto3.Session().get_credentials().secret_key)
            print ("Region:", reg, "-", regname)
            print ("Instance ID: ", i['InstanceId'])
            print ("Public IP: ", i['PublicIpAddress'])
          except:
            print ("Ops... Some problem while processing", reg + ", " + i['InstanceId'])

file.close()
