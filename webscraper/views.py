from django.http import HttpResponseRedirect
import requests
from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from.models import Link


def home(request):

    if request.method == 'POST':
        new_link = request.POST.get('page','')
        url = requests.get(new_link)
        beutify_soup = BeautifulSoup(url.text, 'html.parser')
    
        for link in beutify_soup.find_all('a'):
            link_address = link.get('href')
            link_name = link.string

            Link.objects.create(string_name=link_name, address=link_address)
        return HttpResponseRedirect('/')
    else:
        datas = Link.objects.all()


    return render(request, 'home.html',{"datas":datas})