import requests
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
ACCESS_TOKEN = os.getenv("HUBSPOT_DEAL_UPDATER_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


# HubSpot API endpoint to fetch pipelines
def get_pipelines():
    url = "https://api.hubapi.com/crm/v3/pipelines/deals"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    print("\n🎯 Available Pipelines and Stages:\n")
    for pipeline in data["results"]:
        print(f"Pipeline Name: {pipeline['label']}")
        print(f"Pipeline ID: {pipeline['id']}")
        for stage in pipeline["stages"]:
            print(f"  - Stage Name: {stage['label']}")
            print(f"    Stage ID:   {stage['id']}")
        print("-" * 40)


if __name__ == "__main__":
    get_pipelines()
