from google.cloud import aiplatform

from src.deploy_model.deploy_model_to_endpoint import deploy_model_to_endpoint
from src.initializing_configuration.configration import PROJECT_ID, REGION
from src.dataset.dataset_creation.dataset_creation import creating_dataset
from src.prediction.prediction_model import prediction_using_deployed_model
from src.training_model.model_training import training_model
from src.utils.constant import file_path
import pandas as pd


class Tabular_Template:
    def __init__(self):
        """
        getting the dataset and reading it
         @param dataset
        @type dataset
        """
        self.dataset = pd.read_csv(file_path)
        aiplatform.init(project=PROJECT_ID, location=REGION)
        self.pipeline()

    def pipeline(self):
        dataset_created = creating_dataset(self.dataset)
        model_training = training_model()
        deploy_model = deploy_model_to_endpoint()
        prediction = prediction_using_deployed_model()
        return prediction
