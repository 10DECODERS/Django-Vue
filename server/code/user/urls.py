from django.urls import path
from .views import (UserPost, UserView)

users_urlpatterns = (
    [
        path('', UserPost.as_view(), name="User-Detail"),
        path('<pk>', UserView.as_view(), name="User-list"),
    ], "users_urlpatterns"
)
