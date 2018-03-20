from django.shortcuts import render
from django.http import HttpResponse


def list_posts(requests):

    return HttpResponse("This is a list of posts.")


def show_post(request, post_id):

    return HttpResponse("This is a post %d" % post_id)
