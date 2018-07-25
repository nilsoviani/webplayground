from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    # Este mixin requerirá que el usuario sea miembro del staff

    def dispatch(self, request, *args, **kwargs):
        # print(request.user)
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order'] Como está definido en PageForm se puede obviar
    success_url = reverse_lazy('pages:pages') # Con reverse_lazy se redirecciona sin necesidad de sobreescribir la funcion get_success_url
    
    # def get_success_url(self): Con esta funcion se redefine su valor y se redirecciona a la lista de publicaciones
        # return reverse('pages:pages')
    
    def dispatch(self, request, *args, **kwargs):
        # print(request.user)
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(PageCreate, self).dispatch(request, *args, **kwargs)

class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:pages')

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    
    def get_success_url(self):
        return reverse_lazy('pages:pages') + '?deleted'
