from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User, Quiz, Challenger
from random import randint

domain = "http://localhost:8000/quiz/"

# Create your views here.
def quiz_home(request):
    if request.GET:
        user = User()
        user.name = request.GET['name']
        user.hashcode = request.GET['hashcode']
        user.save()
        return redirect("quiz:quiz_create", user.id)

    return render(request, "quiz/quiz_home.html")

def quiz_create(request, pk):
    user = get_object_or_404(User, pk=pk)

    if user.quiz_url:
        return redirect("quiz:quiz_home") 

    num = 1
    if request.POST:
        num = int(request.POST['quiz_id']) + 1
        if num > 10:
            return redirect("quiz:quiz_complete", pk)
        user.answer = ''.join([user.answer, request.POST['answer']])
        user.save()
        
    quiz = get_object_or_404(Quiz, id=num)
    
    return render(request, "quiz/quiz_create.html", {'quiz':quiz})

def quiz_complete(request, pk):
    user = get_object_or_404(User, pk=pk)

    if len(user.answer) == 10:
        while True:
            try:
                user.quiz_url=domain+str(randint(1, 999999)).zfill(6)
                user.save()
                break
            except:
                pass
    return render(request, "quiz/quiz_complete.html", {"user":user})


#퀴즈 풀이
def solve_home(request, quiz_url):
    user = get_object_or_404(User, quiz_url=domain+str(quiz_url))

    if request.GET:
        challenger = Challenger()
        challenger.name = request.GET['name']
        challenger.user_obj = user
        challenger.save()
        return redirect("quiz:solve_quiz", challenger.pk)

    return render(request, "quiz/solve_home.html", {"user":user})

def solve_quiz(request, pk):
    challenger = get_object_or_404(Challenger, pk=pk)
    user = challenger.user_obj

    num = 1
    if request.POST:
        num = int(request.POST['quiz_id']) + 1
        
        if request.POST['answer'] == user.answer[num-2]:
            challenger.result += 1
            challenger.save()
        if num > 10:
                return render(request, "quiz/solve_result.html", {"user":user, "challenger":challenger})

    quiz = get_object_or_404(Quiz, id=num)
    
    return render(request, "quiz/solve_quiz.html", {'quiz':quiz})

def solve_result(request, pk):
    challenger = get_object_or_404(Challenger, pk=pk)
    user = get_object_or_404(User, pk=challenger.user_obj.pk)
    return render(request, "quiz/solve_result.html", {"user":user, "challenger":challenger})