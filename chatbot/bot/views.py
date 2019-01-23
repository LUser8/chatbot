from django.shortcuts import render
from .models import ChatAssistent


def home(request):
    assist = ChatAssistent.objects.all()
    if request.method == 'POST':
        print(request.POST)
        answer = ChatAssistent.objects.get(question=request.POST['question'])
        context = {
            'title': 'Home',
            'answer': answer
        }
        return render(request, 'bot/home.html', context)

    context = {
        'title': 'Home',
        'assist': assist
    }
    return render(request, 'bot/home.html', context)
