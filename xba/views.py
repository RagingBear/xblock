from django.shortcuts import render


# Create your views here.
def admin(request):
    return render(request, 'xba/index.html', {'request_path': request.path})


def researcher(request):
    return render(request, 'xba/researcher.html', {'request_path': request.path})


def paper(request):
    return render(request, 'xba/paper.html', {'request_path': request.path})


def dataset(request):
    return render(request, 'xba/dataset.html', {'request_path': request.path})
