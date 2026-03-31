from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp import views as myapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('register/', include('registration.urls')),
    path('blog/', include('blog.urls')),
    path('signup/', myapp_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='myapp:home'), name='logout'),
    path('api/', include('api.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
