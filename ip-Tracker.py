import requests

def track_ip(ip_address):
    # API endpoint with all fields
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,mobile,proxy,hosting,query"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "success":
            print("\n=== IP Tracker Results ===")
            print(f"IP Address: {data.get('query', 'N/A')}")
            print(f"Continent: {data.get('continent', 'N/A')} ({data.get('continentCode', 'N/A')})")
            print(f"Country: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"Region: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"District: {data.get('district', 'N/A')}")
            print(f"ZIP Code: {data.get('zip', 'N/A')}")
            print(f"Latitude: {data.get('lat', 'N/A')}")
            print(f"Longitude: {data.get('lon', 'N/A')}")
            print(f"Timezone: {data.get('timezone', 'N/A')}")
            print(f"Currency: {data.get('currency', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
            print(f"AS Number: {data.get('as', 'N/A')}")
            print(f"AS Name: {data.get('asname', 'N/A')}")
            print(f"Mobile Network: {data.get('mobile', 'N/A')}")
            print(f"Proxy/VPN: {data.get('proxy', 'N/A')}")
            print(f"Hosting Provider: {data.get('hosting', 'N/A')}")
            # Google Maps link for visual location
            if 'lat' in data and 'lon' in data:
                maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
                print(f"View on Google Maps: {maps_url}")
            print("\nNote: This is an approximate location (city-level) based on IP.")
        else:
            print(f"Error: {data.get('message', 'Invalid IP or API issue')}")
    
    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet.")
    except requests.exceptions.Timeout:
        print("Timeout Error: API took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def main():
    print("=== Welcome to Advanced Python IP Tracker ===")
    print("Note: Exact addresses cannot be tracked with IP alone.")
    while True:
        ip = input("\nEnter IP address (Enter for your IP, 'q' to quit): ").strip()
        
        if ip.lower() == 'q':
            print("Exiting... Thanks for using!")
            break
        elif not ip:
            print("Tracking your own IP...")
            track_ip("")
        else:
            print(f"Tracking IP: {ip}")
            track_ip(ip)

if __name__ == "__main__":
    main()