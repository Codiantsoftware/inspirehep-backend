from elasticsearch import Elasticsearch, helpers
from urllib.parse import urlencode
import json
import os

from dotenv import load_dotenv
load_dotenv()


ELASTIC_BASE_URL = os.getenv("ELASTIC_BASE_URL")

es = Elasticsearch(
    ELASTIC_BASE_URL,
    verify_certs=False,
    http_auth=(os.getenv("ELASTIC_USERNAME"), os.getenv("ELASTIC_PASSWORD")),
)


def create_index_if_not_exists(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Created index: {index_name}")
    else:
        print(f"Index {index_name} already exists")


def prepare_records_for_bulk(data, category):
    """Prepare the records for Elasticsearch bulk insertion"""
    actions = []
    for record in data["hits"]["hits"]:

        index_name = f"inspire_hep_{category}"

        create_index_if_not_exists(index_name)
        print(record)
        import pdb

        action = {
            "_index": index_name,
            "_id": record.get("id"),
            "_source": record,
        }
        actions.append(action)
    return bulk_insert_to_elasticsearch(actions)


def bulk_insert_to_elasticsearch(records):
    """Bulk insert data into Elasticsearch"""
    try:
        helpers.bulk(es, records)
        return {"success": "Bulk insert successful!"}
    except Exception as e:
        return {"error": e}


def query_by_category(category):
    """Query documents based on category (dynamic index name)"""
    index_name = f"inspire_hep_{category}"
    response = es.search(index=index_name, body={"query": {"match_all": {}}})
    return response


def single_record_by_id(id, category):
    """Get a single record by id"""
    index_name = f"inspire_hep_{category}"
    response = es.get(index=index_name, id=id)
    return response


def build_query_string(params):
    return urlencode(params)


def search(index_name, query_params, sort=None, size=10):
    index_name = f"inspire_hep_{index_name}"
    query_string = build_query_string(query_params)

    body = {
        "query": {"query_string": {"query": query_string}},
        "size": size,
    }

    if sort:
        order_by = 'desc' if sort not in ('mostrecent', 'dateasc', 'dateasc') else 'asc'
        body["sort"] = [{'created': {"order": order_by}}]

    response = es.search(index=index_name, body=body)

    return response["hits"]["hits"]
