from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
from django.db.models import F
from django.urls import reverse


# def index(request):
# 	# return HttpResponse("Hello) 기존코드
	
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	context = {"latest_question_list": latest_question_list}
# 	return render(request, "polls/index.html", context)

# 메인 페이지 (질문 목록)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.")

# 투표 처리 로직
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
# # def aa():
# # 	return HttpResponse("polls/aa.html")

# def aa(request):
# 	table_question_list = Question.objects.all()
# 	table_choice_list = Choice.objects.all()
	
# 	choice_first = Choice.objects.first()

# 	context = {
# 		"table_question_list" : table_question_list,
# 		"table_choice_list" : table_choice_list,
# 		"choice_first" : choice_first,
# 	}
# 	return render(request, "polls/aa.html", context)

    
