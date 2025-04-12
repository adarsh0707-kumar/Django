from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  context = {
    'name': 'Adarsh',
    'age': 23,
    'nationality': 'Indian'
  }
  return render(
    request, 
    'index.html', 
    context
  )

def counter(req):
  text = req.POST['text']
  amount_of_words = len(text.split())
  return render( 
    req, 
    'counter.html',
    { 
      'amount' : amount_of_words
    }
  )
