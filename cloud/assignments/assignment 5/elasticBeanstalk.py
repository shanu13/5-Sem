import boto3

ebsClient = boto3.client('elasticbeanstalk')

version_label = 'version_demo'
application_name = 'MyHomePage'
environment_name = 'MyHomePageEnv'
# aws-elasticbeanstalk-ec2-role


def createNewVersion():
    try:
        ebsClient.create_application_version(
            ApplicationName=application_name,
            VersionLabel=version_label,
            Description='Auth website',
            SourceBundle={
                'S3Bucket': 'cloud1901182',
                'S3Key': 'Jwt-Auth-main.zip'
            },
            AutoCreateApplication=True,
            Process=False
        )
        print('application Created')
    except Exception as e:
        print('some error has occured: ', e)


def createEnvironment():
    try:
        ebsClient.create_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            Description='Jwt-Auth web app Nodejs environment',
            CNAMEPrefix='shantanuagrawal',
            Tier={
                'Name': 'WebServer',
                'Type': 'Standard',
            },
            VersionLabel=version_label,
            SolutionStackName='64bit Amazon Linux 2 v5.4.5 running Node.js 14',
            OptionSettings=[
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'IamInstanceProfile',
                    'Value': 'aws-elasticbeanstalk-ec2-role'
                },
            ],
        )
        print('Environment Created')
    except Exception as e:
        print('some error has occured: ', e)


def init():
    createNewVersion()
    createEnvironment()


if __name__ == '__main__':
    init()
