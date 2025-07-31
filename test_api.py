#!/usr/bin/env python3
"""
Test script for the eCFR Agency Regulations API
"""
import asyncio
import httpx
import json
from main import eCFRAnalyzer

async def test_ecfr_analyzer():
    """Test the eCFRAnalyzer functionality"""
    print("🧪 Testing eCFR Analyzer...")
    
    analyzer = eCFRAnalyzer()
    
    try:
        # Test getting titles
        print("📚 Fetching CFR titles...")
        titles = await analyzer.get_all_titles()
        print(f"✅ Found {len(titles)} titles")
        
        if titles:
            # Test analyzing first few titles
            print("🔍 Testing regulation size analysis...")
            
            # Get a sample title
            sample_title = titles[0] if titles else None
            if sample_title:
                title_number = sample_title.get('number')
                print(f"📖 Analyzing Title {title_number}: {sample_title.get('name')}")
                
                # Get title parts
                parts = await analyzer.get_title_parts(title_number)
                if parts:
                    size = analyzer.calculate_content_size(parts)
                    print(f"📊 Title {title_number} parts size: {size} MB")
                
        print("✅ eCFR Analyzer test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
    
    finally:
        await analyzer.close()

async def test_api_endpoints():
    """Test API endpoints locally"""
    print("\n🌐 Testing API endpoints...")
    
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        try:
            # Test root endpoint
            response = await client.get(f"{base_url}/")
            print(f"✅ Root endpoint: {response.status_code}")
            
            # Test status endpoint
            response = await client.get(f"{base_url}/status")
            print(f"✅ Status endpoint: {response.status_code}")
            print(f"📊 Status: {response.json()}")
            
        except httpx.ConnectError:
            print("⚠️  API server not running. Start with: python main.py")
        except Exception as e:
            print(f"❌ API test error: {e}")

if __name__ == "__main__":
    print("🚀 eCFR API Test Suite")
    print("=" * 40)
    
    # Test the analyzer functionality
    asyncio.run(test_ecfr_analyzer())
    
    # Test API endpoints (if server is running)
    asyncio.run(test_api_endpoints())
    
    print("\n" + "=" * 40)
    print("🎯 Test suite completed!")
    print("\n📋 To start the API server:")
    print("   python main.py")
    print("\n🌐 API will be available at:")
    print("   http://localhost:8000")
    print("   http://localhost:8000/docs (Interactive API docs)")
