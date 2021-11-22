import boto3

try:
    client = boto3.client("elasticbeanstalk")
    response = client.create_application(
        ApplicationName="Web-App-trial",
    )

    client.create_application_version(
        ApplicationName="Web-App-trial",
        VersionLabel="v1",
        SourceBundle={
            "S3Bucket": "cloud1901182",
            "S3Key": "Jwt-Auth-main.zip",
        },
    )

    client.create_environment(
        ApplicationName="Web-App-trial",
        EnvironmentName="Web-App-env-trial",
        Tier={
            "Name": "WebServer",
            "Type": "Standard",
        },
        SolutionStackName="64bit Amazon Linux 2 v5.4.5 running Node.js 14",
        VersionLabel="v1",
        OptionSettings=[
            {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "IamInstanceProfile",
                "Value": "aws-elasticbeanstalk-ec2-role",
            },
        ],
    )
    print(response)
except Exception as e:
    print(e)
