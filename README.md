git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

cd python-docs-samples/codelabs/flex_and_vision

export PROJECT_ID=[YOUR_PROJECT_ID]

gcloud iam service-accounts create sacc \
  --display-name "Service Account"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
--member serviceAccount:sacc@${PROJECT_ID}.iam.gserviceaccount.com \
--role roles/owner

gcloud iam service-accounts keys create ~/key.json \
--iam-account sacc@${PROJECT_ID}.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"




virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt




gcloud app create

export CLOUD_STORAGE_BUCKET=${PROJECT_ID}

gsutil mb gs://${PROJECT_ID}




python main.py