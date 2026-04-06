# UNIFIED DEPLOYMENT TO GOOGLE CLOUD SERVICES

## What Changed

Your application is now **unified**:
- Backend (FastAPI) + Frontend (React) = ONE application
- Served from ONE Docker container
- Deployed on ONE Google Cloud project
- Single URL, no cross-origin requests

## Architecture

```
BEFORE (Separate Services):
  Vercel Frontend → API Calls → Render Backend

AFTER (Unified on GCP):
  Google Cloud Run
  ├── Backend API (FastAPI)
  └── Frontend UI (React) - served from same server
```

## Prerequisites

1. **Google Cloud Project** with billing enabled
   - Create at: https://console.cloud.google.com

2. **Google Cloud SDK** installed
   - Download: https://cloud.google.com/sdk/docs/install

3. **Docker** locally (optional)
   - Or use Cloud Build

---

## DEPLOYMENT OPTION 1: Google Cloud Run (Recommended)

### Best For:
- Serverless, auto-scaling
- Pay only for what you use
- Easier to manage
- Less operational overhead

### Step-by-Step:

#### 1. Initialize Google Cloud

```bash
# Install Google Cloud SDK first from: https://cloud.google.com/sdk/docs/install

# Login
gcloud auth login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Where YOUR_PROJECT_ID is from: https://console.cloud.google.com/welcome
```

#### 2. Enable Required APIs

```bash
gcloud services enable run.googleapis.com
gcloud services enable build.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

#### 3. Build and Push Docker Image

**Option A: Using gcloud builds (Recommended)**

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/coastal-ai-agent
```

**Option B: Using Docker locally**

```bash
docker build -f Dockerfile_GCP -t gcr.io/YOUR_PROJECT_ID/coastal-ai-agent .
docker push gcr.io/YOUR_PROJECT_ID/coastal-ai-agent
```

#### 4. Deploy to Cloud Run

```bash
gcloud run deploy coastal-ai-agent \
  --image gcr.io/YOUR_PROJECT_ID/coastal-ai-agent \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars JWT_SECRET=YOUR_JWT_SECRET_HERE \
  --set-env-vars TAVILY_API_KEY=YOUR_TAVILY_KEY_HERE \
  --set-env-vars GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID \
  --set-env-vars GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_SECRET \
  --set-env-vars GEMINI_MODEL=gemini-2.5-flash \
  --set-env-vars GEMINI_EMBED_MODEL=text-embedding-004 \
  --set-env-vars GCP_LOCATION=us-central1 \
  --set-env-vars CHROMA_COLLECTION=coastal_chunks_v3 \
  --set-env-vars GCP_SA_KEY_PATH=./service-account-key.json \
  --memory 2Gi \
  --cpu 2 \
  --timeout 3600s \
  --max-instances 10
```

#### 5. Get Your URL

```bash
gcloud run services describe coastal-ai-agent --region us-central1 --format 'value(status.url)'
```

**Your app will be at**: `https://coastal-ai-agent-xxxxx.run.app`

---

## DEPLOYMENT OPTION 2: Google App Engine

### Best For:
- Always-on applications
- Simpler management
- Traditional deployment model

### Step-by-Step:

#### 1. Initialize Google Cloud

```bash
gcloud init
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

#### 2. Create app.yaml (already provided)

File is at: `app.yaml`

All environment variables already set!

#### 3. Deploy

```bash
gcloud app deploy app.yaml
```

#### 4. Open Your App

```bash
gcloud app browse
```

**Your app will be at**: `https://YOUR_PROJECT_ID.uc.r.appspot.com`

---

## FILES PROVIDED

```
api/main_unified.py        - Unified backend + frontend server
Dockerfile_GCP             - Docker image for GCP
app.yaml                   - App Engine configuration
GCP_DEPLOYMENT_GUIDE.md    - This file
```

---

## ENVIRONMENT VARIABLES

All already set in deployment commands. They are:

```
JWT_SECRET                 - Authentication token secret
TAVILY_API_KEY            - Web search API
GOOGLE_CLIENT_ID          - OAuth authentication
GOOGLE_CLIENT_SECRET      - OAuth authentication
GEMINI_MODEL              - AI model
GEMINI_EMBED_MODEL        - Embedding model
GCP_LOCATION              - Default region
CHROMA_COLLECTION         - Database collection
GCP_SA_KEY_PATH           - Service account credentials
```

