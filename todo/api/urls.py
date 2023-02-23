from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('list/', ToDoAPI.as_view()),
    path('createlist/', ToDoAPI.as_view()),
    path('updatelist/<pk>', ToDoAPI.as_view()),
    path('partialupdatelist/<pk>', ToDoAPI.as_view()),
    path('deletelist/<pk>', ToDoAPI.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]