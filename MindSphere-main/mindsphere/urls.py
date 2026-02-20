from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mindsphere.views import home

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Accounts (signup + dashboard)
    path('accounts/', include('accounts.urls')),

    # Core features
    path('checkin/', include('checkin.urls')),
    path('history/', include('checkin.urls')),
    path('chatbot/', include('chatbot.urls')),

    # Games
    path('dashboard/games/', include('games.urls')),
]
