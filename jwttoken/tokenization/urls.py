from django.contrib import admin
from django.urls import path, include
from .views import * 
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('', home),
    # path('student/',post_student),
    # path('update-student/<id>', update_student),
    # path('delete-student/<id>',delete_student),
    #path('api-token-auth/', views.obtain_auth_token),
    # path('get-books/', get_book),
    path('register/', RegisterUser.as_view()),
    path('', StudentAPI.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generic_student/', StudentGeneric.as_view()),
    path('generic_student/<id>/', StudentGenericUpdate.as_view())
]   

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()