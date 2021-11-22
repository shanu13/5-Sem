import boto3

client=boto3.client('rds',region_name='us-east-1',aws_access_key_id='ASIAUV6KQ6OIUVQRQBNU',
aws_secret_access_key='Dezgjc1HBB1pPWlkyu7r6q1D6oGP/LXf2gjDbX8e',aws_session_token='FwoGZXIvYXdzEHIaDDagM/AvehuxmesVTiLLASXjy1STCfv5OsSGjUa7gXG8QLOLp3socoIeT5aNpRskz6lLr/E0lR6MXMxzdF81Z5E90oS6NyyZY9tDwx9lj1EsfK0CL5HeVfRTP4QV0D10RamtAi7A+8mgHXOw4/Y/H6UQ0K4cBclfLSSrr4gx1VlzBNe4ktsfSaqAdgd8TbtPwrwwmWCRQwRa77zqLDsvIs/MUxfs+J6+pUAZpTaKDhlCfvpxXtD93V20JGBwqlVhxEMeEcjx3yrWl8UD8xtGnBp76h0xAenXq0iuKKrgm4oGMi0rkeTCFkgOKf3bB7kWPNqsIS8+ew0oPinbndwXWt0D4yyFWOsit4UJx8U+W64=')


response = client.create_db_instance(
    DBName="my_db",
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='mymysqlinstance',
    Engine='MySQL',
    MasterUserPassword='agrawal',
    MasterUsername='root',
    VpcSecurityGroupIds=[
        'sgr-0241d9b7a7edfdbc1',
    ],
    PubliclyAccessible=True,
    AllocatedStorage=5,
)

print(response)