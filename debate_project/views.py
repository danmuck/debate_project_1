from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evidence
from .forms import EvidenceList

# Create your views here.

def main_ev_view(request):
    obj = Evidence.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'debate_project/main_ev.html', context)
    
def new_ev_view(request):
    form = EvidenceList(request.POST or None)
    if form.is_valid():
        form.save()
        form = EvidenceList()

    context = {
        'form': form
    }
    return render(request, 'debate_project/new_ev.html', context)

def delete_ev_view(request, ev_id):
    obj = get_object_or_404(Evidence, id=ev_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/ev_home/')
    context = {
        'object': obj
    }
    return render(request, 'debate_project/delete_ev.html', context)


def all_ev_view(request):
    queryset = Evidence.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'debate_project/all_ev.html', context)

#edit items
def ev_editor(request, ev_id):
    initial_data = 'ev_EDIT:'
    try:
        obj = Evidence.objects.get(id=ev_id)
    except Evidence.DoesNotExist:
        raise Http404
    form = EvidenceList(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'debate_project/new_ev.html', context, initial_data)
