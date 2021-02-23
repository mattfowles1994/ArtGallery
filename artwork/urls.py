"""AG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from artwork.views import (
    artwork_detail_view, 
    artwork_create_view,
    dynamic_lookup_view,
    artwork_delete_view,
    artwork_list_view
)

app_name = 'artwork'

urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='artwork'),
    path('list/', artwork_list_view),
    path('create/', artwork_create_view),
    path('<int:id>/delete', artwork_delete_view, name='product-delete')
]