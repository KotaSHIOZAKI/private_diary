from diary.forms import InquiryForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

#インデックス（関数）
def index(request):
    #msg = request.GET['msg']
    #return HttpResponse('Your message : ' + msg)

    return render(request, 'diary/index.html')

#インデックス
class IndexView(generic.TemplateView):
    template_name = "diary/index.html"

#問い合わせ
class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm