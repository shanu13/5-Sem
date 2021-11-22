import boto3

version_label = '1.0.0'
application_name = 'jwt-auth'
environment_name = 'jwt-auth-env'


def createNewVersion() -> bool:
    try:
        client = boto3.client('elasticbeanstalk')
    except:
        print('Failed to create Elastic Beanstalk client')
        return False

    try:
        response = client.create_application(
               ApplicationName=application_name 
            )
        
        response = client.create_application_version(
            ApplicationName=application_name,
            VersionLabel=version_label,
            Description='Shantanu Agrawal Jwt-auth',
            SourceBundle={
                'S3Bucket': 'cloud1901182',
                'S3Key': 'Jwt-Auth-main.zip'
            },
            AutoCreateApplication=True,
            Process=True
        )
        print(f'Application: {application_name} Created')
    except Exception as e:
        print(f'Error has occured while creating a version for the application: {e}: ')
        return False

    return True


def createEnvironment() -> bool:
    try:
        client = boto3.client('elasticbeanstalk')
    except:
        print('Failed to create Elastic Beanstalk client')
        return False

    try:
        response = client.create_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            Description='Simple 1.0.0 Auth',
            CNAMEPrefix='shantanu',
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
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'InstanceType',
                    'Value': 't2.micro',

                },
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'EC2KeyName',
                    'Value': 'cs351-2021',

                },
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'ImageId',
                    'Value': 'ami-0c2b8ca1dad447f8a',

                },
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'SecurityGroups',
                    'Value': "launch-wizard-1",
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'BreachDuration',
                    'Value': '1',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'Statistic',
                    'Value': 'Average',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'Unit',
                    'Value': 'Percent',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'EvaluationPeriods',
                    'Value': '1',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'Period',
                    'Value': '1',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'UpperThreshold',
                    'Value': '70',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'UpperBreachScaleIncrement',
                    'Value': '1',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'MeasureName',
                    'Value': 'CPUUtilization',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'LowerThreshold',
                    'Value': '30',
                },
                {
                    'Namespace': 'aws:autoscaling:trigger',
                    'OptionName': 'LowerBreachScaleIncrement',
                    'Value': '-1',
                },
                {
                    'Namespace': 'aws:autoscaling:asg',
                    'OptionName': 'Availability Zones',
                    'Value': 'Any 2',
                },
                {
                    'Namespace': 'aws:autoscaling:asg',
                    'OptionName': 'MaxSize',
                    'Value': '3',
                },
                {
                    'Namespace': 'aws:autoscaling:asg',
                    'OptionName': 'MinSize',
                    'Value': '1',
                },
            ],
        )
        print('Environment created for the web application')
    except Exception as e:
        print(f'Error occured while creating the environment for web application: {e}')
        return False

    return True


def start():
    created = createNewVersion()
    if created:
        env = createEnvironment()


if __name__ == '__main__':
    start()
