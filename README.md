The error was not showing because the error output for the API module had not been redirected and displayed. First, find the file, edit the code to display the output:
```python
import requests

class SaaSCityAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.saascity.com/v1'

    def upvote(self, listing_id):
        url = f'{self.base_url}/listings/{listing_id}/upvote'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)

def saascity_upvote(api_key, listing_id, dry_run=False):
    saascity = SaaSCityAPI(api_key)
    if dry_run:
        print(f"[Dry Run] Would upvote listing {listing_id}")
    else:
        try:
            result = saascity.upvote(listing_id)
            print(f"Successfully upvoted listing {listing_id}: {result}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to upvote listing {listing_id}: {e}")

# Example usage
if __name__ == "__main__":
    import os
    api_key = os.getenv('SAASCITY_KEY')
    if not api_key:
        print("Error: SAASCITY_KEY environment variable not set")
    else:
        saascity_upvote(api_key, 'some-listing-id', dry_run=True)
        saascity_upvote(api_key, 'some-listing-id')
```