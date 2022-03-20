name_list = ['Mary', 'Josh', 'Tracy']
print('目前名單：', name_list)
num_flog = int(input('輸入1：增加名單\n輸入2：刪除名單\n請輸入數字：'))
if num_flog == 1:
    new_name = input("請輸入需新增名單：")
    name_list.append(new_name)
    print('目前名單：', name_list)
elif num_flog == 2:
    new_name = input("請輸入需移除名單：")
    if new_name in name_list:
        name_list.remove(new_name)
        print('目前名單：', name_list)
    else:
        print('名單輸入錯誤')
        print('目前名單：', name_list)
