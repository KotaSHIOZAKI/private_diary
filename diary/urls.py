from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #インデックス
    path('', views.IndexView.as_view(), name="index"),
    
    #問い合わせ
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]
