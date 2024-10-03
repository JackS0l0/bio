from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from main import views as mainviews
from users import views as usersviews
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',usersviews.index,name='indexpage'),
    path('home/',mainviews.home,name='homepage'),
    path('book/<int:pk>/',mainviews.DetailBook.as_view(), name='bookpage'),
    path('exit/',usersviews.LogoutView.as_view(), name='logout'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)