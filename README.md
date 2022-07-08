git clone https://github.com/fadheladlansyah/profile-app.git

cd profile-app

export PROJECT_ID=$(gcloud config get-value project)

gcloud iam service-accounts create sa-profile-app \
  --display-name "Service Account"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
--member serviceAccount:sa-profile-app@${PROJECT_ID}.iam.gserviceaccount.com \
--role roles/owner

gcloud iam service-accounts keys create ~/key.json \
--iam-account sa-profile-app@${PROJECT_ID}.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"




virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt




gcloud app create

export CLOUD_STORAGE_BUCKET=${PROJECT_ID}

gsutil mb gs://${PROJECT_ID}




python main.py




gcloud config set app/cloud_build_timeout 1000

gcloud app deploy