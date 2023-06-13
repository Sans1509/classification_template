from google.cloud import aiplatform
from src.initializing_configuration import configration

PROJECT_ID = configration.PROJECT_ID
REGION = configration.REGION
aiplatform.init(project=PROJECT_ID, location=REGION)

aiplatform.init(staging_bucket='gs://my-bucket')


def creating_dataset(dataset):
    my_dataset = aiplatform.TabularDataset.create(
        display_name="credit_card_defaulter", gcs_source=['gs://'])

    return my_dataset
