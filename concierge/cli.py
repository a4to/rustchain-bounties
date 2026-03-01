import os
import json
import requests
import argparse

# Load environment variables
SAASCITY_KEY = os.getenv('SAASCITY_KEY')

def saascity_upvote(dry_run=False):
    """
    Upvote SaaSCity listings using the SaaSCity API.

    Args:
        dry_run (bool): If True, only show what would be upvoted without making API calls.

    Returns:
        A list of upvoted listing IDs or a message indicating what would be upvoted in dry-run mode.
    """
    if not SAASCITY_KEY:
        raise ValueError("SAASCITY_KEY environment variable is not set")

    # Set API endpoint and authentication headers
    api_endpoint = "https://api.saascity.com/v1/listings/upvote"
    headers = {"Authorization": f"Bearer {SAASCITY_KEY}"}

    # Prepare the payload with RustChain/BoTTube listings
    payload = {"listings": ["RustChain", "BoTTube"]}

    if dry_run:
        print("Dry-run mode: Would upvote the following listings:")
        print(json.dumps(payload, indent=4))
        return "Dry-run mode: No upvotes made"

    try:
        # Make the API call to upvote the listings
        response = requests.post(api_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        upvoted_listings = response.json()["upvoted_listings"]
        return upvoted_listings
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to upvote listings: {e}")

def main():
    parser = argparse.ArgumentParser(description="Concierge CLI")
    parser.add_argument("--saascity", action="store_true", help="Upvote SaaSCity listings")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be upvoted without making API calls")
    args = parser.parse_args()

    if args.saascity:
        try:
            upvoted_listings = saascity_upvote(args.dry_run)
            print(upvoted_listings)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()