#!/bin/bash
# 🚀 Final Deployment Script for Coastal AI Agent
# Deploy to HuggingFace Spaces with all configurations

set -e

echo "========================================="
echo "🚀 COASTAL AI AGENT - FINAL DEPLOYMENT"
echo "========================================="
echo ""

# Step 1: Verify all files are in place
echo "✓ Step 1: Verifying project structure..."

FILES=(
  "api/main.py"
  "api/requirements.txt"
  "api/app/auth.py"
  "api/app/auth_routes.py"
  "api/app/routes.py"
  "api/app/agent.py"
  "api/app/config.py"
  "api/static/index.html"
  "api/static/auth.html"
  "api/static/professor-profile.html"
  "Dockerfile"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "  ✓ $file"
  else
    echo "  ✗ MISSING: $file"
    exit 1
  fi
done

echo ""
echo "✓ All required files present!"
echo ""

# Step 2: Create assets directory
echo "✓ Step 2: Creating assets directory..."
mkdir -p api/static/assets
echo "  ✓ api/static/assets/ created"
echo ""

# Step 3: Display environment variables needed
echo "✓ Step 3: Environment Variables to Configure"
echo "  (Add these to HuggingFace Spaces secrets)"
echo ""
echo "  REQUIRED:"
echo "  - GOOGLE_CLIENT_ID (you have this ✓)"
echo "  - GOOGLE_CLIENT_SECRET (you have this ✓)"
echo "  - SENDGRID_API_KEY (get from sendgrid.com)"
echo ""
echo "  COPY FROM YOUR .env FILE:"
echo "  - JWT_SECRET"
echo "  - TAVILY_API_KEY"
echo "  - GCP_PROJECT"
echo "  - GCP_SA_KEY_PATH"
echo ""

# Step 4: Verify Dockerfile
echo "✓ Step 4: Verifying Dockerfile..."
if grep -q "uvicorn" Dockerfile; then
  echo "  ✓ Dockerfile configured correctly"
else
  echo "  ✗ Dockerfile may need updates"
fi
echo ""

# Step 5: Check requirements.txt
echo "✓ Step 5: Verifying Python dependencies..."
if grep -q "sendgrid" api/requirements.txt; then
  echo "  ✓ SendGrid package added"
else
  echo "  ✗ Warning: SendGrid not in requirements"
fi
echo ""

echo "========================================="
echo "✅ VALIDATION COMPLETE!"
echo "========================================="
echo ""
echo "NEXT STEPS FOR DEPLOYMENT:"
echo ""
echo "1. Go to: https://huggingface.co/spaces"
echo "2. Click 'Create new Space'"
echo "3. Name: coastal-ai-agent"
echo "4. Type: Docker"
echo "5. Visibility: Public"
echo ""
echo "6. Clone space:"
echo "   git clone https://huggingface.co/spaces/YOUR_USERNAME/coastal-ai-agent"
echo "   cd coastal-ai-agent"
echo ""
echo "7. Copy all files from this repo to the space"
echo ""
echo "8. Create assets directory and add:"
echo "   mkdir -p api/static/assets"
echo "   # Copy prof-photo.jpg to api/static/assets/"
echo ""
echo "9. Push to HF:"
echo "   git add ."
echo "   git commit -m 'Deploy Coastal AI Agent v2.0'"
echo "   git push"
echo ""
echo "10. In HF Spaces UI → Settings → Secrets → Add:"
echo "    - GOOGLE_CLIENT_ID"
echo "    - GOOGLE_CLIENT_SECRET"
echo "    - SENDGRID_API_KEY"
echo "    - JWT_SECRET"
echo "    - TAVILY_API_KEY"
echo "    - GCP_PROJECT"
echo "    - GCP_SA_KEY_PATH"
echo ""
echo "11. HF Spaces will auto-build (~10 minutes)"
echo "    Your app will be live at:"
echo "    https://huggingface.co/spaces/YOUR_USERNAME/coastal-ai-agent"
echo ""
echo "========================================="
