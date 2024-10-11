from django.urls import path
from .views import (
    InspireDataFetchView,
    IdentifierRecordsView,
    SingleIdentifierRecordView,
)

urlpatterns = [
    path(
        "insert-data/<str:identifier_type>/",
        InspireDataFetchView.as_view(),
        name="fetch_inspire_data",
    ),
    path(
        "documents/<str:identifier_type>/",
        IdentifierRecordsView.as_view(),
        name="identifier_records",
    ),
    path(
        "identifier-by-id/<str:identifier_type>/<str:id>/",
        SingleIdentifierRecordView.as_view(),
        name="single_identifier_record",
    ),
   
]

# path("search/<str:index>/", SearchView.as_view(), name="search"),