from django.shortcuts import render

from learning_logs.models import Topic


def index(request):
    """Homepage for Learning Log application."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show list of topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show one topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)