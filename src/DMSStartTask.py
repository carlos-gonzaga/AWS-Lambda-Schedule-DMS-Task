import boto3


def start_task(task_arn):
    try:    
        client = boto3.client('dms')
        response = client.start_replication_task(
            ReplicationTaskArn=task_arn,
            StartReplicationTaskType='reload-target'
        )
        print(f'Task started successfully: %s' %(task_arn))
    except Exception as e:
        print('Error starting DMS task ...' + str(e))
    return response


def lambda_handler(event, context):
    for id in event:
        print(f'Starting Task %s...' %(id))
        start_task(event[id])