---

## TESTING YOUR DEPLOYMENT

### Cloud Run:

```bash
# Get URL
URL=$(gcloud run services describe coastal-ai-agent --region us-central1 --format 'value(status.url)')

# Test health check
curl $URL/health

# Open in browser
open $URL
```

### App Engine:

```bash
# Test health check
curl https://YOUR_PROJECT_ID.uc.r.appspot.com/health

# Open in browser
gcloud app browse
```

---

## TROUBLESHOOTING

### "Permission denied" errors

```bash
# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable build.googleapis.com

# Check project setting
gcloud config get-value project
```

### "Image not found"

```bash
# Replace YOUR_PROJECT_ID with actual ID
gcloud config get-value project

# Rebuild image
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/coastal-ai-agent
```

### "Deployment failed"

```bash
# Check logs
gcloud run logs read coastal-ai-agent --region us-central1 --limit 50

# For App Engine
gcloud app logs read
```

### "Frontend not loading"

- Ensure `api/static/index.html` exists
- Check that static files are properly copied to container
- Check logs for file path errors

### "API calls failing"

- Verify all environment variables are set
- Check CORS settings in `main_unified.py`
- Review server logs

---

## MONITORING

### Cloud Run

```bash
# View dashboard
gcloud run dashboard

# Check logs
gcloud run logs read coastal-ai-agent --region us-central1

# View metrics
gcloud monitoring dashboards list
```

### App Engine

```bash
# View dashboard
gcloud app browse

# Check logs
gcloud app logs read -f
```

---

## SCALING

### Cloud Run

Auto-scales based on requests. Configure limits:

```bash
gcloud run deploy coastal-ai-agent \
  --max-instances 50 \
  --min-instances 1
```

### App Engine

Set in `app.yaml`:

```yaml
automatic_scaling:
  min_instances: 1
  max_instances: 50
```

---

## COSTS

### Cloud Run (Recommended)
- **Free**: 2 million requests/month
- **Pay**: $0.25 per 1 million requests
- **Compute**: First 180,000 GB-seconds free/month
- **Average**: $5-20/month

### App Engine
- **Free tier**: Limited
- **Average**: $7-15/month
- **24/7 pricing**: Always running

### Total with GCP Services
- **Per month**: $10-30
- **Includes**: Storage, APIs, database
- **Much cheaper than**: Separate Render + Vercel

---

## KEY COMMANDS

### Cloud Run

```bash
# Deploy
gcloud run deploy coastal-ai-agent --image gcr.io/YOUR_PROJECT_ID/coastal-ai-agent --platform managed --region us-central1

# View details
gcloud run services describe coastal-ai-agent --region us-central1

# View logs
gcloud run logs read coastal-ai-agent --region us-central1

# Update environment variables
gcloud run deploy coastal-ai-agent --update-env-vars KEY=VALUE

# Delete
gcloud run services delete coastal-ai-agent --region us-central1
```

### App Engine

```bash
# Deploy
gcloud app deploy app.yaml

# View details
gcloud app describe

# View logs
gcloud app logs read -f

# Delete version
gcloud app versions delete VERSION_ID

# Split traffic
gcloud app services set-traffic default --splits v1=0.5,v2=0.5
```

---

## NEXT STEPS CHECKLIST

- [ ] Create Google Cloud project
- [ ] Install Google Cloud SDK
- [ ] Run `gcloud init`
- [ ] Enable APIs
- [ ] Build Docker image
- [ ] Deploy to Cloud Run or App Engine
- [ ] Get your URL
- [ ] Test the application
- [ ] Share with users!

---

## SUCCESS INDICATORS

✅ Cloud Run shows "Serving traffic"
✅ App Engine shows green checkmark
✅ Health endpoint responds: `/health`
✅ Frontend loads at root URL `/`
✅ API responds at `/api/...`
✅ No CORS errors in console
✅ OAuth login works
✅ Can ask questions and get responses

---

## ADDITIONAL RESOURCES

- Cloud Run Docs: https://cloud.

.com/run/docs
- App Engine Docs: https://cloud.google.com/appengine/docs
- Pricing Calculator: https://cloud.google.com/products/calculator
- Support: https://cloud.google.com/support

---

**You're ready to deploy on Google Cloud!** 

Choose your platform (Cloud Run or App Engine) and follow the steps above.

Good luck!
