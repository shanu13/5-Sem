import boto3


# aws configuration
access_id_key = "ASIA6EZT2VU6C4DA2UVN"
secret_access_key = "SSG3gSBYtX3Yqgr2jlEe6irZTEQDMoV9n7cfRgvC"
session_token_key = "FwoGZXIvYXdzELb//////////wEaDPDtXz4RLn6Uv3tMWyLMAcyM6+M3JG8xOoIj327nNxJaziP4VQ7MLltJCHLI6/RHT9iQbW+KFxwRH5AXxfsA/jwXAFlCXJoJc8ifz34L3Cy72YwC5SnmElEM+H2EjigTNWjjUprIWBf7Ay/I7S8hu27F2yqq8RXeSoNrEtdJCEIOMSbCQEGyZgW9498N3x4lOQyPKxFjzAh6fmOk11L39pOZRJZjPfpXzgh4NALFg/k2Ol+4tSWJjfqgWzwCdLHBis02EDy3guwWWfyS0FObnLbPYXKbYYyBeKc5liiB5aqKBjItbH6T0zzTq1/2Ll4MWNqZx3VQV+2J4UJKPBd9ZWinbMVlUjhcCoDtWxqYwCgx"
rdsClient = boto3.client(
    "rds",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="mydb",
    DBInstanceIdentifier="mydb",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="root",
    MasterUserPassword="agrawal123",
    PubliclyAccessible=True,
)


import time

while True:
    response = rdsClient.describe_db_instances(
        DBInstanceIdentifier="shantanu",
        MaxRecords=20,
    )

    status = response["DBInstances"][0]["DBInstanceStatus"]

    if status == "available" or status == "AVAILABLE":
        break
    else:
        time.sleep(10)


print(response["DBInstances"][0]["Endpoint"]["Address"])
