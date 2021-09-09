from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    return render(request, 'index.html')


def departure_view(request):
    return render(request, 'departure.html')


def tour_view(request, tour_id):
    return render(request, 'tour.html')
