from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.cour,name='cour'),
    path('exercice/',views.exercice,name='exercice'),
    path('correction/',views.correction,name='correction'),
	path('accounts/login/', views.loginPage, name="login"),  
	path('accounts/logout/', views.logoutUser, name="logout"),
	path('classe/', views.classe, name="classe"),
	path('endlive/', views.live, name="live"),
	path('error/', views.error, name="error"),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
