from django.shortcuts import render
from .models import memory
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm

@login_required(login_url='/accounts/login')
def show(request):
    log_user = request.user
    memories = memory.objects.filter(user=log_user)
    return render(request, 'showdiary.html', {'m':memories})


@login_required(login_url='/accounts/login')
def add(request):
    if request.method == "POST":
        data = request.POST['data']
        color = request.POST['color']
        new = memory(content=data,color=color, user=request.user)
        new.save()
        return render(request, 'addmemory.html')
    else:
        return render(request, 'addmemory.html')

