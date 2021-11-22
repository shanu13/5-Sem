import boto3
import time

client=boto3.client('elasticbeanstalk',region_name='us-east-1',aws_access_key_id='ASIA6EZT2VU6E6ZHXQR3',
aws_secret_access_key='GrdwVz3n97JccqKoE8q5CiFmo0WVem6nyvtavpAS',aws_session_token='FwoGZXIvYXdzEAMaDIKugPkPE4NlOPUMVyLMAe8tJwQczZ5bS6clQqco/IpVpoNvceww4lkj7n8nxR6GqYEwj5Cv7nniB4hi14w7lYU7TuGn52Cd9w6FBxWUTPB8nlevZpNg+2H53yKhT3aet0S2PHl8v52VJuHQwaUzjxUY3oWmHwQROUQF+t2B3HYW1tApZMLQnZM6wRjlRbzmkbtc833A8UHlJsBlot59+U7Eos0g4TMlvH5iHAM+dsfd1HiDuXzWsbP3HhdzWjdNMG8bL6ImQ3MpujagJvbVU+xndM4tesnR4enM4Sj/sYOKBjItggS9vWJn+UZVQKc/rdkNm5bvznwVok5eaoD5BN4IFtwbHrzg+HoARwg1Nnb5')

#client=boto3.client('cloudfront',region_name='us-east-1',aws_access_key_id='ASIAXT2EVHYJEQWGI3MZ',
#aws_secret_access_key='z2Vja9gxsSvB8hdmxYBOk8u725HZ9NzlhlQIJ1fV',aws_session_token='FwoGZXIvYXdzEAEaDO9Sttk4jdvkkJXCiCLHAR8SYzkuCDgKPwJ8pZ4ugjK/hxAlQ9hZCQ0xFUsXnfWkLPYObmiOToa4t+dKL+ie2cg3XWUs2HAQzUIXur6teWGgmgDy4ar81kxE7aB/04p+l63BUfU8V5lBM6AtEODdgooOxv77Q1anz3/S/YdT7LKwhwZ/gALjqBAAY/EggOAfUswxWEdGmcE7DwoPjhM8PKFaKLQJwdWmA6uAb/7wf+XuBV12gDUFf9hIg2Z6BRkEGslp4/5Txs/3FItMth4KYHo0vXHlVfEozPaCigYyLXGufkdrk7m7mzvYsuHMhK0AwHae4gxkPZ5CVKt07BX0DiHqiE7vsNQf4BKp0Q==')


def cloudFront_distribution():
    print('hi')
    response = client.create_distribution(
            DistributionConfig={
                'CallerReference': 'my-distribution-cdn',
                
                'DefaultRootObject': 'index.html',
                'Origins': {
                    'Quantity':1,
                    
                    'Items': [
                        {
                            'Id':'lab3dynamicwebsite',
                            'DomainName': 'lab3dynamicwebsite.s3.us-east-1.amazonaws.com',
                        
                            
                            'S3OriginConfig': {
                                'OriginAccessIdentity': ''
                            },
                           
                        
                        },
                    ]
                },
             'DefaultCacheBehavior': {
                'TargetOriginId': 'lab3dynamicwebsite',
                
               
                'ViewerProtocolPolicy': 'allow-all',
                'AllowedMethods': {
                    'Quantity': 1,
                    'Items': [
                        'GET','HEAD','POST','PUT','PATCH','OPTIONS','DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 1,
                        'Items': [
                            'GET','HEAD','POST','PUT','PATCH','OPTIONS','DELETE',
                        ]
                    }
                },
        },
        'Comment':'distribution to host portfolio',
        'Enabled':True,

    }
    )
    print(response)
    


def create_version():
    response = client.create_application_version(
        ApplicationName='my-app-1',
        AutoCreateApplication=True,
        Description='my-app-v4',
        Process=True,
        SourceBundle={
        'S3Bucket': 'cloud1901182',
        'S3Key': 'Jwt-Auth-main.zip',
        },
        VersionLabel='v1',

    )
    print(response)

def create_environment():
    
    response = client.create_environment(
        ApplicationName='my-app-1',
        CNAMEPrefix='my-app-1',
        EnvironmentName='my-env-1',
        SolutionStackName='64bit Amazon Linux 2 v5.4.5 running Node.js 14',
        VersionLabel='v1',
        OptionSettings=[
        {
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'IamInstanceProfile',
            'Value':'EMR_EC2_DefaultRole'
            
            
        },{
            'Namespace':'aws:autoscaling:launchconfiguration',
            'OptionName': 'EC2KeyName',
            'Value':'cs351-2021'
        },{
            'Namespace':'aws:autoscaling:asg',
            'OptionName':'MaxSize',
            'Value':'2'
        }
    ],
    )
    
    print(response)

if __name__ == "__main__":
    #cloudFront_distribution()
    create_version()
    time.sleep(5)
    create_environment()