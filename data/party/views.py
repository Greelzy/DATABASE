from django.shortcuts import render

from django.views.generic.list import ListView

from .models import *


class PartyListView(ListView):
    model = Party
    context_object_name = 'party_List'
    paginate_by = 5  # if pagination is desired
    template_name = 'Party/party_page.html'
    ordering = ['id']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.method == 'GET':
            return qs
        pass

    def get_context_data(self, **kwargs):

        pass


def details_party(request, id_party):
    context = {}
    tickets = Tickets.objects.get(ID_Party=id_party)
    context['tickets'] = tickets
    return render(request, 'Party/about_party.html', context=context)


def ticketsInfo(request, id_party, id_tickets):
    context = {}
    tickets = Tickets.objects.get(ID_Party=id_party)
    context['tickets'] = tickets
    return render(request, 'Party/ticketbuy.html', context=context)
    # context = {}
    # try:
    #     context['sessions'] = Session.objects.get(id=id_sess)
    # except Session.DoesNotExist:
    #     raise Http404("movies_id does not exist")
    #
    # if request.method == 'POST':
    #     Ticket.tickets = request.POST.get('countTicket')
    #     return HttpResponseRedirect('ticketbuy')
    # return render(request, 'Movies/sessioninfo.html', context=context)