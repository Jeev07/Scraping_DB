from django.contrib import admin
from django.urls import path,include
from .admin import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('',include('Import_excel_db.urls')),
]