from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World! <br> Welcome to Elastic Beanstalk Django App!")
