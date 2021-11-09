from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('', views.main, name='main'),
    path('article/<int:id_article>',views.article_info,name='article_info'),
    path('registration',views.registration,name='registration'),
    path('signin',views.signin,name='signin'),
    path('write_article',views.write_article,name='write_article'),
    path('signout',views.signout,name='signout'),
    path('category/<int:id_category>',views.category_page,name='category_page'),
    path('task/<int:id_task>',views.task_info,name='task_info'),
    path('create_task',views.create_task,name='create_task'),
    path('tasks/',views.tasks, name='tasks'),
    path('lk',views.lk,name='lk'),
    path('user_info/<int:user_id>',views.user_info,name='user_info'),
    path('search_page',views.search_page,name='search_page')
    ]