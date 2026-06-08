import requests
from bs4 import BeautifulSoup
import json

def check_supreme_drops():
    """Check Supreme new releases and return item list."""
    url = "https://us.supreme.com/collections/new"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = []
        # This is a placeholder - Supreme's site changes often
        # You would inspect the actual HTML and update selectors
        for product in soup.find_all('div', class_='product-item')[:5]:
            name = product.find('p', class_='product-name')
            price = product.find('p', class_='product-price')
            if name and price:
                items.append({
                    'name': name.text.strip(),
                    'price': price.text.strip()
                })
        
        return items
    except Exception as e:
        return f"Error checking Supreme: {e}"

if __name__ == "__main__":
    results = check_supreme_drops()
    print(json.dumps(results, indent=2))