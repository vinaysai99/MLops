# Understanding MLflow

## Introduction
MLflow is an open-source platform designed to streamline and manage the machine learning (ML) lifecycle. It provides tools for tracking experiments, storing artifacts, managing models, and deploying them for inference. This document will guide new users through the key features of MLflow.

## Why Use MLflow?
- **Experiment Tracking**: Keep records of model training runs.
- **Artifact Management**: Store datasets, models, and output files.
- **Model Registry**: Manage different versions of trained models.
- **Model Deployment**: Easily deploy trained models for predictions.

## Key MLflow Components

### 1. Experiments
An MLflow experiment is a way to organize multiple training runs. Each experiment contains multiple runs with unique settings, parameters, and results.

#### Creating and Setting an Experiment:
```python
import mlflow
mlflow.set_experiment("my_experiment")
```

#### Viewing Experiments:
```python
mlflow.list_experiments()
```

### 2. Runs
A run represents a single execution of a training script. It logs parameters, metrics, and artifacts.

#### Starting and Logging a Run:
```python
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
```

#### Fetching Run Details:
```python
runs = mlflow.search_runs()
print(runs)
```

### 3. Artifacts
Artifacts are files generated during a run, such as models, logs, plots, and datasets.

#### Logging Artifacts:
```python
mlflow.log_artifact("model.pkl")
```

#### Viewing Artifact Location:
```python
artifacts_uri = mlflow.get_artifact_uri()
print(artifacts_uri)
```

### 4. Model Registry
The Model Registry helps track, manage, and version different trained models, allowing easy access for deployment.

#### Registering a Model:
```python
result = mlflow.register_model("runs:/<run_id>/model", "MyModel")
```

#### Fetching Model Details:
```python
from mlflow.tracking import MlflowClient
client = MlflowClient()
client.get_registered_model("MyModel")
```

### 5. Inference
Inference is the process of using a trained model to make predictions on new data.

#### Loading a Registered Model:
```python
import mlflow.pyfunc
model = mlflow.pyfunc.load_model("models:/MyModel/1")
predictions = model.predict(data)
```

#### Deploying a Model as an API:
```sh
mlflow models serve -m "models:/MyModel/1" --port 5000
```

## Conclusion
MLflow is a powerful tool for managing machine learning workflows. By tracking experiments, storing artifacts, registering models, and deploying them for inference, MLflow improves collaboration, reproducibility, and efficiency in ML projects. Beginners can start using MLflow with minimal setup and expand their usage as their projects grow.

