import requests
from .elastic import prepare_records_for_bulk


def fetch_inspire_data(identifier_type):
    valid_identifiers = [
        "literature",
        "authors",
        "institutions",
        "conferences",
        "seminars",
        "journals",
        "jobs",
        "experiments",
        "data",
    ]

    if identifier_type not in valid_identifiers:
        return {"error": "Invalid identifier type"}

    url = f"https://inspirehep.net/api/{identifier_type}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return prepare_records_for_bulk(response.json(), identifier_type)
    except requests.RequestException as e:
        return {"error": str(e)}


