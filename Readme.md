# MLOps with MLFlow


## Run
1. Direct run the file using `python 'filename.py'`
2. Run project having MLproject and conda.yaml file inside using `mlflow run 'folder_name' -P param1=0.42`
3. Directly run from repo `mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=5.0`

## Run Tracker UI
`mlflow ui`

## Serve model as a REST API
`mlflow models serve -m /Users/mlflow/mlflow-prototype/mlruns/0/7c1a0d5c42844dcdb8f5191146925174/artifacts/model -p 1234`

## MLflow Server
```
mlflow server -p <exposed_port_for_mlflow> \
 --host 0.0.0.0 \
 --backend-store-uri <enter_backend_store_uri> \
 --default-artifact-root <enter_deafult_artifact_root>
 ```

Sample request, 
```
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}' http://127.0.0.1:1234/invocations
```

## Build Docker Image
```
mlflow models build-docker \
-m /Users/macbookpro/Desktop/Graaho/Renforce/MLOps-mlflow/mlruns/0/995c8dfddcbd4b5ab29c294147aec187/artifacts/model \
-n my-docker-image \
--enable-mlserver
```

## Configure MySQL

`pip install pymysql`

```
CREATE USER ‘mlflow-user’ IDENTIFIED BY ‘password’;
CREATE DATABASE ‘mlflowruns’;
GRANT ALL PRIVILEGES ON mlflowruns.* TO ‘mlflow-user’;
```

uri would be, `mysql+pymysql://'mlflow-user':'password'@localhost:3306/mlflowruns`

## Setting up MinIO
Pull docker build of minio, `docker pull minio/minio`

Run minio server using,
```
docker run \
  -p 9000:9000 \
  -p 9001:9001 \
  --name minio1 \
  -e "MINIO_ROOT_USER=minio" \
  -e "MINIO_ROOT_PASSWORD=minio1234" \
  -v /Users/macbookpro/data:/data \
  quay.io/minio/minio server /data --console-address ":9001"
```

default artifact - `s3://mlflow/artifacts`

Install dependencies, 
```
pip3 install minio
pip3 install boto3
```

Setup local environment variables
```
export MLFLOW_S3_ENDPOINT_URL=http://127.0.0.1:<exposed_port_for_minio>
export AWS_ACCESS_KEY_ID=<your_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_secret_key>
```

### Create Bucket 
`python create_bucket.py`


## Redis in Docker

Run the following command to setup redis in docker, 
`docker run -d -p 6379:6379 redis`