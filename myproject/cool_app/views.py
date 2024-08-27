from django.shortcuts import render
from .form import Searchform

# Create your views here.f

def todos(request):
    # data
    data = [
        {'title':'Buy biscuit','complete':False},
        {'title':'Buy medicine','complete':True},
        {'title':'Buy vegtables','complete':True}
    ]

   
  
    # if search_form.is_valid():
    #     search_term = search_form.cleaned_data['Search']
    #     print(search_term)


    # url_string = request.GET.get('Search')

    # form
    search_form = Searchform(request.GET)

    # form data
    search_term=''
    if search_form.is_valid():
        search_term = search_form.cleaned_data['Search'].lower()
        

  

# loop and data print browser
    search_todo = []
    for todo in data:
        if search_term and search_term in todo.get('title').lower():
            search_todo.append(todo)
           

    data ={
        'todos': search_todo,
        'search_obj':search_form,
        }

    return render(request,'cool_app/todo.html',context=data)

