from django.shortcuts import render, redirect

# Create your views here.


def stock(request):
    try:
        if request.session['is_login'] != True:
            return redirect('/')
    except KeyError:
        return redirect('/')
    return render(request, 'stock.html')

def test(request):
    pass
