from django.shortcuts import render
# import 必要的函式庫
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import random
import urllib.request
import urllib.parse
from urllib.parse import quote 
# from .models import reg,BetList,grouplist,playbetlist,moneylist,templine,line_group,sort_list,admin_list
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage,ImagemapSendMessage, BaseSize, URIImagemapAction, MessageImagemapAction, ImagemapArea,JoinEvent, LeaveEvent,TextMessage
####計時器
from apscheduler.executors.pool import ThreadPoolExecutor
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from PIL import Image, ImageDraw, ImageFont
#檔案操作
import os
import shutil
from django.http import HttpResponse, JsonResponse
import json 
# Create your views here.
########redis#####
from django.core.cache import cache 


LINE_CHANNEL_ACCESS_TOKEN = "CXmSF2Hy7TTbyvBF5o2qec8utMwC6t8xLB5Ol4PoxxpZXssHwgorbsgR04r2QjQsRIx5iWDY4XAHSG4dHuTFEuPioIaseH29nIwxJoRLDTb1sr21d2fwb+Bhw9hX6xAe9oCtdUmIJGy/Spu4IU9FewdB04t89/1O/w1cDnyilFU="

LINE_CHANNEL_SECRET = "b740dc4deb4352100c88977b8d463c1f"
# 這邊是Linebot的授權TOKEN(等等註冊LineDeveloper帳號會取得)，我們為DEMO方便暫時存在settings裡面存取，實際上使用的時候記得設成環境變數，不要公開在程式碼裡喔！
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)

image_url ='https://www.gamelong.cc/static/images/sss.png?'
click_link_1 = 'https://drive.google.com/file/d/1B-L8BS7zhbEHuq7EkQVWeVQzOBiR5MFg/view?usp=sharing'
click_link_2 = 'https://drive.google.com/file/d/12vmWh7RYPz6r_YXuInqQM45v7uaPvywo/view?usp=sharing'
image_urlbet='https://www.gamelong.cc/static/images/QQQ.png?'
image_urlconnt='https://www.gamelong.cc/static/images/XXX.png?'
LIFF_url='https://liff.line.me/1654364997-eq01nZYj'


#event123='C04d3c7ffd8f072d2a6d85af94d06de1e'#測試群組ID
event123='Cca4a0e852499422bfce3e7cc10fa1b28'#輕鬆贏麻將妞妞

@csrf_exempt
def callback(request):
    if request.method == 'GET':
          code = request.GET.get('code','')
          status = request.GET.get('status','')
          result = {
                    "success":"true",  
                    "code":code,
                    "status":status,
                   }               
          response=HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json")
          response["Access-Control-Allow-Origin"] = "*"
          response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
          response["Access-Control-Max-Age"] = "1000"
          response["Access-Control-Allow-Headers"] = "*" 
          return response

    else:
          url = "https://www.pureentertainment.cc/bot/callback"
          result = {
                   
                    "code":"code",
                    "status":"false",
                   }               
          response=HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json")
          response["Access-Control-Allow-Origin"] = "*"
          response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
          response["Access-Control-Max-Age"] = "1000"
          response["Access-Control-Allow-Headers"] = "*" 
          return response 



