from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #インデックス
    path('', views.IndexView.as_view(), name="index"),
    
    #問い合わせ
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),

    #日記一覧表示
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    
    #日記詳細表示
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),

    #日記作成機能
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),

    #日記編集機能
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),

    #日記削除機能
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]
