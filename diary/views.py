from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    #msg = request.GET['msg']
    #return HttpResponse('Your message : ' + msg)

    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"