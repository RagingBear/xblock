from django.shortcuts import render


# Create your views here.
def dataset(request):
    return render(request, 'dataset.html')
