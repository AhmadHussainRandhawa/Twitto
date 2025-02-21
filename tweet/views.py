from django.shortcuts import render

# Create your views here.
def tweet_page(request):
    return render(request, 'index.html')