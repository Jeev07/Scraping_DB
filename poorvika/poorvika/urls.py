"""poorvika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from excel_to_db import views  
# from Import_Excel import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Import_excel,name="Import_excel"),
    # path("",views.Import_excel_TV,name="Import_excel_TV"),
    
# path('admin',admin.site.urls),

    # path('Import_Excel_pandas/', views.Import_excel,name="Import_excel"),
    # path('Import_Excel_pandas/', views.Import_excel_TV,name="Import_excel_TV"), 
]
# from django.urls import path
# from excel_app import views  
# # from Import_Excel import settings
# from django.conf.urls.static import static
# # from excel_app import *

# urlpatterns =[
