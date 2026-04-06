#!/bin/bash
# REBUILD COASTAL AI AGENT ON GOOGLE CLOUD RUN

PROJECT_ID="true-shoreline-447519-g7"
SERVICE_NAME="coastal-ai-agent"
REGION="us-central1"

echo "=========================================="
echo "REBUILDING COASTAL AI AGENT ON GCP"
echo "=========================================="

# Step 1: Make sure we're in the API directory
echo ""
echo "Step 1: Preparing build..."
cd api || { echo "ERROR: api directory not found"; exit 1; }

# Step 2: Check if Dockerfile exists
if [ ! -f "Dockerfile" ]; then
    echo "ERROR: Dockerfile not found in api/ directory"
    exit 1
fi

# Step 3: Build local Docker image (optional, for testing)
echo ""
echo "Step 2: Building Docker image locally..."
docker build -t gcr.io/$PROJECT_ID/$SERVICE_NAME:latest .

if [ $? -ne 0 ]; then
    echo "ERROR: Local build failed"
    exit 1
fi

# Step 4: Push to Google Container Registry
echo ""
echo "Step 3: Pushing to Google Container Registry..."
docker push gcr.io/$PROJECT_ID/$SERVICE_NAME:latest

if [ $? -ne 0 ]; then
    echo "ERROR: Push failed"
    exit 1
fi

# Step 5: Deploy to Cloud Run
echo ""
echo "Step 4: Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME:latest \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars JWT_SECRET=$JWT_SECRET \
  --set-env-vars TAVILY_API_KEY=$TAVILY_API_KEY \
  --set-env-vars GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID \
  --set-env-vars GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET \
  --set-env-vars GEMINI_MODEL=gemini-2.5-flash \
  --set-env-vars GEMINI_EMBED_MODEL=text-embedding-004 \
  --set-env-vars GCP_LOCATION=us-central1 \
  --set-env-vars CHROMA_COLLECTION=coastal_chunks_v3 \
  --set-env-vars GCP_SA_KEY_PATH=./service-account-key.json \
  --memory 2Gi \
  --cpu 2 \
  --timeout 3600s \
  --max-instances 10

if [ $? -ne 0 ]; then
    echo "ERROR: Cloud Run deployment failed"
    exit 1
fi

# Step 6: Get the service URL
echo ""
echo "=========================================="
echo "DEPLOYMENT SUCCESS!"
echo "=========================================="
echo ""
gcloud run services describe $SERVICE_NAME --region $REGION --format 'value(status.url)'
echo ""
echo "Your Coastal AI Agent is LIVE!"
