from django.shortcuts import render


def index(request):
    """Home page for Learning Log application."""
    return render(request, 'learning_logs/index.html')
