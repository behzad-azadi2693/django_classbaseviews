from django.shortcuts import render
from .models import Todo
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import (
        ListView, DetailView, FormView,
        CreateView, UpdateView, DeleteView
    )
from .forms import TodoCreateForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.dates import MonthArchiveView



class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'first/home.html')



class Index(TemplateView):
    template_name = 'first/todo_index.html'
    users = User.objects.all()
    extra_context = {'users':users}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context

class TodoListView(ListView):
    template_name = 'first/todo_list.html' #first/todo_list.html
    model = Todo 
    '''
    queryset = Todo.objects.all() 
    ......or......
    def get_queryset(self):
        return Todo.objects.all().ordering('-created')
    '''    
    
    users = User.objects.all()
    extra_context = {'users':users}
    context_object_name = 'todos' #object_list


class TodoDetailView(DetailView):
    model = Todo 
    users = User.objects.all()
    extra_context = {'users':users}
    '''
    querset = Todo.objects.filter(pulished=True)
    ......or......
    def get_queryset(self, **kwargs):
        if request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['myslug'])
        else:
            pass
    '''
    template_name = 'first/todo_detail.html' #first/todo_detal.html
    context_object_name = 'todo' #object 
    '''--> path('<slug:myslug'/,...)
    >>>DEFINE WORKING WITH PK<<<

    slug_field = 'slug' #name in models
    slug_url_kwarg = 'myslug' #name in url
    '''


class TodoCreateForm(FormView):
    form_class = TodoCreateForm
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')
    
    def form_valid(self, form):
        self.create_todo(form=cleaned_data)
        return super().form_valid(form)

    def create_todo(sefl, data): #this def we created
        todo = Todo(title=data['title'], slug=slugify(data['title']))
        todo.save()
        messages.success(self.request, 'your todo add', 'success')


class TodoCreate(CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        messages.success(self.request, 'your todo add', 'success')
        return super().form_valid(form)


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'first/todo_delete.html'
    success_url = reverse_lazy('first:home')


class TodoUpdate(UpdateView):
    model = Todo
    fieds = ('title',)
    template_name = 'first/todo_update.html'
    success_url = reverse_lazy('first:home')


class MonthTodo(MonthArchiveView):
    model = Todo
    date_field = 'created'
    month_format = '%m'
    template_name = 'first/todo_month.html'