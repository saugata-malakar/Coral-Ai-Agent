#!/bin/bash
# Coastal AI Agent - Complete Deployment Script
# Supports: Render Backend + Vercel Frontend

set -e

echo "🚀 COASTAL AI AGENT - DEPLOYMENT SCRIPT"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# ====== CONFIG ======
GITHUB_REPO=""
RENDER_SERVICE="coastal-ai-agent-api"
VERCEL_DOMAIN="coastal-ai-agent-frontend"

echo -e "${BLUE}>>> Prerequisites Check ${NC}"
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git required${NC}"
    exit 1
fi
echo "✅ Git: OK"

echo ""
echo -e "${BLUE}>>> Step 1: GitHub Setup ${NC}"
read -p "Enter GitHub repository URL (or press enter to skip): " github_url

if [ -n "$github_url" ]; then
    GITHUB_REPO="$github_url"
    
    if [ ! -d .git ]; then
        git init
    fi
    
    if ! git remote get-url origin &> /dev/null; then
        git remote add origin "$GITHUB_REPO"
    fi
    
    git add .
    git commit -m "feat: Complete Coastal AI Agent deployment" || true
    git branch -M main
    git push -u origin main
    
    echo -e "${GREEN}✅ Code pushed to GitHub${NC}"
    echo "   Repository: $GITHUB_REPO"
fi

echo ""
echo -e "${BLUE}>>> Step 2: Backend Configuration (Render) ${NC}"
echo "render.yaml is ready. To deploy manually:"
echo "1. Go to https://render.com"
echo "2. New Service → Web Service"
echo "3. Connect repository"
echo "4. Configure with render.yaml"
echo "5. Add environment variables:"
echo "   - JWT_SECRET"
echo "   - GOOGLE_CLIENT_ID"
echo "   - GOOGLE_CLIENT_SECRET"  
echo "   - TAVILY_API_KEY"
echo "   - GCP service account key"
echo ""
echo -e "${YELLOW}ℹ️  Save Backend URL:${NC}"
read -p "(you'll use this for frontend) Render API URL: " RENDER_API_URL

echo ""
echo -e "${BLUE}>>> Step 3: Frontend Setup (Vercel) ${NC}"
echo "vercel.json is ready. To deploy manually:"
echo "1. Go to https://vercel.com"
echo "2. New Project → Import Git Repo"
echo "3. Framework: Other"
echo "4. Build Command: npm run build"
echo "5. Output: dist/"
echo "6. Environment: REACT_APP_API_URL=$RENDER_API_URL"
echo "7. Deploy!"

if command -v vercel &> /dev/null; then
    echo ""
    read -p "Deploy frontend to Vercel now? (y/n): " vercel_deploy
    if [ "$vercel_deploy" = "y" ]; then
        cd api/static
        echo "Deploying frontend..."
        vercel --prod --env REACT_APP_API_URL="$RENDER_API_URL"
        cd ../../
        echo -e "${GREEN}✅ Frontend deployed!${NC}"
    fi
fi

echo ""
echo -e "${BLUE}>>> Summary ${NC}"
echo "✅ Repository: Ready on GitHub"
echo "📦 Backend: Deploy to Render (render.yaml configured)"
echo "🎨 Frontend: Deploy to Vercel (vercel.json configured)"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Set environment variables on Render"
echo "2. Upload service account key to Render"
echo "3. Deploy backend on Render dashboard"
echo "4. Configure frontend with backend API URL"
echo "5. Deploy frontend on Vercel"
echo ""
echo "See DEPLOYMENT_GUIDE.md for detailed instructions"
echo -e "${GREEN}🎉 Ready to deploy! 🎉${NC}"
