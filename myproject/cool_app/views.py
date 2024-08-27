from django.shortcuts import render
from .form import searchform

# Create your views here.f

def todos(request):
    # data
    data = [
        {'title':'Buy biscuit','complete':False},
        {'title':'Buy medicine','complete':True},
        {'title':'Buy vegtables','complete':True}
    ]

    search_obj = searchform(request.GET)
    if search_obj.is_valid():
        search_obj = search_obj.cleaned_data['Search']

    # data from url
    # url_string = request.GET.get('Search')
  

# loop and data print browser
    search_term = []
    for todo in data:
        if search_obj and search_obj.lower() in todo['title'].lower():
            search_term.append(todo)
           

    data ={
        'todos': search_term,
        'serch_obj':search_obj
        }

    return render(request,'cool_app/todo.html',context=data)

