# eCFR Agency Regulations Size API

A FastAPI-based JSON API that analyzes federal agency regulations from the eCFR (electronic Code of Federal Regulations) and returns each agency's regulation data size in megabytes.

## Features

- 📊 Real-time analysis of federal agency regulation sizes
- 🔄 Automatic updates every 24 hours without code modifications
- 🚀 Fast JSON API responses with caching
- 📈 Regulation size calculation in megabytes
- 🏛️ Comprehensive federal agency coverage

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /agencies` - Get all agencies with regulation sizes
- `GET /agencies/{agency_name}` - Get specific agency regulation size
- `GET /status` - API status and last update information
- `POST /refresh` - Manually trigger data refresh

## Quick Deployment

### 🚀 One-Click Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### 🐳 Docker Deployment

```bash
docker build -t ecfr-api .
docker run -p 8000:8000 ecfr-api
```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## Local Development

### Prerequisites

- Python 3.8+
- Internet connection for eCFR API access

### Installation

1. Clone or download the project
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

```bash
# Option 1: Use the startup script
./start.sh

# Option 2: Manual activation
source venv/bin/activate
python main.py

# Option 3: Direct execution
./venv/bin/python main.py
```

The API will be available at `http://localhost:8000`

**Interactive API Documentation:** `http://localhost:8000/docs`

### Example API Response

```json
{
  "agencies": {
    "Department of Agriculture": 45.23,
    "Environmental Protection Agency": 78.91,
    "Department of Transportation": 52.67,
    "Food and Drug Administration": 34.12
  },
  "total_agencies": 4,
  "last_updated": "2025-07-31T10:30:00",
  "data_size_unit": "megabytes"
}
```

## How It Works

1. **Data Collection**: Fetches CFR titles and parts from the official eCFR API
2. **Size Calculation**: Converts JSON content to bytes and calculates megabyte sizes
3. **Agency Mapping**: Maps CFR titles to their corresponding federal agencies
4. **Automatic Updates**: Background scheduler updates data every 24 hours
5. **Caching**: Stores results in memory for fast API responses

## eCFR API Integration

This application uses the official eCFR API:
- Base URL: `https://www.ecfr.gov/api/versioner/v1`
- Documentation: https://www.ecfr.gov/developers/documentation/api/v1

## Development

### Project Structure

```
├── main.py                          # Main FastAPI application
├── requirements.txt                 # Python dependencies
├── README.md                       # This file
└── .github/
    └── copilot-instructions.md     # Copilot workspace instructions
```

### Key Components

- **eCFRAnalyzer**: Core class for fetching and analyzing eCFR data
- **Background Scheduler**: Automatic data updates every 24 hours
- **Caching System**: In-memory storage for fast API responses
- **Agency Mapping**: CFR title to federal agency correlation

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation powered by FastAPI's automatic OpenAPI generation.

## License

This project analyzes publicly available federal regulations data from eCFR.
