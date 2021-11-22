        import boto3

client = boto3.client('autoscaling')


data = '''
#!/bin/bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
wget https://cloud1901182.s3.amazonaws.com/index.html
wget https://cloud1901182.s3.amazonaws.com/script.js
wget https://cloud1901182.s3.amazonaws.com/style.css
'''


launch_config = client.create_launch_configuration(
    ImageId='ami-0c2b8ca1dad447f8a',
    InstanceType='t2.micro',
    KeyName='cs351-2021',
    LaunchConfigurationName='1901182_launch_config',
    SecurityGroups=[
        'sg-01ab59ecd0a7dc68d',
    ],
    UserData=data,
)


response = client.create_auto_scaling_group(
    AutoScalingGroupName='1901182-auto-scaling-group',
    MaxSize=3,
    VPCZoneIdentifier='subnet-a89cb189',
    MinSize=1,
    LaunchConfigurationName='1901182_launch_config',
)


policy1 = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='1901182-auto-scaling-group',
    PolicyName='ScaleDown',
    ScalingAdjustment=-1,
)

policy2 = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='1901182-auto-scaling-group',
    PolicyName='ScaleUp',
    ScalingAdjustment=1,
)


cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_alarm(
    AlarmName='high_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=120,
    Statistic='Average',
    Threshold=80.0,
    AlarmDescription='Alarm when server CPU exceeds 80%',
    Dimensions=[
        {
          'Name': 'AutoScalingGroupName',
          'Value': '1901182-auto-scaling-group'
        },
    ],
    Unit='Seconds'
)

cloudwatch.put_metric_alarm(
    AlarmName='low_CPU_Utilization',
    ComparisonOperator='LessThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=120,
    Statistic='Average',
    Threshold=20.0,
    AlarmDescription='Alarm when server CPU is below 20%',
    Dimensions=[
        {
          'Name': 'AutoScalingGroupName',
          'Value': '1901182-auto-scaling-group'
        },
    ],
    Unit='Seconds'
)

