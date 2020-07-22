from django.shortcuts import render

# Create your views here.
# 用来写请求的处理逻辑


def hello(request):
    return render(request, 'hello.html');