def assign(account):     
    if account.message.text== '綁定':       
       sts=reg.objects.filter(line_Id=account.source.user_id)
       if len(sts) == 0: 
          templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單           
          author = templine(save_line_id=account.source.user_id)
          author.save() 
          result='請輸入帳號?'       
       else:
          result='您的帳號已經被綁定!'
    elif account.message.text== '查詢餘額': 
       sts=reg.objects.filter(line_Id=account.source.user_id)
       if len(sts) != 0:
          sts1 = reg.objects.get(line_Id=account.source.user_id)                   
          result='目前餘額:'+sts1.sum_amt
          return result          
       else:
          result='請先LINE綁定'
          return result
    elif account.message.text== '解除綁定': 
      sts=reg.objects.filter(line_Id=account.source.user_id)
      if len(sts) != 0:
         sts1 = reg.objects.get(line_Id=account.source.user_id)
         sts1.line_Id=''
         sts1.user_name=''
         sts1.save()
         result='已解除綁定'
         return result          
      else:
         result='請先LINE綁定'
         return result                 
    elif account.message.text== '紀錄': 
       sts=reg.objects.filter(line_Id=account.source.user_id)
       if len(sts) != 0:
          D1 = datetime.now()           
          T1=str(D1)
          T1=T1[:-15]
          T1=T1+'00:00:00'
          #T1='2020-05-09 00:00:00'
          print(T1)

          AA=''
          sts=playbetlist.objects.filter(line_Id=account.source.user_id,Bet_time__gte =T1)#取今天的下注紀錄          
          if len(sts) != 0:
             AA=Calrecord(account)            
             result=AA
          else:
             result='今天沒有下注紀錄'
          return result             
       else:
          result='請先LINE綁定'
          return result                
    else:
      result='請輸入關鍵字有問題'
      if account.message.text!='881':
         ttt=templine.objects.filter(save_line_id=account.source.user_id)
         if len(ttt)==1:                                
            tt1=templine.objects.get(save_line_id=account.source.user_id)
            if tt1.user_id=='':                
               sts=reg.objects.filter(acc_Id=account.message.text)
               if len(sts) == 1:
                  ss=reg.objects.get(acc_Id=account.message.text)
                  if ss.line_Id!=''and ss.line_Id!=None :
                     templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單 
                     result='此帳號已綁定、離開此流程' 
                     return  result
                  if ss.LV>0 :
                     templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單 
                     result='只有會員帳號才能綁定、離開此流程' 
                     return  result                       
                  tt1.user_id = account.message.text
                  tt1.save()  
                  result='請輸入此帳號的密碼'
                  return  result
               else:
                  result='請輸入正確的帳號或輸入881離開此流程'
                  return  result    
            else:              
                ss=reg.objects.get(acc_Id=tt1.user_id)
                profile = line_bot_api.get_profile(account.source.user_id)                 
                if ss.PassWod==account.message.text:
                   ss.user_name=profile.display_name                  
                   ss.line_Id=account.source.user_id
                   ss.save()
                   templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單
                   result='手機認證成功'                  
                   return  result
                else:
                   templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單
                   result='手機認證失敗,結束流程'                
                   return  result            
         else:           
           result='請輸入關鍵字'#'不要逼我說話'#'請輸入註冊或餘額'
           return  result
      else:
          tt1=templine.objects.filter(save_line_id=account.source.user_id)
          if len(tt1)!=0:
             templine.objects.filter(save_line_id=account.source.user_id).delete()#刪除註冊表單
             result='離開流程' 
          else:
             result='沒進入綁定手機流程' 
    return  result

def share(account): 
    profile = line_bot_api.get_profile(account.source.user_id)   
    sts=reg.objects.filter(line_Id=profile.user_id)
    if len(sts) != 0:
       sts1 = reg.objects.get(line_Id=profile.user_id) 
       result='https://social-plugins.line.me/lineit/share?url=海寶奇幻世界,推廣連結%20https://www.topfish.cc/register.html?registerid='+sts1.promotion_code
       return result          
    else:
       result='請先LINE綁定'
       return result    




def countN(s): #數字
    count_a=count_z=count_o=count_s=0
    for i in s:
       if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
          count_a=count_a+1
       elif ord(i)>=48 and ord(i)<=57:
          count_z=count_z+1
       elif ord(i)==32:
          count_s=count_s+1
       else:
          count_o=count_o+1
    return  count_z

def countA(s): #英文
    count_a=count_z=count_o=count_s=0
    for i in s:
       if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
          count_a=count_a+1
       elif ord(i)>=48 and ord(i)<=57:
          count_z=count_z+1
       elif ord(i)==32:
          count_s=count_s+1
       else:
          count_o=count_o+1
    return  count_a 

def countS(s): #空白
    count_a=count_z=count_o=count_s=0
    for i in s:
       if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
          count_a=count_a+1
       elif ord(i)>=48 and ord(i)<=57:
          count_z=count_z+1
       elif ord(i)==32:
          count_s=count_s+1
       else:
          count_o=count_o+1
    return  count_s
 
def countO(s): #其他
    count_a=count_z=count_o=count_s=0
    for i in s:
       if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
          count_a=count_a+1
       elif ord(i)>=48 and ord(i)<=57:
          count_z=count_z+1
       elif ord(i)==32:
          count_s=count_s+1 
       else:
          count_o=count_o+1
    return  count_o
 
def checkAccount(s): #檢查帳號
    a=0
    AN=countN(s)
    AA=countA(s)
    AS=countS(s)
    AO=countO(s)
    AC=AN+AA
    if AC==12 and AN>=0 and AA>=0 and AO==0 and AS==0:
       a=0
    else:
       a=1
    return  a

