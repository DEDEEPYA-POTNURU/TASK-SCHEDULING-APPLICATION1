from django.shortcuts import render
from django.http import HttpResponse
from trello.models import Board
from asana.models import Project
from podoist.models import Label
from notion.models import Workspace
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def trello(request):
    boards = Board.objects.all()
    return render(request, "trello.html" ,{'Board':boards})

@login_required
def asana(request):
    subject = Project.objects.all()
    return render(request, "asana.html" ,{'Project': subject})
@login_required
def podoist(request):
    time = Label.objects.all()
    return render(request, "podoist.html" ,{'Label': time})
@login_required
def notion(request):
    product = Workspace.objects.all()
    return render(request, "notion.html" ,{'Workspace': product})
    
@login_required
def forms(request):
    # Your view logic here
    return render(request, 'trello_form.html')