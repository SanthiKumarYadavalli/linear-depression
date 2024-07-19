from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name='register_or_get_details'),
    path('complaint/', views.ComplaintCreate.as_view(),
         name='new_or_all_complaints'),
    path('complaint/<int:pk>', views.ComplaintDetails.as_view(),
         name='complaint_details'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
