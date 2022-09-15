from django.urls import path

from.import views

app_name = 'blog'
urlpatterns = [
    path('blog/',views.IndexView.as_view(),name="blog"),
    path('blog/inquiry/',views.InquiryView.as_view(),name="blog_inquiry"),
]