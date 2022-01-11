from django.urls import path
from .views import *

urlpatterns = [
    path('get-comments/<blogSlug>', GetBlogCommentsView.as_view()),
    path('get-comment/<blogSlug>', GetBlogCommentView.as_view()),
    path('create-comment/<blogSlug>', CreateBlogCommentView.as_view()),
]
