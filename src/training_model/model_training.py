from google.cloud import aiplatform
from src.initializing_configuration import configration

REGION = configration.REGION
PROJECT_ID = configration.PROJECT_ID
aiplatform.init(project=PROJECT_ID, location=REGION)


def training_model():
    def get_dataset_id():
        global dataset_name
        import requests

        # Set the endpoint URL
        service_endpoint = f"https://{REGION}-aiplatform.googleapis.com"
        parent = f"projects/{PROJECT_ID}/locations/{REGION}"

        # Set the request URL
        url = f"{service_endpoint}/v1/{parent}/datasets"

        # Get the access token using gcloud command

        access_token = "abc" #update your access token


        # Set the headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Send the GET request
        response = requests.get(url, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # Print the response content
            datasets = response.json()["datasets"]
            for my_dataset in datasets:
                print(f"Dataset ID: {my_dataset['name']}")
                dataset_name = my_dataset['name']
                print(f"Display Name: {my_dataset['displayName']}")
                print(f"Create Time: {my_dataset['createTime']}")
                print("---")
                dataset_name = my_dataset['name']
        else:
            print(f"Error: {response.status_code}, {response.text}")

        return dataset_name

    DATASET_ID = get_dataset_id()
    dataset = aiplatform.TabularDataset(DATASET_ID)

    job = aiplatform.AutoMLTabularTrainingJob(
        display_name="Credit_Card_defaulter_training",  # user defined
        optimization_prediction_type="classification",
    )

    model = job.run(
        dataset=dataset,
        target_column="defaulter",  # user defined
        training_fraction_split=0.6,
        validation_fraction_split=0.2,
        test_fraction_split=0.2,
        budget_milli_node_hours=1000,
        model_display_name="my-automl-model",
        disable_early_stopping=False,
    )
    return model
