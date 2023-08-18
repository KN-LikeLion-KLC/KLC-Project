from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
 
urlpatterns = [
    path('', views.redirect_main),
    path('main', views.main),
    path('app-guide', views.appGuide),
    path('kiosk-guide', views.kioskGuide),
    path('email-guide', views.emailGuide),
    path('mobile-notification-guide', views.mobilenotificationGuide),
    path('quiz', views.quiz),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)