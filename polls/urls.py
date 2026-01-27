from django.urls import path
from . import views
from . import practice_views

app_name = "polls"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),

    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # path("<int:question_id>/results/", views.results, name="results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
    # 추가: CRUD
    path("create/", views.QuestionCreateView.as_view(), name="question_create"),
    # path 안 1번 : 도메인 경로는 http://127.0.0.1:8000/polls/create
    # 2번 : 제너릭에 CreateView 상속받아서 클래스 글 생성을 구현
    # 3번 : url polls:question_create 를 템플릿(html)로 보여줘라
    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question_update"),
    # 도메인 경로는 http://127.0.0.1:8000/polls/1/update 경로
    # 제너릭에 UpdateView 상속받아서 클래스 글 수정을 구현
    # url polls:question_update 을 템플릿(html) 로 보여줘라
    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question_delete"),  
    # 도메인 경로는 http://127.0.0.1:8000/polls/1/delete 경로
    # 제너릭에 DeleteView 상속받아서 클래스 글 수정을 구현
    # url polls:question_delete 을 템플릿(html) 로 보여줘라

    
    # # /polls/aa
    # path("aa/", views.aa, name="aa"),

    # ✅ 연습용 (브라우저 확인)
    path("practice/1/", practice_views.practice_1, name="practice_1"),
    path("practice/2/", practice_views.practice_2, name="practice_2"),
    path("practice/3/", practice_views.practice_3, name="practice_3"),
    path("practice/5/", practice_views.practice_5, name="practice_5"),
    path("practice/6/", practice_views.practice_6, name="practice_6"),

    # ✅ 연습용 (플랫폼 확인: JSON)
    path("practice/api/1/", practice_views.practice_api_1, name="practice_api_1"),
    path("practice/api/2/", practice_views.practice_api_2, name="practice_api_2"),
    path("practice/api/3/", practice_views.practice_api_3, name="practice_api_3"),
    path("practice/api/5/", practice_views.practice_api_5, name="practice_api_5"),
    path("practice/api/6/", practice_views.practice_api_6, name="practice_api_6"),
    
]

