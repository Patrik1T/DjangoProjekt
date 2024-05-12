from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    # cesta pro zobrazení úvodní stránky
    path('', views.index, name='index'),

    # Přesměrování z hlavní cesty na cestu 'movies/'
    path('', RedirectView.as_view(url='/movies/')),
]