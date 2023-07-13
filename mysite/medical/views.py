from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {})


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        open = request.POST.get('open')
        close = request.POST.get('close')
        location = request.POST.get('location')
        print(name)

        return render(request, 'form.html', {'name': name, 'open': open, 'close': close, 'location': location})
    
    return render(request, 'form.html', {})