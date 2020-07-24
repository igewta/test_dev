from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required  # 用来装饰登录状态


# Create your views here.
# 用来写请求的处理逻辑


def hello(request):
    return render(request, 'hello.html')


def login(request):
    """
    用户登录页，通过请求的方法来来区别操作
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username', '')  # 获取username，如果获取不到，赋值空字符串
        password = request.POST.get('password', '')

        if username == '' or password == '':
            print('获取到的用户名为空或者密码为空！！！')
            # print(f'获取的username 类型是 ：{type(username)}')
            return render(request, 'login.html', {'error': '用户名或者密码为空！'})

        user = auth.authenticate(username=username, password=password) # 从系统自带表中查询用户是否存在
        if user:
            auth.login(request, user)  # 记录用户的登录状态
            print('用户是存在的！', user)
            # 重定向到/manage/ url 地址，然后/manage/地址指向 manage 方法
            return HttpResponseRedirect('/manage/')
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})


@login_required
def manage(request):
    """
    登录后的主页，需要登录才能访问，所以要加限制
    :param request:
    :return:
    """
    return render(request, 'manage.html')


def logout(request):
    """
    退出登录，实质是删除数据库中对应的session
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect('/')




def login_action(request):
    """
    用户登录动作的处理, 这个用不到，直接用login 函数中的get post 方法来区分
    :param request:
    :return:
    """
    # print('登录的请求方法时：', request.method)
    if request.method == 'POST':
        username = request.POST.get('username', '')  # 获取username，如果获取不到，赋值空字符串
        password = request.POST.get('password', '')

        if username == '' or password == '':
            print('获取到的用户名为空或者密码为空！！！')
            print(f'获取的username 类型是 ：{type(username)}')
            return render(request, 'login.html', {'error': '用户名或者密码为空！'})

        user = auth.authenticate(username=username, password=password) # 从系统自带表中查询用户是否存在
        if user:
            print('用户是存在的！', user)
            return render(request, 'manage.html')
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})

    else:
        return render(request, 'login.html', {'error': '请求方法错误，请使用post 请求方法。'})


'''
django 处理逻辑
1. url 指定路径 /hello/
2. 在urls 文件里找到指定的方法
3. 在views 里找到方法，返回html
4. 在templates里找到对应的html文件
'''
