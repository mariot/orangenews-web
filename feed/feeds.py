from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from . import views

from .models import Depeche, Actualite

class DernieresDepeches(Feed):
    title = "Les dernieres depeches"
    link = "/depeches/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Depeche.objects.order_by('-heure')[:25]

    def item_title(self, item):
        return item.titre

    def item_pubdate(self, item):
        return item.heure

    def item_description(self, item):
        return item.contenu

    def item_link(self, item):
        return reverse(views.home) + str(item.id)

class DerniersActualites(Feed):
    title = "Les derniers actualites"
    link = "/actualites/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Actualite.objects.order_by('-date')[:25]

    def item_title(self, item):
        return item.titre

    def item_pubdate(self, item):
        return item.date

    def item_description(self, item):
        return item.contenu

    def item_categories(self, item):
    	return item.categorie

    def item_link(self, item):
        return item.image.url