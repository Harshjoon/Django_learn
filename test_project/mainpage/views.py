from django.shortcuts   import render
from django.http        import HttpResponse

tasks = [
    {
        'name'      : 'Clinical',
        'title'     : 'Clinical tasks',
        'content'   : 'fill all surgery details',
    },
    {
        'name'      : 'Feild service',
        'title'     : 'Feild service tasks',
        'content'   : 'fill all serive related details',
    },
]


# def home(request):
#     #return HttpResponse('<hi>home page</h1>')   
#     return render(request, 'mainpage/mainpage.html')


def home(request):
    context     = {
        'tasks'     : tasks
    }
    #return HttpResponse('<hi>home page</h1>')   
    return render(request, 'mainpage/mainpage.html', context)

def about(request):
    return render(request, 'mainpage/about.html', {'title': 'About'})