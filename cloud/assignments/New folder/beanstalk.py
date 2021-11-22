import boto3
import time

client=boto3.client('elasticbeanstalk',region_name='us-east-1',aws_access_key_id='ASIA6EZT2VU6FEWNWH6L',
aws_secret_access_key='0mOvi6b1i634JBauPnkRvt8ZI5StDTCh0qEUnvdh',
aws_session_token='FwoGZXIvYXdzEA0aDFMvbyT+2uEkzy+SmiLMAfBMqXZgyj/VTdCjlgwkMHpGluSMDNmSKikZRB8m6ZiiRx1kODv66Er3iBh+xlj3AzxFF7Evi8iUNp03K6/P3XgiWkGLJyPoaOgHcqnN3ZMrrHOyeGHL0hRTUfoyZLMBlcfAaPtAeuyIJcum2ndydyW1XHFt8iPK2G+BHIVhP9rGQhxsNUagJLcN1qcU5OJfU/sqQfgCE+XaHlEb7K9+lzafzh0USekryWK2gHXfDXlFA0BuRrzjRicoxwKAmzdRmor5aH9mzJK0v5C8KCiv0oWKBjItWYo9AmuFyx36MoAWo3U2coTf/go1qkMBrX3bAo2GN2D2s1CuTYohs3pAheFH')

#client=boto3.client('cloudfront',region_name='us-east-1',aws_access_key_id='ASIAXT2EVHYJEQWGI3MZ',
#aws_secret_access_key='z2Vja9gxsSvB8hdmxYBOk8u725HZ9NzlhlQIJ1fV',aws_session_token='FwoGZXIvYXdzEAEaDO9Sttk4jdvkkJXCiCLHAR8SYzkuCDgKPwJ8pZ4ugjK/hxAlQ9hZCQ0xFUsXnfWkLPYObmiOToa4t+dKL+ie2cg3XWUs2HAQzUIXur6teWGgmgDy4ar81kxE7aB/04p+l63BUfU8V5lBM6AtEODdgooOxv77Q1anz3/S/YdT7LKwhwZ/gALjqBAAY/EggOAfUswxWEdGmcE7DwoPjhM8PKFaKLQJwdWmA6uAb/7wf+XuBV12gDUFf9hIg2Z6BRkEGslp4/5Txs/3FItMth4KYHo0vXHlVfEozPaCigYyLXGufkdrk7m7mzvYsuHMhK0AwHae4gxkPZ5CVKt07BX0DiHqiE7vsNQf4BKp0Q==')


def cloudFront_distribution():
   
    response = client.create_distribution(
            DistributionConfig={
                'CallerReference': 'my-distribution-cdn',
                
                'DefaultRootObject': 'index.html',
                'Origins': {
                    'Quantity':1,
                    
                    'Items': [
                        {
                            'Id':'cloud1901182',
                            'DomainName': 'cloud1901182.s3.us-east-1.amazonaws.com',
                        
                            
                            'S3OriginConfig': {
                                'OriginAccessIdentity': ''
                            },
                           
                        
                        },
                    ]
                },
             'DefaultCacheBehavior': {
                'TargetOriginId': 'cloud1901182',
                
               
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
        ApplicationName='my-app-2',
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
        ApplicationName='my-app-2',
        CNAMEPrefix='my-app-2',
        EnvironmentName='my-env-2',
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