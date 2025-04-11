from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BOOK

def BOOK_LIST(request):
    books = BOOK.objects.all()
    return render(request, 'BOOKSTORE/BOOK_LIST.html', {'books': books})

def LOGIN_VIEW(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('BOOK_LIST')
    return render(request, 'BOOKSTORE/LOGIN.html')

def LOGOUT_VIEW(request):
    logout(request)
    return redirect('BOOK_LIST')

@login_required
def ADD_TO_CART(request, BOOK_ID):
    cart = request.session.get('cart', [])
    cart.append(BOOK_ID)
    request.session['cart'] = cart
    return redirect('VIEW_CART')

@login_required
def VIEW_CART(request):
    cart = request.session.get('cart', [])
    books = BOOK.objects.filter(id__in=cart)
    return render(request, 'BOOKSTORE/CART.html', {'books': books})
