from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.hashers import check_password
from django.template.context_processors import csrf
from .forms import addUserForm, editUserForm
from .models import User
import pyotp
from datetime import datetime


def index(request):
    """首頁"""
    User().setRootAccount()  # 若無帳號建立第一個root帳號
    if 'ok' in request.GET:
        account = request.GET['account']
        password = request.GET['password']
        request.session['account'] = account
        if User.objects.filter(account=account).exists():
            dataPassword = User.objects.get(account=account)
            if check_password(password, dataPassword.password):
                request.session['is_login'] = None
                return redirect('verify/', account=account)
            else:
                return render(request, 'login.html', context={"message": "密碼錯誤"})
        else:
            return render(request, 'login.html', context={"message": "帳號不存在"})
    else:
        return render(request, 'login.html')


def googleVerify(request):
    """驗證碼頁面"""
    if 'veriftyok' in request.GET:
        verifty = request.GET['verifty']
        account = request.session['account']
        secret = User.objects.get(account=account).googleSecret
        if pyotp.totp.TOTP(secret).verify(verifty):
            request.session['is_login'] = True
            user = User.objects.filter(account=account).get()
            user.loginStatus = 'online'
            user.save()
            return redirect('/main/')
        else:
            return render(request, 'loginVerify.html', context={"message": "驗證碼錯誤"})
    else:
        return render(request, 'loginVerify.html')


def mainPage(request):
    '''主頁面'''
    try:
        if request.session['is_login'] != True:
            return redirect('/')
    except KeyError:
        return redirect('/')
    context = getAccount(request)
    context.update({'datetime': datetime.now()})
    return render(request, 'template.html', context=context)


def userPage(request):
    '''會員頁面'''
    try:
        if request.session['is_login'] != True:
            return redirect('/')
    except KeyError:
        return redirect('/')
    context = getAccount(request)
    context.update({'datetime': getTime()})
    userlist = User.objects.all()
    userdata = []
    for user in userlist:
        temp = {
            'id': user.id,
            'account': user.account,
            'accountID': user.accountID,
            'accountState': user.accountState,
            'createDate': user.createDate,
            'lastEditDate': user.lastEditDate,
            'googleQRCodeURL': user.googleQRCodeURL,
            'loginStatus': user.loginStatus,
            'detial': user.detial
        }
        userdata.append(temp)
    context.update({'userdata': userdata})
    return render(request, 'user.html', context=context)


def logout(request):
    '''登出動作'''
    request.session['is_login'] = False
    account = request.session['account']
    user = User.objects.filter(account=account).get()
    user.loginStatus = 'offline'
    user.save()
    return redirect('/')


def useraddforms(request):
    '''新增會員表單頁面'''
    try:
        if request.session['is_login'] != True:
            return redirect('/')
    except KeyError:
        return redirect('/')
    csrftoken = csrf(request)['csrf_token']  # 提供做csrftoken驗證
    addform = addUserForm(request.POST)
    context = {
        'csrftoken': csrftoken,
        'addform': addform
    }
    return render(request, 'useradd.html', context=context)


def usereditforms(request, id):
    '''編緝會員表單頁面'''
    try:
        if request.session['is_login'] != True:
            return redirect('/')
    except KeyError:
        return redirect('/')
    csrftoken = csrf(request)['csrf_token']  # 提供做csrftoken驗證
    user = User.objects.get(id=id)
    editform = editUserForm(request.POST)
    editform.default_account = user.account
    context = {
        'csrftoken': csrftoken,
        'editform': editform,
        'user': user
    }
    return render(request, 'useredit.html', context=context)


def useradd(request):
    '''處理新增會員操作'''
    if request.method == "POST":
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        message = ''
        request.session['message'] = message
        if User.objects.filter(account=account).exists():
            message = '帳號已存在'
            return redirect('/useradd/', message=message)
        User().createUser(account, password)
        return redirect('/user/')


def useredit(request):
    '''處理編輯會員操作'''
    if request.method == "POST":
        account = request.POST.get('account', '')
    return HttpResponse()


def txtPage(request):
    '''驗證SSL'''
    return render(request, '5E2440DD33F318F86C43B03EA08B6B62.txt')


def getAccount(request):
    '''取得帳號'''
    account = request.session['account']
    return {'account': account}


def getTime():
    '''取得時間'''
    return str(datetime.now())[:-7]