def checknumber(s): #檢查數字
    a=0
    AN=countN(s)
    AA=countA(s)
    AS=countS(s)
    AO=countO(s)
    if AN>=1 and AA==0 and AO==0 and AS==0:
       a=0
    else:
       a=1
    return  a    
def foo(num):#判斷是否為浮點數
    try:
        float(num)
        return 0
    except:
        return 1         
def ioo(num):#判斷是否為整數
    try:
        int(num)
        return 0
    except:
        return 1   
        
def changebet(s):#判斷是否為整數
    a=''
    if s=='1':
       a='A'
    elif s=='2':
       a='B'
    elif s=='3':
       a='C'
    elif s=='4':
       a='D'    
    elif s=='5':
       a='E'    
    elif s=='6':
       a='F'                     
    return  a  

def savesort(line_Id,num,Betmoney):#儲存莊家列表
    sts=sort_list.objects.filter(line_Id=line_Id)
    if len(sts)>1:
       return 1 
    else:
       D1 = datetime.now() 
       T1=str(D1)
       T1=T1[:-7]    
       ss=reg.objects.filter(line_Id=line_Id)
       if len(ss)==1: 
          ss=reg.objects.get(line_Id=line_Id)
          if int(num)==1:
             author = sort_list(Tid=ss.id,acc_Id=ss.acc_Id,nickname=ss.nickname,line_Id=line_Id,
                  user_name=ss.user_name,feq='2',maxup=Betmoney,ST='0',Create_Time=T1)
             author.save() 
             return 0
          elif int(num)==2:
             author = sort_list(Tid=ss.id,acc_Id=ss.acc_Id,nickname=ss.nickname,line_Id=line_Id,
                  user_name=ss.user_name,feq='2',maxup=Betmoney,ST='0',Create_Time=T1)
             author.save()
             #time.sleep(1)
             sts=sort_list.objects.filter(line_Id=line_Id)
             if len(sts)==1:
                author = sort_list(Tid=ss.id,acc_Id=ss.acc_Id,nickname=ss.nickname,line_Id=line_Id,
                    user_name=ss.user_name,feq='2',maxup=Betmoney,ST='0',Create_Time=T1)
                author.save() 
             return 0
       else:
         return 1 

def Calrecord(account): #計算下注紀錄
    D1 = datetime.now() 
    T1=str(D1)
    T1=T1[:-15]
    T1=T1+'00:00:00'
    num=''
    maker_Card='' 
    TT=''
    AA=''
    BB=''
    CC=''
    DD=''
    YY=''
    MA=0
    MB=0
    MC=0
    MD=0
    MM=0
    ZZ=0
    A=0
    sts=playbetlist.objects.filter(line_Id=account.source.user_id,Bet_time__gte =T1)#取今天的下注紀錄  
    I=len(sts)
    for p in sts:      
      if A==0:
        if p.BetOkMy!='':
           ZZ=float(p.BetOkMy)
      else:
        if p.BetOkMy!='':
           ZZ=ZZ+float(p.BetOkMy)   
      if num!=p.Num_Board :           
         if A>0:
            TT=TT+'局數'+num+'\n'
            TT=TT+'莊家牌型['+maker_Card+']\n' 
            if MA!=0:
               TT=TT+'A區牌型['+AA+']\n' 
               TT=TT+'A區下注['+str(MA)+']\n'
            if MB!=0:
               TT=TT+'B區牌型['+BB+']\n'    
               TT=TT+'B區下注['+str(MB)+']\n'
            if MC!=0:
               TT=TT+'C區牌型['+CC+']\n'    
               TT=TT+'C區下注['+str(MC)+']\n '
            if MD!=0: 
               TT=TT+'D區牌型['+DD+']\n' 
               TT=TT+'D區金下注['+str(MD)+']\n'
            TT=TT+'所得總額['+str(MM)+']\n'
         MA=0
         MB=0
         MC=0
         MD=0
         MM=0
         if p.Betnumber =='1':  
            AA=p.User_Card            
            MA=float(p.Betmoney)
         elif p.Betnumber =='2': 
            BB=p.User_Card             
            MB=float(p.Betmoney)
         elif p.Betnumber =='3': 
            CC=p.User_Card
            MC=float(p.Betmoney)
         elif p.Betnumber =='4':
            DD=p.User_Card
            MD=float(p.Betmoney)
         MM=float(p.BetOkMy)   
         num=p.Num_Board 
         maker_Card=p.Bookmaker_Card            
      else:      
         if p.Betnumber =='1':  
            AA=p.User_Card                        
            MA=MA+float(p.Betmoney)
         elif p.Betnumber =='2':      
            BB=p.User_Card                    
            MB=MB+float(p.Betmoney)
         elif p.Betnumber =='3': 
            CC=p.User_Card            
            MC=MC+float(p.Betmoney)
         elif p.Betnumber =='4':
            DD=p.User_Card            
            MD=MD+float(p.Betmoney)
         MM=MM+float(p.BetOkMy)
      A=A+1         
      if A==I:               
         TT=TT+'局數'+num+'\n'
         TT=TT+'莊家牌型['+maker_Card+']\n' 
         if MA!=0:
            TT=TT+'A區牌型['+AA+']\n' 
            TT=TT+'A區下注['+str(MA)+']\n'
         if MB!=0:
            TT=TT+'B區牌型['+BB+']\n'    
            TT=TT+'B區下注['+str(MB)+']\n'
         if MC!=0:
            TT=TT+'C區牌型['+CC+']\n'    
            TT=TT+'C區下注['+str(MC)+']\n '
         if MD!=0: 
            TT=TT+'D區牌型['+DD+']\n' 
            TT=TT+'D區金下注['+str(MD)+']\n'
         TT=TT+'所得總額['+str(MM)+']\n'
    YY='當天總計結果['+str(ZZ)+']\n'+TT     
    return  YY       

