Complete ML project with CICD
dagshub: https://dagshub.com/ishwarky15/Chestcancerdetection.mlflow
import dagshub
dagshub.init(repo_owner='ishwarky15', repo_name='Chestcancerdetection', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
