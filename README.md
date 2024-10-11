# 🎇 Inspire Data API Project

This project provides a set of RESTful APIs to fetch data from the [InspireHEP](https://inspirehep.net/) database. These APIs allow users to retrieve documents by various identifier types (e.g., literature, jobs, conferences) and fetch single records based on their unique IDs. The APIs are built using **Django REST Framework** and adhere to standard best practices for RESTful API development.

## 🚀 Features

- Retrieve InspireHEP documents by identifier types (e.g., literature, jobs, conferences, seminars).
- Search within specific categories with custom query parameters.
- Fetch a single record based on its unique ID.

---

## 🛠️ Installation

### Prerequisites

- **Python 3.11**
- **ElasticSearch**

### Setup

1. Clone the repository:

   ```bash
   git clone <repo>
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Rename `.temp_env` to `.env` and configure environment variables as needed.

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## 📖 API Endpoints

### 1. Insert Inspire Data To ElasticSearch

- **Endpoint:** `/api/insert-data/<identifier_type>/`
- **Method:** `GET`
- **Parameters:**
  - `identifier_type` (string): The type of identifier to fetch data for (e.g., literature, jobs, conferences, seminars).
- **Response:**
  - `200 OK`: Successfully inserted the fetched data.
  - `400 Bad Request`: Error with an appropriate message.

**Success Response:**

```json
{
  "success": "Bulk insert successful!"
}
```

---

### 2. Search Category Documents

- **Endpoint:** `/api/documents/<identifier_type>/`
- **Method:** `GET`
- **Parameters:**
  - `identifier_type` (string): The identifier to search within (e.g., literature, jobs, conferences, seminars).
  - `q` (optional, string): The query string for searching documents.
  - `sort` (optional, string): The sorting criteria for the results.
  - `size` (optional, integer): Number of results to return (default is 10).
- **Response:**
  - `200 OK`: Returns the search results.
  - `400 Bad Request`: Error message in case of failure.

**Example Request:**

```bash
GET /api/documents/literature/?q=abstracts.source:Springer&sort=asc&size=5
```

**Response Example:**

```json
[
  {
    "_index": "inspire_hep_literature",
    "_id": "1482166",
    "_source": {}
  }
]
```

---

### 3. Retrieve Single Record by ID

- **Endpoint:** `/api/identifier-by-id/<identifier_type>/<id>/`
- **Method:** `GET`
- **Parameters:**
  - `identifier_type` (string): The identifier category (e.g., literature, jobs, conferences, seminars).
  - `id` (string): The unique ID of the record to retrieve.
- **Response:**
  - `200 OK`: Returns the details of the single record.
  - `400 Bad Request`: Error message if the record is not found.

**Example Request:**

```bash
GET /api/identifier-by-id/literature/123456
```

**Success Response:**

```json
{
  "_index": "inspire_hep_literature",
  "_id": "1811940",
  "found": true,
  "_source": {}
}
```

---

## ⚠️ Error Handling

In case of errors, the API will return a JSON object with an `error` key containing the error message, along with the appropriate HTTP status code. Here's an example:

```json
{
  "error": "Invalid identifier type",
  "status_code": 400
}
```

---
