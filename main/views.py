from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_inspire_data
from .elastic import query_by_category, single_record_by_id, search  # InspireHEPService


class InspireDataFetchView(APIView):
    def get(self, request, identifier_type):
        """
        Fetch all records of a given identifier type from Inspire.

        Args:
        request: The request object
        identifier_type: The identifier type to fetch records for. One of 'literature',
            'jobs', 'conferences', 'seminars'.

        Returns:
        A Response object with success message, or an error message if
        the request was invalid.
        """
        data = fetch_inspire_data(identifier_type)
        if "error" in data:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class IdentifierRecordsView(APIView):
    def get(self, request, identifier_type):
        """
        Retrieve records of a given identifier type from Elasticsearch.

        Args:
        request: The request object
        identifier_type: The identifier type to retrieve records for. One of 'literature',
            'jobs', 'conferences', 'seminars'.

        Returns:
        A Response object with the retrieved records, or an error message if
        the request was invalid.

        Query parameters:
        q: The query string to search for.
        sort: The sorting order. One of 'mostrecent', 'dateasc', 'dateasc'.
        size: The number of records to return. Defaults to 10.
        """
        query = request.query_params.get("q")
        if query:
            sort = request.query_params.get("sort")
            size = request.query_params.get("size",25)
            query_params = {
            "q": query,
            }
            
        try:
            results = search(identifier_type, query_params, sort=sort, size=size) if query else query_by_category(identifier_type)
            sort_options = [{"value": "mostrecent","display": "Most Recent"},{"value": "leastrecent","display": "Least Recent"},{"value": "mostcited","display": "Most Cited"}]
            response_data = {'data':results, "sort_option" : sort_options}
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        

class SingleIdentifierRecordView(APIView):
    def get(self, request, identifier_type, id):
        
        """
        Retrieve a single record by its identifier from Elasticsearch.

        Args:
        request: The request object
        identifier_type: The identifier type of the record to retrieve. One of 'literature',
            'jobs', 'conferences', 'seminars'.
        id: The identifier of the record to retrieve.

        Returns:
        A Response object with the retrieved record, or an error message if
        the request was invalid.
        """
        try:
            results = single_record_by_id(id, identifier_type)
                
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class SearchView(APIView):
#     def get(self, request, index):
#         query = request.query_params.get("q")
#         sort = request.query_params.get("sort")
#         size = request.query_params.get("size",10)
        
#         print(query)
#         print(index)
#         print(query)
#         if not index or not query:
#             return Response(
#                 {"error": "Index and query parameters are required."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         query_params = {
#             "q": query,
#         }

#         try:
#             results = search(index, query_params, sort=sort, size=size)
#             return Response(results, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(
#                 {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )https://inspirehep.net/api/authors/2451898
