from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(f'user: {request.user}')
    # return HttpResponse('<h1> sup dawg </h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(f'user: {request.user}')
    return render(request, 'contact.html', {})

def postal_view(request, *args, **kwargs):
    return render(request, 'postal.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'this about me',
        'my_number': (123, 321, 1234),
        'my_list': ['sup dawg', 'testing', 'lol', 8675309, 321]
    }
    return render(request, 'about.html', my_context)

# school stuff
def ev_tracker_view(request, *args, **kwards):
    return render(request, 'ev_tracker.html', {})
    