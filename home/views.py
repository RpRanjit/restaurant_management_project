from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(user = request.user)
    return render(request, "home/note_list.html", {"notes": notes})
