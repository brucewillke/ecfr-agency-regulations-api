# Deployment Guide

This guide covers multiple deployment options for the eCFR Agency Regulations API.

## 🚀 Quick Deploy Options

### 1. Railway (Recommended - Free Tier)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. **Create Railway Account**: Visit [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy from GitHub**: 
   - Click "Deploy from GitHub repo"
   - Select this repository
   - Railway will auto-detect the Python app and deploy

**Configuration:**
- Port: Automatically configured via `PORT` environment variable
- Build: Uses `railway.json` configuration
- Health Check: `/status` endpoint

### 2. Render (Free Tier)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. **Create Render Account**: Visit [render.com](https://render.com)
2. **New Web Service**: 
   - Connect GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Port: `8000`

### 3. Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. **Create Heroku Account**: Visit [heroku.com](https://heroku.com)
2. **Install Heroku CLI**
3. **Deploy Commands**:
   ```bash
   heroku create your-ecfr-api
   git push heroku main
   heroku ps:scale web=1
   ```

### 4. Vercel (Serverless)

1. **Install Vercel CLI**: `npm i -g vercel`
2. **Deploy**: `vercel --prod`
3. **Note**: May require modifications for serverless environment

## 🐳 Docker Deployment

### Local Docker
```bash
# Build image
docker build -t ecfr-api .

# Run container
docker run -p 8000:8000 ecfr-api
```

### Docker Hub
```bash
# Tag and push
docker tag ecfr-api your-username/ecfr-api
docker push your-username/ecfr-api
```

## ☁️ Cloud Platform Deployment

### AWS (Elastic Beanstalk)
1. Install AWS CLI and EB CLI
2. Initialize: `eb init`
3. Create environment: `eb create`
4. Deploy: `eb deploy`

### Google Cloud Platform (Cloud Run)
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT-ID/ecfr-api
gcloud run deploy --image gcr.io/PROJECT-ID/ecfr-api --platform managed
```

### Azure (Container Instances)
```bash
# Create resource group
az group create --name ecfr-api-group --location eastus

# Deploy container
az container create --resource-group ecfr-api-group \
  --name ecfr-api --image your-username/ecfr-api \
  --dns-name-label ecfr-api --ports 8000
```

## 📊 Monitoring & Management

### Environment Variables
- `PORT`: Server port (default: 8000)
- `LOG_LEVEL`: Logging level (default: INFO)

### Health Checks
- **Endpoint**: `/status`
- **Expected Response**: HTTP 200 with JSON status

### Scaling Considerations
- API is stateless (uses in-memory cache)
- Background scheduler runs on single instance
- For high availability, consider external cache (Redis)

## 🔧 Production Optimizations

### Performance
- Add Redis for distributed caching
- Implement request rate limiting
- Add response compression
- Use CDN for static assets

### Security
- Add HTTPS/TLS termination
- Implement API key authentication
- Add CORS configuration
- Input validation and sanitization

### Monitoring
- Add application monitoring (New Relic, DataDog)
- Log aggregation (ELK stack)
- Error tracking (Sentry)
- Uptime monitoring

## 📝 Post-Deployment

1. **Test the API**: Visit `https://your-app.platform.com/docs`
2. **Monitor Status**: Check `/status` endpoint
3. **Verify Updates**: Background updates every 24 hours
4. **Scale as Needed**: Monitor performance and scale horizontally

## 🆘 Troubleshooting

### Common Issues
- **Port Binding**: Ensure `PORT` environment variable is set
- **Memory Limits**: Increase if processing large datasets
- **Timeout Issues**: Adjust health check timeouts for slow eCFR API responses
- **CORS Errors**: Add appropriate CORS headers for frontend access

### Logs
Check application logs for:
- eCFR API connection issues
- Memory usage patterns
- Background job execution
- Error rates and patterns
