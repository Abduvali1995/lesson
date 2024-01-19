from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(requets):
    html = '''
        <h1> Assalamu alaykum bzining web sayitimizga hush kelibsiz </h1>
        <p>bugun juda qiziq narsa o`rganyapmiz</p>
        <a href="second-view"> ikkinchi sahifa </a><br><br>
        <a href="3-view"> 3 sahifa </a><br><br>
        <a href="4-view"> 4 sahifa </a><br><br>
    '''
    return HttpResponse(html)

def second_view(request):
    html = '''
        <h1>ikkinchi sahifa</h1>
        <a href="../">orqaga</a>
    '''
    return HttpResponse(html)

def three_view(request):
    html = '''
        <h1>3 sahifa</h1>
        <a href="../">orqaga</a>
    '''
    return HttpResponse(html)
def four_view(request):
    html = '''
        <h1>4 sahifa</h1>
        <a href="../">orqaga</a>
    '''
    return HttpResponse(html)
