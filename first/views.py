from django.shortcuts import render
from .models import Todo
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import (
        ListView, DetailView, FormView,
        CreateView, UpdateView, DeleteView
    )
from .forms import TodoCreateForm, TodoCommentForm
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.dates import MonthArchiveView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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


class TodoDetailView(LoginRequiredMixin, FormView, DetailView):
    model = Todo
    form_class = TodoCommentForm
    users = User.objects.all()
    extra_context = {'users':users}
    login_url = 'accounts:login'
    template_name = 'first/todo_detail.html' #first/todo_detal.html
    context_object_name = 'todo' #object

    def get_success_url(self): #back to the page for comment
        return reverse('first:todo-detail', kwargs={'pk':self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form =self.get_form() 
        if form.is_valid():
            comment = Comment(todo=self.object, name=form.cleaned_data['name'], body=form.cleaned_data['body'])
        return super().form_valid(form)
    '''
    querset = Todo.objects.filter(pulished=True)
    ......or......
    def get_queryset(self, **kwargs):
        if request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['myslug'])
        else:
            pass

    --> path('<slug:myslug'/,...)
    
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
        todo = Todo(title=data['title'], slug=slugify(data['title'], owner=self.request.user))
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
        todo.owner = self.request.user
        messages.success(self.request, 'your todo add', 'success')
        return super().form_valid(form)


class TodoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'first/todo_delete.html'
    success_url = reverse_lazy('first:home')

    def test_func(self):
        obj = self.get_object()
        obj.owner = self.request.user
        
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
