import requests

def fetch_items_from_api(url):
    try:
        # Make the HTTP GET request to the API endpoint
        response = requests.get(url)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the JSON response and extract the 'items'
        items = response.json().get('items', [])
        
        return items
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []

# Example usage
url = 'https://api.example.com/data'
items = fetch_items_from_api(url)

if items:
    print("Items fetched successfully:")
    for item in items:
        print(item)
else:
    print("No items found or an error occurred.")
