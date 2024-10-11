Inspire Data API Project

Overview
This project provides a set of APIs to fetch data from the InspireHEP database. It allows users to retrieve documents by different identifier types, and access single records based on their IDs. The APIs are built using Django REST Framework and follow standard practices for RESTful APIs.

Installation
Prerequisites
Python 3.10


Setup
Clone the repository:

git clone <repo>
cd inspire-data-api

Create virual envirionment
python -m venv venv
Activate virual envirionment
source venv/bin/activate


Install the required packages:

pip install -r requirements.txt

Rename .temp_env to .env

Run the server:

python manage.py runserver



API Endpoints
1. Fetch Inspire Data
Endpoint: /api/insert-data/<identifier_type>/

Method: GET

Parameters:

identifier_type (string): The type of identifier to fetch data for (e.g., literature, jobs, conferences, seminars).
Response:

200 OK: Insert the fetched data.
400 Bad Request: Returns an error message if an error occurs.

Success Response
{
    "success": "Bulk insert successful!"
}



2. Search Category Documents
Endpoint: /api/documents/<<identifier_type>>/

Method: GET

Parameters:

identifier_type (string): The Identifier to search within (e.g., literature, jobs, conferences, seminars).
q (optional, string): The query string for searching documents.
sort (optional, string): The sorting criteria for the results.
size (optional, integer): The number of results to return (default is 10).
Response:

200 OK: Returns the search results.
400 Bad Request: Returns an error message if an error occurs.
Example Request:

GET /api/documents/literature/?q=abstracts.source:Springer&sort=asc&size=5

Response type:

[
    {
        "_index": "inspire_hep_literature",
        "_id": "1482166",
        "_score": null,
        "_ignored": [
            "metadata.abstracts.value.keyword",
            "metadata.references.reference.misc.keyword"
        ],
        "_source": {

        }
    }
]


3. Retrieve Single Record by ID
Endpoint: /api/identifier-by-id/<identifier_type>/<id>/

Method: GET

Parameters:

identifier_type (string): The Identifier to search within (e.g., literature, jobs, conferences, seminars)..
id (string): The ID of particular Identifier.
Response:

200 OK: Returns the details of the single record.
400 Bad Request: Returns an error message if an error occurs.
Example Request:

GET /api/identifier-by-id/literature/123456


{
    "_index": "inspire_hep_literature",
    "_id": "1811940",
    "_version": 3,
    "_seq_no": 20,
    "_primary_term": 1,
    "found": true,
    "_source": {
    }
}

Error Handling
In case of errors, the API will return a JSON object with an "error" key containing the error message and an appropriate HTTP status code.

