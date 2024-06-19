from django.shortcuts import render

def sign_in(request):
    return render(request, 'authentication/sign-in.html')