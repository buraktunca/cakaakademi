from .models import Dersler, tutorials, study_question, testler, test_questions, test_answers, winners
from datetime import datetime,timedelta
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import  datetime
# Create your views here.

def main_page(request):

    last_dersler=Dersler.objects.filter()
    winner = winners.objects.all()
    content={"last_dersler":last_dersler,"winner":winner}

    return render(request,"index.html",content)

def ders_detail(request,id):

    ders = Dersler.objects.get(pk=id)
    tutorial=tutorials.objects.filter(ders=ders)
    studyquestions = study_question.objects.filter(ders=ders)
    content={"ders":ders,"tutorial":tutorial,"studyquestions":studyquestions}
    if request.method == "POST":
        count = 0
        k=1
        answer=[]
        for i in studyquestions:
            cevap=request.POST[str(i.pk)]
            if cevap == i.right_answer:
                count = count + 1
                k=k+1
            else:
                answer.append(k)
                count = count
                k=k+1

        content["puan"]=count
        content["wrong"]=answer
        content["amount"]=studyquestions.count()
        content["result"] = (count/studyquestions.count())*100


    return render(request,"ders_detail.html",content)


def signin(request):
    if request.user.is_authenticated:
        return redirect('testler/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/testler/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'page-signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'page-signin.html', {'form': form})


def test_page(request):
    if request.user.is_authenticated:
        testall = testler.objects.all()
        sorusayısı=[]
        for i in testall:
            sorusayısı.append(test_questions.objects.filter(test=i).count())
        list=zip(testall,sorusayısı)

        return render(request,"testler.html",{"list":list})


    else:
        return redirect("/signin/")



def solve_test(request,id):
    test = testler.objects.get(pk=id)
    qot = test_questions.objects.filter(test=test)
    date = datetime.today().strftime(("%d.%m.%Y %H:%M:%S"))
    if "time" not in request.session:
        request.session["time"]=date
    else:
        request.session["time"]

    content = {"qot" : qot,"test":test,"date":request.session["time"]}
    if request.method == "POST":
        for i in qot:
            cevap=request.POST[str(i.pk)]
            p=test_answers.objects.create(test=test,test_question=i,user=request.user,user_answer=cevap)
            p.save()
            return redirect("/result/")

    return render(request,"solvetest.html",content)



def konular(request):

    return render(request,"konular.html")
