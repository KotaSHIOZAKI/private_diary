from diary.forms import InquiryForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

# Create your views here.
def index(request):
    #msg = request.GET['msg']
    #return HttpResponse('Your message : ' + msg)

    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name = "diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm