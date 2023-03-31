"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from MusicClub.views import( index, RootList, RootMineList, RootDetail, RootUpdate, RootDelete,
                            RootCreate, Login, Logout, SignUp, ProfileCreate, ProfileUpdate,
                            MensajeCreate, MensajeDelete, MensajeList, RootSearch, about
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', index, name="index"),
    path ('root/list', RootList.as_view(), name="root-list"),
    path ('root/list/mine', RootMineList.as_view(), name="root-mine"),
    path ('root/<pk>/detail', RootDetail.as_view(), name="root-detail"),
    path ('root/<pk>/update', RootUpdate.as_view(), name="root-update"),
    path ('root/<pk>/delete', RootDelete.as_view(), name="root-delete"),
    path ('root/create', RootCreate.as_view(), name="root-create"),
    path ('login/', Login.as_view(), name="login"),
    path ('logout/', Logout.as_view(), name="logout"),
    path ('signup/', SignUp.as_view(), name="signup"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('root/search', RootSearch.as_view(), name="root-search"),
    path('about/', about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
