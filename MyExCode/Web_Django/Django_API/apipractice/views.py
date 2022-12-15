from django.http import JsonResponse
from .models import users
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addUser(request):  # 新增
    if request.method == "POST":
        try:
            account = request.POST["account"]
            password = request.POST["password"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            if users.objects.filter(account=account).exists():  # 若相同帳號
                result = {
                    "status": "fail",
                    "message": "%s is exists" % account
                }
            else:
                users.objects.create(account=account, password=password,
                                     email=email, phone=phone)
                item = (account, phone, email)
                result = {
                    "status": "success",
                    "message": "account:%s,phone:%s,email:%s" % item
                }
            return JsonResponse(result)
        except Exception:
            result = {
                "status": "fail",
            }
            return JsonResponse(result)


@csrf_exempt
def delUser(request):  # 刪除
    if request.method == "POST":
        try:
            account = request.POST["account"]
            users.objects.filter(account=account).delete()
            result = {
                "status": "success",
                "message": "%s is delete" % account
            }
            return JsonResponse(result)
        except Exception:
            result = {
                "status": "fail",
            }
            return JsonResponse(result)


@csrf_exempt
def getUserInfo(request):
    if request.method == "POST":
        try:
            account = request.POST["account"]
            target_account = users.objects.filter(account=account).get()
            item = (target_account.phone, target_account.email,
                    target_account.token_key)
            result = {
                "status": "success",
                "message": "phone:%s ,email:%s ,token_key%s" % item
            }
            return JsonResponse(result)
        except Exception:
            result = {
                "status": "fail",
            }
            return JsonResponse(result)
