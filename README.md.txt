# AWS Cost Optimization using Lambda

Identifying Stale EBS Snapshots
In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

Description:
The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.

## Services Used
- AWS Lambda
- Amazon EC2
- Amazon EBS
- CloudWatch Logs

## Working
- Finds all EBS snapshots
- Checks attached volumes
- Deletes orphan or unused snapshots
- Runs automatically or manually

## Architecture
Lambda → EC2 → EBS Snapshots → CloudWatch Logs

## How it Works
1. Lambda fetches snapshots
2. Checks volume and instance status
3. Deletes unused snapshots
4. Logs output in CloudWatch

## Author
Your Name