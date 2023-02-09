from django.urls import path, include
from customerapp.views import homepage, dbview, records, add_cust

urlpatterns = [
    path('', homepage, name="homepage"),
    path('dbview/', dbview, name="dbview"),
    path('records/', records, name="records"),
    path('add/', add_cust, name="add"),
]