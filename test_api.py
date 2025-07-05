import requests
import json
import sys
import threading
import time
from main import app
import uvicorn

def test_endpoints():
    """Test all API endpoints"""
    base_url = "http://localhost:8000"
    
    # Wait for server to start
    time.sleep(2)
    
    print("🧪 Testing Bank Account Agent API")
    print("=" * 50)
    
    # Test cases
    endpoints = [
        {"path": "/", "name": "Health Check"},
        {"path": "/account/balance", "name": "Account Balance"},
        {"path": "/account/info", "name": "Account Info"},
        {"path": "/account/transactions", "name": "Account Transactions"}
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint['path']}")
            
            print(f"\n📍 {endpoint['name']} - {endpoint['path']}")
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ SUCCESS")
                print(f"   Response: {json.dumps(data, indent=4)}")
                results.append({"endpoint": endpoint['name'], "status": "PASS", "data": data})
            else:
                print(f"   ❌ FAILED - Status: {response.status_code}")
                results.append({"endpoint": endpoint['name'], "status": "FAIL", "error": response.status_code})
                
        except requests.exceptions.ConnectionError:
            print(f"\n📍 {endpoint['name']} - {endpoint['path']}")
            print(f"   ❌ CONNECTION ERROR - Server not running")
            results.append({"endpoint": endpoint['name'], "status": "CONNECTION_ERROR"})
        except Exception as e:
            print(f"\n📍 {endpoint['name']} - {endpoint['path']}")
            print(f"   ❌ ERROR: {str(e)}")
            results.append({"endpoint": endpoint['name'], "status": "ERROR", "error": str(e)})
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed
    
    print(f"✅ Passed: {passed}/{len(results)}")
    print(f"❌ Failed: {failed}/{len(results)}")
    
    if failed == 0:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed.")
    
    return results

if __name__ == "__main__":
    # Start server in background thread
    def run_server():
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Run tests
    test_endpoints()
