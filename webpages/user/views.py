from django.shortcuts import render, get_object_or_404,redirect
from .models import Question,Answer
from django.http import HttpResponseRedirect
from .forms import QuestionForm,AnswerForm,RegistrationForm
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request,'user/login.html')

def logout(request):
    return render(request,'user/logout.html')

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RegistrationForm()
    args= {'form':form}
    return render(request,'user/register.html', args)



def post_question(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            pk=post.pk
            post.save()
            return redirect('question')
    else:
        form=QuestionForm()
    args={'form':form}
    return render(request, 'user/question.html', args)




def question(request):
    post=Question.objects.all().order_by('-created')
    args={'post':post}
    return render(request, 'user/home.html', args)

def question_detail(request, slug):
    post= get_object_or_404(Question, slug=slug)
    args={'post':post}
    return render(request, 'user/detail.html', args)

def answer(request, slug):
    post = get_object_or_404(Question, slug=slug)

    if request.method == 'POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.user=request.user
            answer.post=post
            answer.save()
            return redirect('question_detail', slug=post.slug)
    else:
        form=AnswerForm()
    args={'form':form}
    return render(request, 'user/answer.html', args)
