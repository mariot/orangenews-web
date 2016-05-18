from django.conf.urls import url, include

from . import views, feeds

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'actualite', views.ActualiteViewSet)
router.register(r'depeche', views.DepecheViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^depeches/', feeds.DernieresDepeches()),
    url(r'^actualites/', feeds.DerniersActualites()),
    url(r'^depeche/$', views.home, name='depeche')
]