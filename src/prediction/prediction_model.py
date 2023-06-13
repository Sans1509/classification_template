from google.cloud import aiplatform

from src.initializing_configuration.configration import PROJECT_ID, REGION

aiplatform.init(project=PROJECT_ID, location=REGION)

input_data = [
    {
        "LIMIT_BAL": '140000.0',
        "PAY_0": '0.0',
        "PAY_2": '0.0',
        "PAY_3": '0.0',
        "PAY_4": '0.0',
        "PAY_6": '0.0',
        "BILL_AMT1": '22453.0',
        "BILL_AMT2": '21295.0',
        "BILL_AMT3": '20116.0',
        "PAY_AMT1": '2100.0',
        "PAY_AMT2": '2010.0',
        "PAY_AMT3": '1806.0',
        "PAY_AMT4": '1500.0',
        "PAY_AMT5": '1500.0'
    }
]


def prediction_using_deployed_model():
    client = aiplatform.gapic.EndpointServiceClient(
        client_options={"api_endpoint": f"{REGION}-aiplatform.googleapis.com"})

    endpoints = client.list_endpoints(parent=f"projects/{PROJECT_ID}/locations/{REGION}")

    endpoint_id = ''
    for endpoint in endpoints:
        endpoint_id = endpoint.name.split("/")[-1]

    aiplatform.init(project=PROJECT_ID, location=REGION)
    endpoint = aiplatform.Endpoint(endpoint_id)

    prediction = endpoint.predict(instances=input_data)
    return prediction
