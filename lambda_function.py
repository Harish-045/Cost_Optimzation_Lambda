import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    print(f"Total snapshots: {len(snapshots)}")

    for snap in snapshots:
        snapshot_id = snap['SnapshotId']
        volume_id = snap.get('VolumeId')

        print(f"Checking: {snapshot_id}, Volume: {volume_id}")

        try:
            # CASE 1: No volume linked
            if not volume_id:
                print(f"Deleting {snapshot_id} (no volume linked)")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                continue

            # CASE 2: Volume exists check
            vol = ec2.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]

            if not vol['Attachments']:
                print(f"Deleting {snapshot_id} (no attachments)")
                ec2.delete_snapshot(SnapshotId=snapshot_id)

        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                print(f"Deleting {snapshot_id} (volume not found)")
                ec2.delete_snapshot(SnapshotId=snapshot_id)