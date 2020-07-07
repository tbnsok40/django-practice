from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from django.utils import timezone

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html',{'portfolios':portfolios})
def newPortfolio(request):
    return render(request, 'newPortfolio.html')
def createPortfolio(request):
    
    print(request.POST)
    print(request.FILES)
    portfolios = Portfolio()
    portfolios.title = request.POST['title']
    portfolios.description = request.POST['description']
    
    portfolios.image = request.FILES['image']

    portfolios.save()
    return redirect('portfolio')
    # return render(request,'portfolio.html',{'portfolios': portfolios})