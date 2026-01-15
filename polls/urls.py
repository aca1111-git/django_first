from django.urls import path
from . import views

# app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    # http://127.0.0.1:8000/polls/
    # (도메인주소, views로 부터함수또는 클래스 호출, html에서 호출될 이름)
]
