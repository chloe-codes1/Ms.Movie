from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListCreate.as_view()),
    path('<int:review_pk>/', views.ReviewDetail.as_view()),
    path('<int:review_pk>/like/', views.like),
    path('<int:review_pk>/dislike/', views.dislike),
    path('<int:review_pk>/report/', views.Reporting.as_view()),
    path('comments/', views.CommentCreate.as_view()),
    path('comments/<int:comment_pk>/', views.CommentDetail.as_view()),

]