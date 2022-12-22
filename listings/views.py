from typing import List
from django.shortcuts import render, get_object_or_404
from . models import Listing    #importing all the models from the models.py file
from django.core.paginator import Page, PageNotAnInteger, Paginator #imports for paginator
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    #pagination codes
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True) #fetching all the row from the file and arrangrs according to the latest one
    paginaotr = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginaotr.get_page(page)
    context={'listings':paged_listings}   #passing this to the html file
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context={
        'listing':listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] #if we type pool in the keywords then pool will be extractrd
        if keywords:
            queryset_list = queryset_list.filter(descrption__icontains=keywords)
    
    #city
    if 'city' in request.GET:
        city = request.GET['city'] #extracting data based on the cities
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    #State
    if 'state' in request.GET:
        state = request.GET['state'] #extracting data based on the cities
        print(state)
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms'] #extracting data based on the cities
        print(bedrooms)
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    #price
    if 'price' in request.GET:
        price = request.GET['price'] #extracting data based on the cities
        print(price)
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET
    }
    return render(request, 'listings/search.html', context)

'''
whene we give invalid pk then to get 404 page we are using get_object_or_404 method
'''