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
    portfolio = Portfolio()
    portfolio.title = request.GET['title']
    portfolio.image = request.GET['image']
    portfolio.description = request.GET['description']
    portfolio.save()
    return redner(request,'portfolio.html',{'portfolios': portfolio})