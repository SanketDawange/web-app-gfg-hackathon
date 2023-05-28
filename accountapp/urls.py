from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Patient side
    
    path('user_login', views.user_login, name='user_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)