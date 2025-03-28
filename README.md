***Google Cloud Console:***
  
  Navigate to "IAM & Admin" -> "Service Accounts."
  Create a service account (or use an existing one).
  Grant it the "Cloud Vision API User" role.
  Create and download a JSON key file.

***Test it using docker run***

docker run \
  -e GOOGLE_CLOUD_PROJECT="qwiklabs-gcp-04-cd1eee3e5c2e" \
  -e IMAGE_URI="gs://unnati19201920/Copy of one1.jpeg" \
  -v "$(pwd)/YOUR_SERVICE_ACCOUNT_KEY_FILE.json:/app/service-account-key.json" \
  -e GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-key.json" \
  vision-api-app

***Same can be done using Cloud Run***

gcloud run deploy <service-name> \
  --image <image-url> \
  --region <region> \
  --service-account <service-account-email> \
  --set-env-vars GOOGLE_APPLICATION_CREDENTIALS=<path-to-json-file>
