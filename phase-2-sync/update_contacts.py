import requests
import time
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
ACCESS_TOKEN = os.getenv("HUBSPOT_DEAL_UPDATER_TOKEN")


# 🔧 Pipeline and stage IDs
PIPELINE_ID = "default"
DEAL_STAGE_ID = "closedwon"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

HUBSPOT_API = "https://api.hubapi.com"


# Step 1: Get all contacts whose "Membership Notes" contain "bought"
def get_buyer_contacts():
    all_contacts = []
    after = None

    while True:
        url = f"{HUBSPOT_API}/crm/v3/objects/contacts/search"
        query = {
            "filterGroups": [
                {
                    "filters": [
                        {
                            "propertyName": "hs_content_membership_notes",
                            "operator": "CONTAINS_TOKEN",
                            "value": "bought",
                        }
                    ]
                }
            ],
            "properties": [
                "email",
                "firstname",
                "lastname",
                "hs_content_membership_notes",
            ],
            "limit": 100,
        }

        if after:
            query["after"] = after

        response = requests.post(url, headers=HEADERS, json=query)
        response.raise_for_status()
        data = response.json()

        contacts = data.get("results", [])
        all_contacts.extend(contacts)

        paging = data.get("paging")
        if paging and "next" in paging:
            after = paging["next"]["after"]
        else:
            break

    return all_contacts


# Step 2: Create deal for a contact
def create_deal(contact):
    contact_id = contact["id"]
    email = contact["properties"].get("email", "")
    first_name = contact["properties"].get("firstname", "Unknown")

    deal_payload = {
        "properties": {
            "dealname": f"{first_name} Glasses Purchase",
            "pipeline": PIPELINE_ID,
            "dealstage": DEAL_STAGE_ID,
        },
        "associations": [
            {
                "to": {"id": contact_id},
                "types": [
                    {
                        "associationCategory": "HUBSPOT_DEFINED",
                        "associationTypeId": 3,  # Contact-to-deal
                    }
                ],
            }
        ],
    }

    url = f"{HUBSPOT_API}/crm/v3/objects/deals"
    response = requests.post(url, headers=HEADERS, json=deal_payload)
    response.raise_for_status()
    print(f"✅ Deal created for {email} ({first_name})")
    time.sleep(0.3)  # Avoid API rate limits


# === Main Execution ===
if __name__ == "__main__":
    print("🔎 Searching for contacts with 'bought' in membership notes...")
    contacts = get_buyer_contacts()
    print(f"📋 Found {len(contacts)} matching contacts.")

    for contact in contacts:
        try:
            create_deal(contact)
        except Exception as e:
            print(f"⚠️ Error for contact {contact['id']}: {e}")
