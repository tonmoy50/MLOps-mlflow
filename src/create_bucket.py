from minio import Minio
# from minio.error import ResponseError
import json
import os
from dotenv import load_dotenv

load_dotenv()


minioClient = Minio(os.environ['MLFLOW_S3_ENDPOINT_URL'].split('//')[1],
                  access_key=os.environ['AWS_ACCESS_KEY_ID'],
                  secret_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                  secure=False)

# minioClient = Minio(os.environ['MLFLOW_S3_ENDPOINT_URL'], #.split('//')[1],
#                   access_key="minioadmin",
#                   secret_key="minioadmin",
#                   secure=False)

minioClient.list_buckets()
bucket_name = "mlflow-test2"
try:
    minioClient.make_bucket(bucket_name)
    print("Bucket Created")
except Exception as err:
    print(err)

buckets = minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

policy = {"Version":"2012-10-17",
        "Statement":[
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetBucketLocation",
            "Resource":f"""arn:aws:s3:::{bucket_name}"""
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:ListBucket",
            "Resource":f"""arn:aws:s3:::{bucket_name}"""
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetObject",
            "Resource":f"""arn:aws:s3:::{bucket_name}/*"""
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:PutObject",
            "Resource":f"""arn:aws:s3:::{bucket_name}/*"""
            }

        ]}

minioClient.set_bucket_policy(bucket_name, json.dumps(policy))

# List all object paths in bucket that begin with my-prefixname.
objects = minioClient.list_objects(bucket_name, prefix='my',
                              recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)