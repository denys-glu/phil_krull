from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # type of HTTP method from client
    print(request.method)
    print(request.GET)
    print(request.POST)
    # return HttpResponse("message from index method")
    context = {
        'day_of_week': "Sunday",
        'date': "11/1/2020",
        'loop': [1,2,3,4,5,6,7]
    }
    request.session['number'] = 1
    return render(request, 'index.html', context)

def say_hi(request, user_name):
    print(user_name)
    print(request.session['number'])
    return HttpResponse(f'Hi {user_name}')

def handle_form(request):
    print(request.POST)
    return redirect("/")