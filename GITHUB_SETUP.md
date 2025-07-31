# Quick GitHub Setup & Deployment Guide

## 🔗 Push to GitHub

### Step 1: Create GitHub Repository
1. Go to [github.com](https://github.com) and log in
2. Click "New repository" 
3. Name it: `ecfr-agency-regulations-api`
4. Keep it public for easy deployment
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Push Your Code
```bash
# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ecfr-agency-regulations-api.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🚀 Deploy Publicly

### Option 1: Railway (Recommended - Easiest)
1. Visit [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "Deploy from GitHub repo"
4. Select your `ecfr-agency-regulations-api` repository
5. Railway auto-detects Python and deploys!
6. **Your API will be live at**: `https://your-app-name.railway.app`

### Option 2: Render (Also Free)
1. Visit [render.com](https://render.com)
2. Sign up with GitHub
3. "New Web Service" → Connect repository
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
5. Deploy and get your URL!

### Option 3: Heroku
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Commands:
   ```bash
   heroku login
   heroku create your-ecfr-api
   git push heroku main
   ```

## 🌐 Access Your Live API

Once deployed, your API will be publicly accessible:
- **Main API**: `https://your-app.platform.com/`
- **All Agencies**: `https://your-app.platform.com/agencies`
- **Specific Agency**: `https://your-app.platform.com/agencies/Environmental%20Protection%20Agency`
- **Interactive Docs**: `https://your-app.platform.com/docs`
- **API Status**: `https://your-app.platform.com/status`

## 📊 Features Available

✅ **48 Federal Agencies** with regulation sizes in MB  
✅ **Auto-updates every 24 hours** from eCFR  
✅ **Interactive API documentation** at `/docs`  
✅ **Health monitoring** at `/status`  
✅ **Fast JSON responses** with caching  
✅ **Professional REST API** with error handling  

## 🔧 Example Usage

```bash
# Get all agencies
curl https://your-app.railway.app/agencies

# Get EPA specifically  
curl https://your-app.railway.app/agencies/Environmental%20Protection%20Agency

# Check API status
curl https://your-app.railway.app/status
```

## 🆘 Need Help?

- **GitHub Issues**: Create issues in your repository
- **Deployment Docs**: See [DEPLOYMENT.md](DEPLOYMENT.md)
- **API Docs**: Visit `/docs` on your deployed API

---

**🎉 Your eCFR Regulations API is ready for the world!**
