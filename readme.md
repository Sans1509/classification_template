To run :
install google cloud aiplatform using command - pip install google-cloud-aiplatform
Run the class Tabular_Template() from main.py .
 
Constant :
1 . The file path of the dataset is set in constant.py of utils , you can make changes in the file to input your dataset path.

2 . PROJECT_ID , REGION is mentioned in configuration.py of initializing_configuration , you can make changes over there.

3 . In dataset_creation.py ,
    gcs_source = Update your gcs path here.

3 . In model_training.py , 
    access_token = Update your access token. 
    command to get access token (run this on terminal) - gcloud auth application-default print-access-token
    - update your target column in running the model job.

4 . In deploy_model_to_endpoint.py ,
    - model_display_name is mentioned manually , you can change it if you want but you have to change the model name while training the model as well , so make changes in model_training.py file as well.
    - Update your access token
    - deployed_model_display_name is mentioned , you can change it according to your preference.


5 . In prediction_model.py ,
    Update your columns and value for which you want to make prediction.

6 . If you want to undeploy your model , this is the command ,
    endpoint.undeploy(deployed_model_id=prediction.deployed_model_id)


THANK YOU   