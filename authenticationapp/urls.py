from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'authenticationapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/profile/', views.index, name='index'),
]
# from django.contrib import admin
# from django.conf.urls import include
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('oauth/', include('social_django.urls', namespace='social')),
#     path('accounts/profile/', views.index, name='index')
# ]
