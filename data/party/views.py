from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.db import connection
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from data.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives

class PartyListView(ListView):
    model = Party
    context_object_name = 'party_List'
    template_name = 'Party/party_page.html'
    ordering = ['id']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.method == 'GET':
            search = self.request.GET.get('search')
            orderAge = self.request.GET.get("orderAge")
            orderLocal = self.request.GET.get("orderLocal")
            if search:
                qs = Party.objects.filter(name_party__istartswith=search)
                return qs
            elif orderAge:
                if orderAge != 'all':
                    qs = Party.objects.filter(age_party=orderAge)
                    return qs
                else:
                    return qs
            elif orderLocal:
                if orderLocal != 'all':
                    qs = Party.objects.filter(tickets__ID_Local__nameLocal=orderLocal)
                    return qs
                else:
                    return qs
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partyAge'] = Party.objects.all()
        context['locals'] = LocalsParty.objects.all()
        return context


def details_party(request, id_party):
    context = {}
    tickets = Tickets.objects.get(ID_Party=id_party)
    context['tickets'] = tickets
    if request.method == 'POST':
        countTickets = request.POST.get("countTickets")
        with connection.cursor() as cursor:
            cursor.executescript(
                f'''insert into party_sales(dataSales,countTicket,price_Ticket,User_id_id,tickets_id_id)VALUES(date('now'),{countTickets},({countTickets}*{tickets.price}),{request.user.id},{tickets.id});
                 UPDATE  party_tickets set count_ticket = count_ticket - {countTickets} where party_tickets.id ={tickets.id};
                ''')
        context['message'] = 1
        context['tickets'] = Tickets.objects.get(ID_Party=id_party)
        tic = Tickets.objects.get(ID_Party=id_party)
        messages = f"{request.user.username} your ticket to {tic.ID_Party.name_party}. " \
                   f" At the local {tic.ID_Local.nameLocal}. Located at {tic.ID_Local.address}." \
                   f"  And time {tic.date.strftime('%b %d %Y %H:%M:%S')}"
        subject = 'Your ticket! Party Search.'
        msg = EmailMessage(subject, messages, EMAIL_HOST_USER, [request.user.email])
        msg.send(fail_silently=True)

        return render(request, 'Party/about_party.html', context=context)
    return render(request, 'Party/about_party.html', context=context)

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
