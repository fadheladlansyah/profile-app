# Profile Web App

Simple profile web app deployed on Google App Engine

## How-to

Get resources

`git clone https://github.com/fadheladlansyah/profile-app.git`

`cd profile-app`

Config env

`export PROJECT_ID=$(gcloud config get-value project)`

``gcloud iam service-accounts create sa-profile-app --display-name "Service Account"``

``gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:sa-profile-app@${PROJECT_ID}.iam.gserviceaccount.com --role roles/owner``

``gcloud iam service-accounts keys create ~/key.json --iam-account sa-profile-app@${PROJECT_ID}.iam.gserviceaccount.com``

`export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r requirements.txt`

`gcloud services enable appengine.googleapis.com`

`gcloud app create`

`export CLOUD_STORAGE_BUCKET=${PROJECT_ID}`

`gsutil mb gs://${PROJECT_ID}`

_upload image named "profile_image.jpg" to the bucket_

## Deployment

Test locally

`python main.py`

_modify app.yaml specify CLOUD_STORAGE_BUCKET value_

`gcloud config set app/cloud_build_timeout 1000`

`gcloud app deploy`