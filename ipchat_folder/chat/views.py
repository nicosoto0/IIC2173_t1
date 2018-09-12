from django.views import generic
from django.views.generic.edit import CreateView
from .models import Message
from ipware import get_client_ip
from uuid import getnode as get_mac
from django.utils import timezone



class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    context_object_name = 'all_msg'

    def get_queryset(self):
        return Message.objects.all()

class DetailView(generic.DetailView):
    model = Message
    template_name = 'chat/detail.html'
    context_object_name = 'msg'

class MessageCreate(CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        #form.content  = "fix comment"
        #self.object = form.save()
        form_request = self.request
        form.instance.ip_client = get_client_ip(form_request)[0]
        form.instance.ip_mac = get_mac()
        form.instance.request_time = timezone.now()

        return super().form_valid(form)
