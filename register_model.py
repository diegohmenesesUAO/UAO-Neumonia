import mlflow
import mlflow.keras
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np

# Cargar el modelo desde el archivo local
model = load_model('model/conv_MLP_84.h5')

# Crear una entrada de ejemplo para la firma
input_example = np.random.rand(1, 512, 512, 1).astype(np.float32)

# Iniciar una nueva ejecución en MLflow
with mlflow.start_run() as run:
    # Guardar el modelo en MLflow con una firma
    mlflow.keras.log_model(
        model,
        "model",
        signature=mlflow.models.infer_signature(input_example, model.predict(input_example)),
        input_example=input_example
    )
    
    # Registrar el modelo en el Model Registry de MLflow
    model_uri = f"runs:/{run.info.run_id}/model"
    mlflow.register_model(model_uri, "PneumoniaDetectionModel")
