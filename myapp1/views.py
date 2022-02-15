from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def myfunc():
    return "something"


def index(request):
    return HttpResponse("<html><body>This is index</body></html>")


def about(request):
    return HttpResponse("<html><body>This is about</body></html>")


def default(request):
    path = request.path
    method = request.method
    user_agent = request.META.get('HTTP_USER_AGENT')
    remote_address = request.META.get('HTTP_REMOTE_ADDR')
    default_content = "<html>" \
                      "<body>" \
                      "This is landing page at path: {} with method: {}" \
                      "You are using user agent {} and have remote address {}" \
                      "</body>" \
                      "</html>"
    return HttpResponse(default_content.format(path, method, user_agent, remote_address))
