from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dataset(request):
    return render(request, 'dataset.html')


def papers(request):
    return render(request, 'papers.html')


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')
