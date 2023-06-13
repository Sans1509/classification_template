from google.cloud import aiplatform

from src.initializing_configuration.configration import REGION, PROJECT_ID

aiplatform.init(project=PROJECT_ID, location=REGION)
deployed_model_display_name = "credit_card_defaulter_endpoint"
model_display_name = "my-automl-model"


def get_model_id():
    global model_id
    import requests

    # Set the endpoint URL
    service_endpoint = f"https://{REGION}-aiplatform.googleapis.com"
    parent = f"projects/{PROJECT_ID}/locations/{REGION}"

    # Set the request URL
    url = f"{service_endpoint}/v1/{parent}/models"

    # Get the access token using gcloud command
    access_token = "abc" #give your access code

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
        models = response.json()["models"]
        for model in models:
            if model["displayName"] == model_display_name:
                print(f"Model ID: {model['name']}")
                print(f"Display Name: {model['displayName']}")
                print(f"Create Time: {model['createTime']}")
                print("---")
                model_id = model['name'].split("/")[-1]
    else:
        print(f"Error: {response.status_code}, {response.text}")

    print(model_id)


Model_ID = get_model_id()


def deploy_model_to_endpoint(trained_model):
    Model = trained_model
    model_name = f"projects/{PROJECT_ID}/locations/{REGION}/models/{Model_ID}"
    model = aiplatform.Model(model_name=model_name)
    endpoint = model.deploy(
        deployed_model_display_name=deployed_model_display_name,
        machine_type="e2-highmem-4",
        sync=True
    )
    model.enable_feature_attributions = True
    aiplatform.gapic.ModelServiceClient().update_model(model=model)

    return endpoint
