#!/bin/bash
set -e

PROJECT_ID="project-69cd4571-9df8-49d0-93d"
REGION="us-central1"
SERVICE="coastal-agent"
IMAGE="gcr.io/$PROJECT_ID/$SERVICE"

echo "==> Setting project..."
gcloud config set project $PROJECT_ID

echo "==> Enabling required APIs..."
gcloud services enable run.googleapis.com containerregistry.googleapis.com --quiet

echo "==> Building and pushing image (this takes ~5 min first time)..."
gcloud builds submit --tag $IMAGE .

echo "==> Deploying to Cloud Run..."
gcloud run deploy $SERVICE \
  --image $IMAGE \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300 \
  --concurrency 10

echo ""
echo "==> DONE! Your app URL:"
gcloud run services describe $SERVICE --platform managed --region $REGION --format "value(status.url)"
