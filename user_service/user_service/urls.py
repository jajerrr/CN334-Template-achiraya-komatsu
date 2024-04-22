from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from user_management.views import *

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/register', register),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/myinfo', CustomerView.as_view(), name="myinfo")
]