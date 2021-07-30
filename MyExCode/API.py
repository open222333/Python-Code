def getPlaylist(request):  # 根據局號抓取　暱稱　下注結果　玩家下注結算餘額
    if request.method == 'POST':
        gameNum = request.POST.get('gameNum', '')
        numB = gameNum.split("-")[3]
        Datab = gameNum[:10]
        if grouplist.objects.filter(Data_B=Datab, Num_B=numB).exists():
            pass
        else:
            result = {
                "success": "true",
                "result": "局號不存在",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        numBoard = grouplist.objects.filter(
            Data_B=Datab, Num_B=numB).get().Num_Board
        playbetResult = playbetlist.objects.filter(Num_Board=numBoard)
        resultList = []
        for item in playbetResult:
            user_name = reg.objects.filter(
                line_Id=item.line_Id).get().user_name
            itemdict = {
                "playbetlistId": item.id,
                "user_name": user_name,
                "BetOk": item.BetOk,
                "BetOkMy": item.BetOkMy
            }
            resultList.append(itemdict)
        result = {
            "success": "true",
            "result": resultList,
        }
        response = HttpResponse(json.dumps(
            result, ensure_ascii=False), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    else:
        result = {
            "success": "false",
            "error_msg": "不是用POST傳訊息",
        }
        response = HttpResponse(json.dumps(
            result, ensure_ascii=False), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response


@csrf_exempt
def setAmount(request):  # 修改金額
    if request.method == 'POST':
        playbetlistId = request.POST.get('playbetlistId', '')
        corp = request.POST.get('account', '')
        amount = request.POST.get('amount', '')

        if playbetlistId == '':
            result = {
                "success": "false",
                "error_msg": "需傳遞playbetlistId",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif corp == '':
            result = {
                "success": "false",
                "error_msg": "需傳遞account",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        elif amount == '':
            result = {
                "success": "false",
                "error_msg": "需傳遞amount",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        try:
            float(amount)
        except ValueError:
            result = {
                "success": "false",
                "error_msg": "金額格式錯誤",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        if reg.objects.filter(acc_Id=corp).exists() == False:
            result = {
                "success": "false",
                "error_msg": "操作者輸入錯誤",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        if playbetlist.objects.filter(id=playbetlistId).exists() == False:
            result = {
                "success": "false",
                "error_msg": "此下注不存在",
            }
            response = HttpResponse(json.dumps(
                result, ensure_ascii=False), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        # 操作者ID
        Corp_account = reg.objects.filter(acc_Id=corp).get()
        Corp_Id = Corp_account.id
        # 取得修改的那個下注
        PBLData = playbetlist.objects.filter(id=playbetlistId).get()
        gid = PBLData.GroupId
        nb = PBLData.Num_Board
        uid = PBLData.line_Id
        betok = PBLData.BetOk
        betokmy = PBLData.BetOkMy
        bid = PBLData.Bookmaker_Id
        bmm = PBLData.BetOkMM
        bid1 = PBLData.Bookmaker1_Id
        bmm1 = PBLData.BetOk1MM
        bid2 = PBLData.Bookmaker2_Id
        bmm2 = PBLData.BetOk2MM
        bid3 = PBLData.Bookmaker3_Id
        bmm3 = PBLData.BetOk3MM
        bid4 = PBLData.Bookmaker4_Id
        bmm4 = PBLData.BetOk4MM
        bid5 = PBLData.Bookmaker5_Id
        bmm5 = PBLData.BetOk5MM

        ss = grouplist.objects.get(GroupId=gid, Num_Board=nb)
        # 修改單筆下注結果
        if int(amount) > 0:
            PBLData.BetOk = '1'
            PBLData.BetEnd = 'W'
        elif int(amount) < 0:
            PBLData.BetOk = '-1'
            PBLData.BetEnd = 'L'
        else:
            PBLData.BetOk = '0'
            PBLData.BetEnd = 'T'

        cause = '9'
        # 玩家還原金額
        uacc = reg.objects.filter(line_Id=uid).get()
        aocu = round(float(betokmy)*-1, 2)
        uacc.sum_amt = str(round(float(uacc.sum_amt)+aocu, 2))  # 還原金額
        uacc.save()
        # 玩家還原金額紀錄錢包
        user = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.LId), Cause=cause, Amt_In='0', Amt_Out=str(aocu), Amt_All=uacc.sum_amt, Create_Time=gettime())
        user.save()

        # 莊家還原金額
        bma = reg.objects.get(line_Id=bid)
        aocb = round(float(bmm)*-1, 2)
        bma.sum_amt = str(round(float(bma.sum_amt)+aocb, 2))  # 還原金額
        bma.save()
        # 莊家還原金額紀錄錢包
        bm = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId), Cause=cause, Amt_In=str(aocb), Amt_Out='0', Amt_All=bma.sum_amt, Create_Time=gettime())
        bm.save()

        # 配莊1還原金額
        bma1 = reg.objects.get(line_Id=bid1)
        aocb1 = round(float(bmm1)*-1, 2)
        bma1.sum_amt = str(round(float(bma1.sum_amt)+aocb1, 2))  # 還原金額
        bma1.save()
        # 配莊1還原金額紀錄錢包
        bm1 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId1), Cause=cause, Amt_In=str(aocb1), Amt_Out='0', Amt_All=bma1.sum_amt, Create_Time=gettime())
        bm1.save()

        # 配莊2還原金額
        bma2 = reg.objects.get(line_Id=bid2)
        aocb2 = round(float(bmm2)*-1, 2)
        bma2.sum_amt = str(round(float(bma2.sum_amt)+aocb2, 2))  # 還原金額
        bma2.save()
        # 配莊2還原金額紀錄錢包
        bm2 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId2), Cause=cause, Amt_In=str(aocb2), Amt_Out='0', Amt_All=bma2.sum_amt, Create_Time=gettime())
        bm2.save()

        # 配莊3還原金額
        bma3 = reg.objects.get(line_Id=bid3)
        aocb3 = round(float(bmm3)*-1, 2)
        bma3.sum_amt = str(round(float(bma3.sum_amt)+aocb3, 2))  # 還原金額
        bma3.save()
        # 配莊3還原金額紀錄錢包
        bm3 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId3), Cause=cause, Amt_In=str(aocb3), Amt_Out='0', Amt_All=bma3.sum_amt, Create_Time=gettime())
        bm3.save()

        # 配莊4還原金額
        bma4 = reg.objects.get(line_Id=bid4)
        aocb4 = round(float(bmm4)*-1, 2)
        bma4.sum_amt = str(round(float(bma4.sum_amt)+aocb4, 2))  # 還原金額
        bma4.save()
        # 配莊4還原金額紀錄錢包
        bm4 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId4), Cause=cause, Amt_In=str(aocb4), Amt_Out='0', Amt_All=bma4.sum_amt, Create_Time=gettime())
        bm4.save()

        # 配莊5還原金額
        bma5 = reg.objects.get(line_Id=bid5)
        aocb5 = round(float(bmm5)*-1, 2)
        bma5.sum_amt = str(round(float(bma5.sum_amt)+aocb5, 2))  # 還原金額
        bma5.save()
        # 配莊5還原金額紀錄錢包
        bm5 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
            PBLData.BId5), Cause=cause, Amt_In=str(aocb5), Amt_Out='0', Amt_All=bma5.sum_amt, Create_Time=gettime())
        bm5.save()

        # 變動playbetlist
        bkmmoy = ss.Bkmmoney
        bkkmoy1 = ss.Bkkmoney1
        bkkmoy2 = ss.Bkkmoney2
        bkkmoy3 = ss.Bkkmoney3
        bkkmoy4 = ss.Bkkmoney4
        bkkmoy5 = ss.Bkkmoney5

        mmomey = [0]*6
        mpro = [0]*6
        mmomey[0] = mmomey[1] = mmomey[2] = mmomey[3] = mmomey[4] = mmomey[5] = 0

        mmomey[0] = float(bkmmoy)
        if bid1 != '':
            mmomey[1] = float(bkkmoy1)
        if bid2 != '':
            mmomey[2] = float(bkkmoy2)
        if bid3 != '':
            mmomey[3] = float(bkkmoy3)
        if bid4 != '':
            mmomey[4] = float(bkkmoy4)
        if bid5 != '':
            mmomey[5] = float(bkkmoy5)
        bmb = 0
        for i in range(1, 6):
            bmb = bmb+mmomey[i]
        if bmb != 0:
            for i in range(1, 6):
                mpro[i] = mmomey[i]/bmb

        a = 0
        mom = mmomey[0]/3
        Betmoney = float(amount)
        seamount = str(abs(float(amount)))
        if a == 0:
            if mom >= Betmoney:
                NiuNiuCalBetOk(gid, nb, PBLData, bid, 0, seamount)
                NiuNiuCalBetOk(gid, nb, PBLData, bid, 1, seamount)
                mom = mom-Betmoney
            else:
                if mom != 0:
                    NiuNiuCalBetOk(gid, nb, PBLData, bid, 0, seamount)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid, 1, mom)
                    ppm = float(seamount)-mom
                    pmr1 = mpro[1]*ppm
                    pmr2 = mpro[2]*ppm
                    pmr3 = mpro[3]*ppm
                    pmr4 = mpro[4]*ppm
                    pmr5 = mpro[5]*ppm
                    NiuNiuCalBetOk(gid, nb, PBLData, bid1, 2, pmr1)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid2, 3, pmr2)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid3, 4, pmr3)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid4, 5, pmr4)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid4, 6, pmr5)
                    a = 1
                else:
                    ppm = float(seamount)
                    pmr1 = mpro[1]*ppm
                    pmr2 = mpro[2]*ppm
                    pmr3 = mpro[3]*ppm
                    pmr4 = mpro[4]*ppm
                    pmr5 = mpro[5]*ppm
                    NiuNiuCalBetOk(gid, nb, PBLData, bid, 0, seamount)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid1, 2, pmr1)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid2, 3, pmr2)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid3, 4, pmr3)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid4, 5, pmr4)
                    NiuNiuCalBetOk(gid, nb, PBLData, bid4, 6, pmr5)
                    a = 1
        else:
            ppm = float(seamount)
            pmr1 = mpro[1]*ppm
            pmr2 = mpro[2]*ppm
            pmr3 = mpro[3]*ppm
            pmr4 = mpro[4]*ppm
            pmr5 = mpro[5]*ppm
            NiuNiuCalBetOk(gid, nb, PBLData, bid, 0, seamount)
            NiuNiuCalBetOk(gid, nb, PBLData, bid1, 2, pmr1)
            NiuNiuCalBetOk(gid, nb, PBLData, bid2, 3, pmr2)
            NiuNiuCalBetOk(gid, nb, PBLData, bid3, 4, pmr3)
            NiuNiuCalBetOk(gid, nb, PBLData, bid4, 5, pmr4)
            NiuNiuCalBetOk(gid, nb, PBLData, bid4, 6, pmr5)

        cause = '8'
        # 玩家變動後金額
        aoccu = round(float(PBLData.BetOkMy), 2)  # 變動後金額
        uacc.sum_amt = str(round(float(uacc.sum_amt)+aoccu, 2))  # 變動後金額
        uacc.save()
        # 新增玩家變動後金額錢包紀錄
        if aoccu != 0:
            user = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.LId), Cause=cause, Amt_In='0', Amt_Out=str(aoccu), Amt_All=uacc.sum_amt, Create_Time=gettime())
            user.save()
        # 莊家變動後金額
        aoccb = round(float(PBLData.BetOkMM), 2)
        bma.sum_amt = str(round(float(bma.sum_amt)+aoccb, 2))  # 變動後金額
        bma.save()
        # 變動莊家 新增莊家錢包紀錄
        cause = '8'
        if aoccb != 0:
            bm = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId), Cause=cause, Amt_In=str(aoccb), Amt_Out='0', Amt_All=bma.sum_amt, Create_Time=gettime())
            bm.save()

        # 配莊1變動後金額
        aoccb1 = round(float(PBLData.BetOk1MM), 2)
        bma1.sum_amt = str(round(float(bma1.sum_amt)+aoccb1, 2))  # 變動後金額
        bma1.save()
        # 變動配莊1 新增配莊1錢包紀錄
        cause = '8'
        if aoccb1 != 0:
            bm1 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId1), Cause=cause, Amt_In=str(aoccb1), Amt_Out='0', Amt_All=bma1.sum_amt, Create_Time=gettime())
            bm1.save()

        # 配莊2變動後金額
        aoccb2 = round(float(PBLData.BetOk2MM), 2)
        bma2.sum_amt = str(round(float(bma2.sum_amt)+aoccb2, 2))  # 變動後金額
        bma2.save()
        # 變動配莊2 新增配莊2錢包紀錄
        cause = '8'
        if aoccb2 != 0:
            bm2 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId2), Cause=cause, Amt_In=str(aoccb2), Amt_Out='0', Amt_All=bma2.sum_amt, Create_Time=gettime())
            bm2.save()

        # 配莊3變動後金額
        aoccb3 = round(float(PBLData.BetOk3MM), 2)
        bma3.sum_amt = str(round(float(bma3.sum_amt)+aoccb3, 2))  # 變動後金額
        bma3.save()
        # 變動配莊3 新增配莊3錢包紀錄
        cause = '8'
        if aoccb3 != 0:
            bm3 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId3), Cause=cause, Amt_In=str(aoccb3), Amt_Out='0', Amt_All=bma3.sum_amt, Create_Time=gettime())
            bm3.save()

        # 配莊4變動後金額
        aoccb4 = round(float(PBLData.BetOk4MM), 2)
        bma4.sum_amt = str(round(float(bma4.sum_amt)+aoccb4, 2))  # 變動後金額
        bma4.save()
        # 變動配莊4 新增配莊4錢包紀錄
        cause = '8'
        if aoccb4 != 0:
            bm4 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId4), Cause=cause, Amt_In=str(aoccb4), Amt_Out='0', Amt_All=bma4.sum_amt, Create_Time=gettime())
            bm4.save()

        # 配莊5變動後金額
        aoccb5 = round(float(PBLData.BetOk5MM), 2)
        bma5.sum_amt = str(round(float(bma5.sum_amt)+aoccb5, 2))  # 變動後金額
        bma5.save()
        # 變動配莊5 新增配莊5錢包紀錄
        cause = '8'
        if aoccb5 != 0:
            bm5 = BetList(GroupId=gid, Tid='0', Corp_Id=str(Corp_Id), Cnumber=nb, User_Id=str(
                PBLData.BId5), Cause=cause, Amt_In=str(aoccb5), Amt_Out='0', Amt_All=bma5.sum_amt, Create_Time=gettime())
            bm5.save()

        result = {
            "success": "true",
            "result": "已修改",
        }
        response = HttpResponse(json.dumps(
            result, ensure_ascii=False), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    else:
        result = {
            "success": "false",
            "error_msg": "不是用POST傳訊息",
        }
        response = HttpResponse(json.dumps(
            result, ensure_ascii=False), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
