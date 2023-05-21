from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Announce, Response, Mailer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import AnnounceForm, ResponseForm, AcceptForm, SendingNewsForm
from .tasks import send_notification_accepted_resp, send_news


class AnnounceList(ListView):
    model = Announce
    template_name = 'announces.html'
    context_object_name = 'announces'
    paginate_by = 4
    ordering = '-id'


class MyAnnounces(ListView, LoginRequiredMixin):
    raise_exception = True
    model = Announce
    template_name = 'myannounces.html'
    context_object_name = 'myannounces'

    def get_queryset(self):
        queryset = Announce.objects.filter(author=self.request.user)
        return queryset


class ResponsesList (ListView, LoginRequiredMixin):
    raise_exception = True
    model = Response
    template_name = 'responselist.html'
    context_object_name = 'responselist'
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announce = get_object_or_404(Announce, id=self.kwargs['pk'])
        context['responses'] = announce.response_set.all()
        return context


class AnnounceCreate(CreateView, LoginRequiredMixin):
    raise_exception = True
    form_class = AnnounceForm
    model = Announce
    template_name = 'anno_resp_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResponseCreate(CreateView, LoginRequiredMixin):
    raise_exception = True
    form_class = ResponseForm
    model = Response
    template_name = 'anno_resp_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnounceUpdate(UpdateView, LoginRequiredMixin):
    raise_exception = True
    form_class = AnnounceForm
    model = Announce
    template_name = 'anno_resp_edit.html'


class AnnounceDelete(DeleteView):
    model = Announce
    template_name = 'anno_resp_delete.html'
    success_url = reverse_lazy('home')


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'anno_resp_delete.html'
    success_url = reverse_lazy('my_announces')


class ResponseAccept(UpdateView, LoginRequiredMixin):
    raise_exception = True
    form_class = AcceptForm
    model = Response
    template_name = 'response_accept.html'

    def form_valid(self, form):
        form.save()
        if form.instance.accepted:
            send_notification_accepted_resp.apply_async(
                    (form.instance.author.email, form.instance.announce.author.username), countdown=10,)
        return redirect('/')


class Mailing(CreateView, PermissionRequiredMixin):
    permission_required = ('boa_app.add_mailer',)
    form_class = SendingNewsForm
    model = Mailer
    template_name = 'mailing.html'

    def form_valid(self, form):
        form.save()
        send_news.apply_async(
                (form.instance.announce.title, form.instance.announce.content), countdown=10,)
        return redirect('/')
