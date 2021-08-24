from django.shortcuts import render
from django.template.defaultfilters import date

# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=${YOUR_API_KEY}")
    api = json.loads(news_api_request.content)

    return render(request, 'home.html', {'api': api})

def search(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.lower()
        
        
        search_topic_request =  requests.get("https://newsapi.org/v2/everything?q="+ quote +"&sortBy=publishedAt&apiKey=${YOUR_API_KEY}")   
        search_topic = json.loads(search_topic_request.content)
        return render(request, 'search.html', {'quote': quote, 'search_topic': search_topic})

    else:
        notfound = "Sorry, your request is not found. Please enter a new topic"
        return render(request, 'search.html', {'notfound': notfound})   

def sources(request):

    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/sources?apiKey=${YOUR_API_KEY}")
    api = json.loads(news_api_request.content)

    return render(request, 'sources.html', {'api': api})         
