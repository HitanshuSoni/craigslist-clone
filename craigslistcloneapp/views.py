from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request ,'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search': search
    }
    return render(request ,'craigslistcloneapp/new_search.html', stuff_for_frontend)