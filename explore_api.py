#!/usr/bin/env python3
"""
Explore eCFR API structure to understand the correct endpoints
"""
import asyncio
import httpx
import json

async def explore_ecfr_api():
    """Explore the eCFR API structure"""
    base_url = "https://www.ecfr.gov/api/versioner/v1"
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            # Get titles
            print("🔍 Fetching titles...")
            response = await client.get(f"{base_url}/titles.json")
            response.raise_for_status()
            titles_data = response.json()
            
            print(f"📚 Found {len(titles_data.get('titles', []))} titles")
            
            # Show structure of first few titles
            titles = titles_data.get('titles', [])[:3]
            for title in titles:
                print(f"\n📖 Title {title.get('number')}: {title.get('name')}")
                print(f"   Structure: {json.dumps(title, indent=2)}")
                
            # Try different API endpoints to find the correct structure
            if titles:
                first_title = titles[0]
                title_num = first_title.get('number')
                
                # Try various endpoint patterns
                endpoints_to_try = [
                    f"/title/{title_num}",
                    f"/title/{title_num}.json",
                    f"/titles/{title_num}",
                    f"/titles/{title_num}.json",
                    f"/title-{title_num}",
                    f"/title-{title_num}.json"
                ]
                
                print(f"\n🔎 Testing endpoints for Title {title_num}...")
                for endpoint in endpoints_to_try:
                    try:
                        url = f"{base_url}{endpoint}"
                        response = await client.get(url)
                        if response.status_code == 200:
                            print(f"✅ Working endpoint: {url}")
                            data = response.json()
                            print(f"   Data keys: {list(data.keys())}")
                        else:
                            print(f"❌ {endpoint} -> {response.status_code}")
                    except Exception as e:
                        print(f"❌ {endpoint} -> Error: {e}")
                        
        except Exception as e:
            print(f"❌ Error exploring API: {e}")

if __name__ == "__main__":
    asyncio.run(explore_ecfr_api())
