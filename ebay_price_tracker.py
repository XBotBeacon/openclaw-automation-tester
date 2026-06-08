# ebay_price_tracker.py

# This script utilizes the eBay Finding API to search for sold items and get their prices.
# To use this script, you need to obtain an API key from eBay.
# 
# Step to Get eBay API Key:
# 1. Visit the eBay Developer Program website: https://developer.ebay.com/.
# 2. Sign up or log in to your eBay Developer account.
# 3. Navigate to the Application Keys section.
# 4. Create a new application to receive your API key.
# 5. Take note of your App ID (also known as Client ID).

import requests  # Importing the requests library to make API requests

# Set your API key here
API_KEY = 'YOUR_API_KEY'  # Replace with your eBay API key

def search_sold_items(query):
    url = 'https://svcs.ebay.com/services/search/FindingService/v1'
    params = {
        'METHOD': 'findItemsAdvanced',
        'SECURITY-APPNAME': API_KEY,
        'RESPONSE-DATA-FORMAT': 'JSON',
        'keywords': query,
        'itemFilter(0).name': 'SoldItemsOnly',
        'itemFilter(0).value': 'true',
        'paginationInput.entriesPerPage': 10
    }

    response = requests.get(url, params=params)

    # Check for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

if __name__ == '__main__':
    query = 'Pokemon Charizard 1999 Base Set'
    sold_items = search_sold_items(query)
    if sold_items:
        print(sold_items)  # Display the sold items details
