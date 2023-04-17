
from django.urls import path
from accounts.views import create_user, login_view, logout_view

urlpatterns = [
    # the first item in path does NOT need to be the name of an HTML file
    path('signup/', create_user, name='create_user'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view')
]
