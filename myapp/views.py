from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    message ="""
    <center>
        <h1 style="color:green">Welcome to All Viewers</h1>
        <p>Please  <b style="color:blue">Like </b> and <b style="color:red">Subcribe</b> to My Channel</p>
    </center>
    """
    return HttpResponse(message)