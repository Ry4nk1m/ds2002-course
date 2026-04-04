#!/bin/bash

# Your specific IDs from the console
AMI="ami-07ff62358b87c7116" 
SG_ID="sg-0be6679b34372f15a"
SUBNET_ID="subnet-085a38474f2e3b60c"

# Configuration
INSTANCE_TYPE="t2.nano"
INSTANCE_NAME="ds2002-qec4gc"
KEY_NAME="key-ec2"

aws ec2 run-instances \
  --image-id $AMI \
  --count 1 \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-group-ids $SG_ID \
  --subnet-id $SUBNET_ID \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]"
