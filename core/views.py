from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    
    template_name = "core/home.html"
    
    # Reescribiendo el diccionario de contexto para almacenar las variables
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['title'] = 'Mi super web playground'
        # return context
    
    # Haciendo un render con la función get
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Mi Super Web Playground'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
