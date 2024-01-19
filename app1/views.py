from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(requets):
    html = '''
        <h1> Assalamu alaykum bzining web sayitimizga hush kelibsiz </h1>
        <p>bugun juda qiziq narsa o`rganyapmiz</p>
        <a href="https://www.google.com"> google </a>
    '''
    return HttpResponse(html)

