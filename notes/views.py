from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

@login_required
def note_list(request):
    notes = Notes.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.user = request.user  # Assign the logged-in user
            notes.save()
            return redirect('note_list')
    else:
        form = NotesForm()
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Notes, pk=note_id, user=request.user)  # Ensure note belongs to user
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NotesForm(instance=note)
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Notes, pk=note_id, user=request.user)  # Ensure note belongs to user
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

