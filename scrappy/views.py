from bs4 import BeautifulSoup
import requests
from django.http import JsonResponse
from django.shortcuts import render
from .utils import item_cleaner


def index(request):
    return render(request, 'scrappy/index.html')


def search_id(request):
    if request.method == "GET":
        url = request.GET.get('web', None)
        id = request.GET.get('id', None)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")
        item = soup.find(id=id)

        if item is not None:
            item = item.prettify()
        else:
            item = "Nic nie znaleziono"
        return JsonResponse(item, safe=False)


def search_class(request):
    if request.method == 'GET':
        url = request.GET.get('web', None)
        class_ = request.GET.get('class', None)
        element = request.GET.get('id', None)
        source = requests.get(url).text

        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element, class_=class_)
        out = item_cleaner(items)
        return JsonResponse(out, safe=False)


def search_el(request):
    if request.method == "GET":
        url = request.GET.get('web', None)
        element = request.GET.get('id', None)
        source = requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element)
        out = item_cleaner(items)
        return JsonResponse(out, safe=False)
