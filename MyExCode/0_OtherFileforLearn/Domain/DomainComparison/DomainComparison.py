import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 將目前工作目錄設定為指令搞所在目錄
DomainComparison1_file = 'A.txt'  # 設定要開啟的檔案
DomainComparison2_file = 'B.txt'
if os.path.exists(DomainComparison1_file) == False:
    newfile = open('A.txt', 'w')
    newfile.close()
if os.path.exists(DomainComparison2_file) == False:
    newfile = open('B.txt', 'w')
    newfile.close()

with open(DomainComparison1_file, encoding='utf-8-sig') as file_Obj:
    # splitlines() 可消除line中\n的方法
    DomainsComparison1 = set(file_Obj.read().splitlines())
with open(DomainComparison2_file, encoding='utf-8-sig') as file_Obj:
    DomainsComparison2 = set(file_Obj.read().splitlines())

DomainisinA = DomainsComparison1 - DomainsComparison2
DomainisinB = DomainsComparison2 - DomainsComparison1
with open('Reasult.txt', 'w', encoding='utf-8-sig') as file_Obj:
    file_Obj.write("A有B沒有:\n")
    for line in DomainisinA:
        file_Obj.write('%s\n' % line)
    file_Obj.write("B有A沒有:\n")
    for line in DomainisinB:
        file_Obj.write('%s\n' % line)
