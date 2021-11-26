from django.shortcuts import render

from django.views.generic.list import ListView

from .models import *


class PartyListView(ListView):
    model = Party
    context_object_name = 'party_List'
    paginate_by = 5  # if pagination is desired
    template_name = 'Party/party_page.html'
    ordering = ['id']


def details_party(request, id_party):
    context = {}

    party = Party.objects.get(id=id_party)
    context['party'] = party
    # context['sessions'] = Session.objects.filter(ID_Films=movies_id)
    # context['cinemas'] = Cinemas.objects.all()
    # for p in movies:
    #     genre = p.genre_film
    # context['genreFilm'] = Films.objects.filter(Q(genre_film=genre), ~Q(id=movies_id))


    return render(request, 'Party/about_party.html', context=context)
