from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
                  path('', PartyListView.as_view(), name='party_page'),
                  path(r'party_<int:id_party>/', details_party, name='details_party'),
                  # path(r'party_<int:id_party>/tickets_<int:id_tickets>/', ticketsInfo, name='ticketsInfo'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
