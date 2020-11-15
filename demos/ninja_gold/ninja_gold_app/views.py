from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    request.session.setdefault('total_gold',0)
    request.session.setdefault('activities',[])
    return render(request, 'index.html')


def process_form(request, building):
    if request.method == 'POST':
        print(request.POST)

        building = {
            'farm': randint(10, 20),
            'cave': randint(5, 10),
            'house': randint(2, 5),
            'casino': randint(-50, 50)
        }


        # if request.POST['building'] == 'farm' or building == 'farm':
        #     gold = randint(10, 20)
        # if request.POST['building'] == 'cave':
        #     gold = randint(5, 20)
        # if request.POST['building'] == 'house':
        #     gold = randint(2, 5)
        # if request.POST['building'] == 'casino':
        #     gold = randint(-50, 50)

        gold = building[request.POST['building']]

        print('gold is: ' + str(gold))
        request.session['total_gold'] += gold

        time = '{:%Y/%m/%d %I:%M %p}'.format(datetime.now())
        if gold > 0:
            # gained money
            print(time)
            result = f"Earned {gold} from the {request.POST['building']}! ({time})"
            earned = 'text-success'
            print(result)
        else:
            # loss money
            result = f"Enter a casino and lost {abs(gold)} gold....ouch... ({time})"
            earned = 'text-danger'
        request.session['activities'].append({'earned':earned, 'activity': result})

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')