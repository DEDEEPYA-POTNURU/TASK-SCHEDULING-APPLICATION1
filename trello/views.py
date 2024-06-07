from django.shortcuts import render,redirect
from .form import BoardForm

def Board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trello')  
        form = BoardForm()
    return render(request, 'Board_form.html', {'form': form})
# Create your views here.
