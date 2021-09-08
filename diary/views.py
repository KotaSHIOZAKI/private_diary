from diary.forms import InquiryForm
#from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
#メッセージ送信用
import logging
from django.urls import reverse_lazy
#メッセージ取得用
from django.contrib import messages

#ロガーの取得
logger = logging.getLogger(__name__)

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
    #「メッセージを送信しました。」画面のURL
    success_url = reverse_lazy('diary:inquiry')

    #メール送信
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)