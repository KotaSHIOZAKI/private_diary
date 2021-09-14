from diary.forms import InquiryForm
#from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
#メッセージ送信用
import logging
from django.urls import reverse_lazy
#メッセージ取得用
from django.contrib import messages

#日記一覧用
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
#日記作成用（CRUDのC）
from diary.forms import DiaryCreateForm

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

#日記一覧表示
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at') #マイナス＝昇順
        return diaries

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary/diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False) #データに不足がある場合
        diary.user = self.request.user  #ログインしているユーザーのモデルオブジェクトをセット
        diary.save() #保存
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        #失敗したときに実行
        messages.error(self.request, '日記の作成に失敗しました。')
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary/diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '日記の更新に失敗しました。')
        return super().form_invalid(form)