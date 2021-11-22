import sys
import boto3
import boto3.ec2
from botocore.exceptions import ClientError
from botocore.config import Config



my_config = Config(
    region_name = 'us-east-1d',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

instance_id = sys.argv[1]

ec2 = boto3.client('ec2', config=my_config)
print("Found the region")

# Do a dryrun first to verify permissions
try:
    comp = ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
    print("Got error while dryrun")
    if 'DryRunOperation' not in str(e):
        raise
except:
    print("Got error while dryrun")

# Dry run succeeded, run start_instances without dryrun
try:
    response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
except ClientError as e:
    pritn("Found error while running")
    print(e)
except:
    print("Got error while running")
