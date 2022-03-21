from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.cour,name='cour'),
    path('exercice/',views.exercice,name='exercice'),
    path('correction-des-exercices/',views.correction,name='correction'),
	path('accounts/login/', views.loginPage, name="login"),  
	path('accounts/logout/', views.logoutUser, name="logout"),
	path('live/', views.classe, name="classe"),
	path('endlive/', views.live, name="live"),
	path('videos/', views.error, name="error"),
	path('view/<str:pk>', views.view, name="view"),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
