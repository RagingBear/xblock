from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'xb/index.html')


def dataset(request):
    return render(request, 'xb/dataset.html')


def papers(request):
    return render(request, 'xb/papers.html')


def about(request):
    return render(request, 'xb/about.html')
