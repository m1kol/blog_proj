from django.shortcuts import render
from django.http import HttpResponse


def list(request):

    return HttpResponse("List of the categories.")


def detail(request, category_id):

    return HttpResponse("Detail (list of posts) of category %d" % category_id)

