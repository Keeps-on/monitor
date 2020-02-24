from django.shortcuts import render, render_to_response, redirect


def index(request):
    # return render_to_response('index.html')
    return render(request, 'index.html')
