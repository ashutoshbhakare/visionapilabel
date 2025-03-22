=====
Same can be done using Cloud Run
=====
gcloud run deploy <service-name> \
  --image <image-url> \
  --region <region> \
  --service-account <service-account-email> \
  --set-env-vars GOOGLE_APPLICATION_CREDENTIALS=<path-to-json-file>
