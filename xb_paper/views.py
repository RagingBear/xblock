from django.shortcuts import render


# Create your views here.
def papers(request):
    return render(request, 'papers.html')
