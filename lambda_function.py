import boto3
 
def get_volume_id_from_arn(volume_arn)
    return event['resources'][0]
 
def lambda_handler(event, context):
    print("bawlat")
event = {
   "version":"0",
   "id":"e3a05d37-8835-ef55-8b5e-c63ab336834a",
   "detail-type":"EBS Volume Notification",
   "source":"aws.ec2",
   "account":"825317365117",
   "time":"2024-02-28T12:31:51Z",
   "region":"ap-south-1",
   "resources":[
      "arn:aws:ec2:ap-south-1:825317365117:volume/vol-0dfc2516b2fb6defc"
   ],
   "detail":{
      "result":"available",
      "cause":"",
      "event":"createVolume",
      "request-id":"81532611-19cf-4549-8056-a254a2f03369"
   }
}
 
print(event)