def photo(header): #圖文合成  
    font_type = 'C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\kaiu.ttf'#'/static/images/kaiu.ttf'
    font = ImageFont.truetype(font_type, 80)
    color = "#FFFF00"
       #加載背景圖片
    image = Image.open('C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\sss.png')
    imageA = image.convert('RGBA')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    D1 = datetime.now() 
    T1=str(D1)
    TH=str(D1.hour)   #時
    TM=str(D1.minute)
    TS=str(D1.second)

    T1=T1[:-16]
    header_x = 0
    header_y = 0
    draw.text((header_x,header_y), u'%s' % header, color, font)#位置,文字,顏色,字型
    image2=T1+'-'+TH+TM+TS+'0.png'
    image = image.resize((width, height),Image.ANTIALIAS)
    image.save('C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\Temp\\'+T1+'-'+TH+TM+TS+'0.png',quality=30, subsampling=0)
    return image2 

def photo1(header): #圖文合成  
    font_type = 'C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\kaiu.ttf'#'/static/images/kaiu.ttf'
    font = ImageFont.truetype(font_type, 80)
    color = "#FFFF00"
       #加載背景圖片
    image = Image.open('C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\QQQ.png')
    imageA = image.convert('RGBA')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    D1 = datetime.now() 
    T1=str(D1)
    TH=str(D1.hour)   #時
    TM=str(D1.minute)
    TS=str(D1.second)

    T1=T1[:-16]
    header_x = 0
    header_y = 0
    draw.text((header_x,header_y), u'%s' % header, color, font)#位置,文字,顏色,字型
    image2=T1+'-'+TH+TM+TS+'1.png'
    image = image.resize((width, height),Image.ANTIALIAS)
    image.save('C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\Temp\\'+T1+'-'+TH+TM+TS+'1.png',quality=30, subsampling=0)
    return image2     

def Temppoint(): #刪除資料夾與重建一個資料夾
    dirpath='C:\\Users\\autokk\\Desktop\\linemessage\\static\\images\\Temp'
    shutil.rmtree(dirpath) # 能删除该文件夹和文件夹下所有文件
    os.mkdir(dirpath)
    return   

@csrf_exempt
def test(request):#
    if request.method == 'POST' :        
       #group_id = request.POST.get('group_id','')
       ggp=line_group.objects.get(id=1)  
       LK = request.POST.get('LK','')
       bmt=playbetlist.objects.filter(GroupId=ggp.group_id,Num_Board=LK)       
       ll=len(bmt)

       mm=0#莊家總額
       qq=1
       AA=''
       for p in bmt:
          AA=AA+str(qq)+'.('+p.BetOkMM+')'
          mm=mm+float(p.BetOkMM)
          qq=qq+1
       result = {
                  "success":"true",
                  "mm": str(mm),
                  "AA":AA,
                 }
       response=HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json")
       response["Access-Control-Allow-Origin"] = "*"
       response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
       response["Access-Control-Max-Age"] = "1000"
       response["Access-Control-Allow-Headers"] = "*"
       return response          
    result = {
               "success":"false",
               "error_msg":"不是用POST傳訊息",
            }           
    response=HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response    
