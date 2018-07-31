from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'messenger/thread_list.html'
    

    """
    # En este caso (heredando en esta clase de: ListView) se tiene una  relacion inversa ya que a partir de un usuario user
    # podemos consultar todos los hilos de los que forma parte haciendo un:
    #                            user.threads.all() 
    # por lo que este bloque no es necesario

    model = Thread

    def get_queryset(self):
        queryset = super(ThreadList, self).get_queryset()
        return queryset.filter(users=self.request.user)
    
    """
@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    #print(request.GET)
    json_response = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
    else:
        raise Http404('El usuario no se encuentra autenticado')
    return JsonResponse(json_response)