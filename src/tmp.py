from json import load
import mlflow
from dotenv import load_dotenv

load_dotenv()

mlflow.set_experiment("1")
print(mlflow.get_registry_uri())
print(mlflow.get_tracking_uri())
print(mlflow.get_artifact_uri())

mlflow.log_artifact("./src/create_bucket.py")