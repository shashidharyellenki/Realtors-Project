from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Listing # importing all the models into pages app from listing models
from realtors.models import Realtor #importing all the models into the pages for about page
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3] # we are only taking 3 latest models from the entier database
    context={
        'listings':listing,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request, 'pagess/index.html', context)
    # return HttpResponse( "Hello world")

def About(request):
    realtor = Realtor.objects.order_by('-hire_date')# here - indecats for descending order (latest added one will come fitst)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtor,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pagess/About.html', context) #we can acess all the data from the database into about.html using this context 