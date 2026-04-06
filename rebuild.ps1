# FIX CLOUD RUN DEPLOYMENT - PowerShell Version

$PROJECT_ID = "true-shoreline-447519-g7"
$SERVICE_NAME = "coastal-ai-agent"
$REGION = "us-central1"

Write-Host "=========================================="
Write-Host "REBUILDING COASTAL AI AGENT ON GCP"
Write-Host "=========================================="

# Step 1: Navigate to api directory
Write-Host ""
Write-Host "Step 1: Preparing build..."
Push-Location api

if (-not (Test-Path "Dockerfile")) {
    Write-Host "ERROR: Dockerfile not found in api/ directory"
    Pop-Location
    exit 1
}

# Step 2: Build Docker image
Write-Host ""
Write-Host "Step 2: Building Docker image..."
docker build -t gcr.io/$PROJECT_ID/$SERVICE_NAME:latest .

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Docker build failed"
    Pop-Location
    exit 1
}

# Step 3: Push to Google Container Registry
Write-Host ""
Write-Host "Step 3: Pushing to Google Container Registry..."
docker push gcr.io/$PROJECT_ID/$SERVICE_NAME:latest

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Docker push failed"
    Pop-Location
    exit 1
}

# Step 4: Deploy to Cloud Run
Write-Host ""
Write-Host "Step 4: Deploying to Cloud Run..."

$envVars = @(
    "JWT_SECRET=$env:JWT_SECRET",
    "TAVILY_API_KEY=$env:TAVILY_API_KEY",
    "GOOGLE_CLIENT_ID=$env:GOOGLE_CLIENT_ID",
    "GOOGLE_CLIENT_SECRET=$env:GOOGLE_CLIENT_SECRET",
    "GEMINI_MODEL=gemini-2.5-flash",
    "GEMINI_EMBED_MODEL=text-embedding-004",
    "GCP_LOCATION=us-central1",
    "CHROMA_COLLECTION=coastal_chunks_v3",
    "GCP_SA_KEY_PATH=./service-account-key.json"
)

$envString = ($envVars -join ',')

gcloud run deploy $SERVICE_NAME `
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME:latest `
  --platform managed `
  --region $REGION `
  --allow-unauthenticated `
  --set-env-vars $envString `
  --memory 2Gi `
  --cpu 2 `
  --timeout 3600 `
  --max-instances 10

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Cloud Run deployment failed"
    Pop-Location
    exit 1
}

# Step 5: Get service URL
Write-Host ""
Write-Host "=========================================="
Write-Host "DEPLOYMENT SUCCESS!"
Write-Host "=========================================="
Write-Host ""

gcloud run services describe $SERVICE_NAME --region $REGION --format 'value(status.url)'

Write-Host ""
Write-Host "Your Coastal AI Agent is LIVE!"
Write-Host ""

Pop-Location
