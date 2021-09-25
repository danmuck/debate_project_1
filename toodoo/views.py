from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import TooDoo
from .forms import TooDooList

# Create your views here.

def main_toodoo_view(request):
    obj = TooDoo.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'toodoo/main_toodoo.html', context)
    
def new_toodoo_view(request):
    form = TooDooList(request.POST or None)
    if form.is_valid():
        form.save()
        form = TooDooList()

    context = {
        'form': form
    }
    return render(request, 'toodoo/new_toodoo.html', context)

def delete_toodoo_view(request, toodoo_id):
    obj = get_object_or_404(TooDoo, id=toodoo_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/todo/')
    context = {
        'object': obj
    }
    return render(request, 'toodoo/delete_toodoo.html', context)


def all_toodoo_view(request):
    queryset = TooDoo.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'toodoo/all_toodoo.html', context)

#edit items
def toodoo_editor(request, toodoo_id):
    initial_data = {
        'title': 'New ToDo:'
    }
    try:
        obj = TooDoo.objects.get(id=toodoo_id)
    except TooDoo.DoesNotExist:
        raise Http404
    form = TooDooList(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'toodoo/new_toodoo.html', context)
