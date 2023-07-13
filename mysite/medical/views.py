from django.shortcuts import render, redirect
import requests
from requests.structures import CaseInsensitiveDict

def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'POST':
        text = request.POST.get('location')
        api_key = '2f66e0d2e25a40ba8a098c2c3a03d727'
        url = f'https://api.geoapify.com/v1/geocode/autocomplete?text={text}&type=postcode&apiKey={api_key}'

        response = requests.get(url)
        data = response.json()
        # Process the response data as needed

        return render(request, 'form.html', {'data': data})