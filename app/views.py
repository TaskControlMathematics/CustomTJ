from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
import json
from django.core.serializers import serialize
from django.db.models import Q


def main(request):
    all_articles = Article.objects.all()
    assigned_tasks = Task.objects.filter(status='assigned')
    work_tasks = Task.objects.filter(status='work')
    done_tasks = Task.objects.filter(status='done')
    return render(request, 'main.html', locals())


def article_info(request, id_article):
    article = Article.objects.get(id=id_article)

    return render(request, 'article_info.html', locals())


def task_info(request, id_task):
    task = Task.objects.get(id=id_task)
    statuses = Task._meta.get_field('status').choices
    statuses = [item[0]  for item in statuses if item[0]!=task.status]
    if request.POST.get('chenge_status'):
        new_status = request.POST.get('new_status')
        task.status = new_status
        task.save()
    return render(request, 'task_info.html', locals())


def registration(request):
    reg_form = SignUpForm()
    if request.POST:
        reg_form = SignUpForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            user.first_name = reg_form.cleaned_data.get('firstName')
            user.last_name = reg_form.cleaned_data.get('lastName')
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'registration.html', locals())


def signin(request):
    auth_form = AuthUserForm()
    if request.POST:
        email = request.POST["email"]
        username = User.objects.get(email=email).username
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'signin.html', locals())


def write_article(request):
    art_user = request.user
    art_first_name = art_user.first_name
    art_last_name = art_user.last_name
    categories = Categories.objects.all()
    if request.POST:
        art_date = date.today().strftime('%Y-%m-%d')
        art_text = request.POST['text']
        art_title = request.POST['title']
        category_id = request.POST['category']
        category = Categories.objects.get(id=category_id)
        Article.objects.create(title=art_title, text=art_text, date=art_date, user=art_user, category=category)
        return HttpResponseRedirect('/')
    return render(request, 'write_article.html', locals())


def create_task(request):
    statuses = Task._meta.get_field('status').choices
    statuses = [item[0] for item in statuses]
    users = User.objects.all()
    print(request.POST)
    if request.POST:
        text = request.POST['text']
        title = request.POST['title']
        status = request.POST['category']
        user_from = request.user
        user_to = User.objects.get(username=request.POST['user_to'])
        Task.objects.create(title=title,text=text,date=date.today().strftime('%Y-%m-%d'),user_from=user_from,status=status,user_to=user_to)
        return HttpResponseRedirect('/')
    return render(request,'create_task.html',locals())


def signout(request):
    if request.POST:
        logout(request)
    return HttpResponseRedirect('/')


def category_page(request, id_category):
    all_articles = Article.objects.filter(category__id=id_category)

    return render(request, 'category_page.html', locals())


def get_list_task(tasks_query):
    list_task = []
    for item in tasks_query:
        dct = {}
        dct['id'] = item.id
        dct['title'] = item.title
        dct['date'] = item.date
        dct['user'] = item.user_from
        list_task.append(dct)
    return list_task


def tasks(request):
    assigned_tasks = Task.objects.filter(status='assigned',user_to=request.user)
    work_tasks = Task.objects.filter(status='work',user_to=request.user)
    done_tasks = Task.objects.filter(status='done',user_to=request.user)
    assigned_list_task = get_list_task(assigned_tasks)
    work_list_task = get_list_task(work_tasks)
    done_list_task = get_list_task(done_tasks)

    return render(request, 'tasks.html',locals())

def lk(request):
    return render(request,'lk.html',locals())

def user_info(request,user_id):
    articles = Article.objects.filter(user__id = user_id)
    print(articles)
    return render(request,'user_info.html',locals())


def search_page(request):
    if request.GET:
        search_request = request.GET.get('q')
        all_articles = Article.objects.filter(Q(title__icontains=search_request)| Q(text__icontains=search_request))
        print(all_articles)
        return render(request,'main.html',locals())
    return render(request,'main.html',locals())