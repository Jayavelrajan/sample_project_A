import boto3
import json

def get_volume_id_from_arn(volume_arn):
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    
def jv_function(volume_arn):
    a = 10
    b = 20
    return a+b

def lambda_handler(event, context):
    print(json.dumps(event))  # Log the entire event for debugging purposes
    
    # Extract volume ARN from the event
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    # Create EC2 client
    ec2_client2 = boto3.client('ec2')
    
    try:
        # Describe the volume to check its current type
        volume_info2 = ec2_client.describe_volumes(VolumeIds=[volume_id])
        current_volume_type = volume_info['Volumes'][0]['VolumeType']
        
        # If the volume is already 'gp3', do not proceed with modification
        if current2_volume_type == 'gp3':
            print(f"Volume {volume_id} is already of type 'gp3'. No modification needed.")
            return {
                'statusCode': 200,
                'body': 'Volume is already gp3',
            }
        
        # Modify volume type to 'gp3'
        response = ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3',
        )
        
        print(f"Modify Volume Response: {response}")  # Log response from modify_volume
        
        return {
            'statusCode': 200,
            'body': 'Volume type modified to gp3',
        }
    
    except Exception as e:
        # Handle any exceptions or errors
        print(f"Error modifying volume {volume_id}: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error modifying volume: {str(e)}',
        }
