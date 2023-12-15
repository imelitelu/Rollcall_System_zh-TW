'''
學生測試用---名字:測試用 帳號:0123 密碼:0123
教師測試用---名字:測試用 帳號:0123 密碼:0123
'''

import mysql.connector
from mysql.connector import Error

def anyindex(): #主菜單
    print("歡迎蒞臨校用管理系統")
    print("*----------------*")
    print("1.老師")
    print("2.學生")
    print("3.結束程式")

def studentsindex(): #學生菜單
    print()
    print('\x1b['+''+str(91)+'m 學生端系統\x1b[m')
    print("請選擇您要做的項目")
    print("*-------------*")
    print("1.修改帳號密碼")
    print("2.線上點名")
    print("3.登出系統，並退回主選單")
    print("4.結束程式")

def teacherindex(): #教師菜單
    print()
    print('\x1b['+''+str(91)+'m 教師端系統\x1b[m')
    print("請選擇您要做的項目")
    print("*-------------*")
    print("1.查詢班級所有學生的資料")
    print("11.查詢個別學生的資料")
    print("2.修改學生資料")
    print("3.刪除學生帳號")
    print("4.新增學生的帳號")
    print("5.修改帳號密碼")
    print("6.顯示出尚未完成點名之學生名條")
    print("7.將所有學生設置成尚未點名狀態")
    print("8.設定點名密碼(還在建構中，無法使用)")
    print("9.退回教師菜單")
    print("10.結束程式")

def stu_accpwdindex(): #學生更改帳號密碼菜單
    print()
    print("這裡是學生端更改帳號密碼")
    print("請選擇您要做的項目")
    print("*-------------*")
    print("1.更改帳號")
    print("2.更改密碼")
    print("3.離開此操作頁面(將退回學生端主選單)")

def tch_accpwdindex(): #教師更改帳號密碼菜單
    print()
    print("這裡是教師端更改帳號密碼")
    print("請選擇您要做的項目")
    print("*-------------*")
    print("1.更改帳號")
    print("2.更改密碼")
    print("3.離開此操作頁面(將退回教師端主選單)")

def tch_stu_accpwdindex(): #教師維護學生帳號密碼菜單
    print()
    print("此為教師維護學生帳號密碼")
    print("請輸入您要做的項目")
    print("*-------------*")
    print("1.修改學生帳號")
    print("2.修改學生密碼")
    print("3.退回教師菜單")
    print("4.結束系統")

def studentslogin(): #學生登入
    while True:
        global stuid #v1.1.0
        #global stuacc #v1.1.0
        global stuname #v1.1.0
        #global stupwd #v1.1.0
        stutryacc = input("請輸入帳號")
        if stutryacc == "": break
        sql_1 = "SELECT name, studentnum, account,password FROM test WHERE account ='" + stutryacc + "'"
        cursor.execute(sql_1)
        stu_data = cursor.fetchone()
        # print(staff_acc)#顯示出使用者名稱, 帳號, 密碼(非測試時請註解)
        if (stu_data == None):
            print("{}帳號不存在".format(stutryacc))
            continue
        mypwd = stu_data[3]
        # print(mypwd)#顯示使用者密碼(非測試時請註解)
        stutrypwd = input("請輸入密碼")
        if stutrypwd == "": break
        if (mypwd != stutrypwd):
            print("密碼錯誤")
            continue
        else:
            print()
            print("登入成功")
            print()
            staff_name = stu_data[0] #v1.0.1
            print("歡迎", staff_name, "同學登入")
            stuname = stu_data[0] #v1.1.0
            stuid = stu_data[1] #v1.1.0
            stupwd = stu_data[3] #v1.1.0
            stuacc = stu_data[2]
            studentsmenu()
            break

def teacherlogin(): #教師登入
    while True:
        global tchid #v1.1.0
        #global tchacc #v1.1.0
        global tchname #v1.1.0
        #global tchpwd #v1.1.0
        tchtryacc = input("請輸入帳號")
        if tchtryacc == "": break
        sql_1 = "SELECT name, teacherid, account, password FROM testteacher WHERE account ='" + tchtryacc + "'"
        cursor.execute(sql_1)
        tch_data = cursor.fetchone()
        # print(tch_data)#顯示出使用者名稱, 帳號, 密碼(非測試時請註解)
        if (tch_data == None):
            print("{}帳號不存在".format(tchtryacc))
            continue
        mypwd = tch_data[3]
        # print(mypwd)#顯示使用者密碼(非測試時請註解)
        tchtrypwd = input("請輸入密碼")
        if tchtrypwd == "": break
        if (mypwd != tchtrypwd):
            print("密碼錯誤")
            continue
        else:
            print()
            print("登入成功")
            print()
            staff_name = tch_data[0] #v1.0.1
            print("歡迎", staff_name, "教師登入")
            tchid = tch_data[1] #v1.1.0
            tchacc = tch_data[2] #v1.1.0
            tchname = tch_data[0] #v1.1.0
            tchpwd = tch_data[3] #v1.1.0
            teachersmenu()
            break

def studentsRC(): #學生點名
    while True:
        print()
        rcpwd = input("請輸入此課程點名密碼")
        trytchname = input("請輸入任教該課教師名稱")
        sql_1 = "SELECT name, teacherid, account, password, rollcallpwd FROM testteacher WHERE name ='" + trytchname + "'"
        cursor.execute(sql_1)
        tch_data = cursor.fetchone()
        tchrcname = tch_data[0]
        tchrcpwd = tch_data[3]
        if rcpwd == "": break
        if tchrcpwd == rcpwd:
            sql_2 = "UPDATE test SET rollcall = 1  WHERE studentnum ='" + stuid + "'"
            cursor.execute(sql_2)
            print()
            print("點名成功")
            print()
            studentsmenu()
        else:
            print("密碼錯誤請重新輸入")
            continue

def tch_stu_RCcheck(): #教師點名確認
    sql = "SELECT name, studentnum FROM test WHERE rollcall = '0'"
    cursor.execute(sql)
    sturc = cursor.fetchall()
    print()
    print("總人數:", cursor.rowcount, "人")
    for row in sturc:
        print(row)

def stu_accch(): #學生更改帳號
    while True:
        #global stuacc
        print()
        print()
        new_acc = input("請輸入您的新帳號")
        new2_acc = input("請再次確認您的新帳號")
        if new_acc == new2_acc:
            sql = "SELECT account FROM test"
            cursor.execute(sql)
            acc_data = cursor.fetchall()
            account = acc_data[0]  
            print (acc_data)
            if acc_data == new2_acc:
                print("您新註冊的帳號已經被註冊過，請輸入其他的")
                break
            else:
                sql_1 = "UPDATE test SET account = '" + new_acc +"' WHERE studentnum ='" + stuid + "'"
                cursor.execute(sql_1)
                #print(sql_1)
                print("修改成功")
                print()
                studentsmenu()
                break  
        else:
            print("您兩次輸入的帳號不一樣，請重新輸入")
            continue

def stu_pwdch(): #學生更改密碼
    while True:
        #global stupwd #v1.1.0
        print()
        print()
        new_pwd = input("請輸入您的新密碼")
        new2_pwd = input("請再次確認您的新密碼")
        if new_pwd == new2_pwd:
            sql_1 = "UPDATE test SET password = '" + new_pwd +"' WHERE studentnum ='" + stuid + "'"
            cursor.execute(sql_1)
            #print(sql_1)
            print("修改成功")
            print()
            studentsmenu()
            break  
        else:
            print("您輸入的密碼不一樣，請重新輸入")
            continue

def stu_accpwdch(): #學生更改帳號密碼介面
    while True:
        stu_accpwdindex()
        num = int(input("請輸入您執行的項目:"))
        if num == 1:
            stu_accch()
            break
        elif num == 2:
            stu_pwdch()
        elif num == 3:
            studentsmenu()
        else:
            print("輸入指令錯誤，請重新輸入")

def get_stu_info(): #教師獲取班級學生名條
    print()
    print("此系統模式將會列印出該班級學生之姓名學號")
    print("請選擇要的模式")
    print("1.僅列出姓名，學號")
    print("2.列出姓名，學號，帳號")
    print("3.列出姓名，學號，帳號，密碼")
    num = int(input("請輸入操作動作"))
    if num == 1:
        sql = "SELECT name, studentnum FROM test"
        cursor.execute(sql)
        stu_data = cursor.fetchall()
        print()
        print("總人數:", cursor.rowcount, "人")
        for row in stu_data:
            print(row)
    elif num == 2:
        sql_1 = "SELECT name, studentnum, account FROM test"
        cursor.execute(sql_1)
        stu_data = cursor.fetchall()
        print()
        print("總人數:", cursor.rowcount, "人")
        for row in stu_data:
            print(row)
    elif num == 3:
        sql_2 = "SELECT name, studentnum, account FROM test"
        cursor.execute(sql_2)
        stu_data = cursor.fetchall()
        print()
        print("總人數:", cursor.rowcount, "人")
        for row in stu_data:
            print(row)
    else:
        print("輸入錯誤，請重新輸入")

def get_stu_info_one(): #教師獲取個別學生名條
    choose=input("請輸入您要搜尋的欄位 1. 姓名 2. 學號")
    if(choose=='1'):
        name=input("請輸入姓名:")
        sql_1="SELECT name, studentnum, account, password FROM test WHERE name ='" + name + "'"

    else:
        studentnum=input("請輸學號:")
        sql_1="SELECT name, studentnum, account, password FROM test WHERE studentnum ='" + studentnum + "'"

    cursor.execute(sql_1)
    stu_data= cursor.fetchone()     
    print()
    print("姓名，學號，帳號，密碼")
    return stu_data

def tch_stu_accpwd(): #教師更改學生帳號及密碼介面
    tch_stu_accpwdindex()
    while True:
        num = int(input("請輸入您要執行的動作"))
        if num == "":break
        if num == 1: #修改學生帳號
            tch_stu_acc()
            break
        elif num == 2: #修改學生密碼
            tch_stu_pwd()
            break
        elif num == 3:    
            teachersmenu()
            break
        elif num == 4:
            exit()

def tch_stu_pwd(): #教師更改學生密碼
    while True:
        acc = input("請輸入帳號")
        if acc == "": break
        sql_1 = "SELECT name, account,password FROM test WHERE account ='" + acc + "'"
        cursor.execute(sql_1)
        staff_acc = cursor.fetchone()
        #print(staff_acc) #顯示出使用者名稱, 帳號, 密碼(非測試時請註解)
        if (staff_acc == None):
            print("{}帳號不存在".format(acc))
            continue
        mypwd = staff_acc[2]
        #print(mypwd) #顯示使用者密碼(非測試時請註解)
        pwd = input("請輸入密碼")
        if pwd == "": break
        if (mypwd != pwd):
            print("密碼錯誤")
            continue
        else:
            print()
            print()
            new_pwd = input("請輸入您學生的新密碼")
            new2_pwd = input("請再次確認您學生的新密碼")
            if new_pwd == new2_pwd:
                sql_1 = "UPDATE test SET password = '" + new_pwd +"' WHERE account ='" + acc + "'"
                cursor.execute(sql_1)
                #print(sql_1) #測試用，非測試時請勿開起
                print("密碼修改成功")
                print()
                teachersmenu()
                break  
            else:
                print("您兩次輸入密碼的不一樣，請重新輸入")
                continue

def tch_stu_acc(): #教師更改學生帳號
    while True:
        acc = input("請輸入帳號")
        if acc == "": break
        sql_1 = "SELECT name, account,password FROM test WHERE account ='" + acc + "'"
        cursor.execute(sql_1)
        staff_acc = cursor.fetchone()
        #print(staff_acc) #顯示出使用者名稱, 帳號, 密碼(非測試時請註解)
        if (staff_acc == None):
            print("{}帳號不存在".format(acc))
            continue
        mypwd = staff_acc[2]
        #print(mypwd) #顯示使用者密碼(非測試時請註解)
        pwd = input("請輸入密碼")
        if pwd == "": break
        if (mypwd != pwd):
            print("密碼錯誤")
            continue
        else:
            print()
            print()
            new_acc = input("請輸入您學生的新帳號")
            new2_acc = input("請再次確認您學生的新帳號")
            if new_acc == new2_acc:
                sql_1 = "UPDATE test SET account = '" + new_acc +"' WHERE account ='" + acc + "'"
                cursor.execute(sql_1)
                #print(sql_1) #測試用，非測試時請勿開起
                print("帳號修改成功")
                print()
                teachersmenu()
                break  
            else:
                print("您兩次輸入帳號的不一樣，請重新輸入")
                continue

def tch_accpwdch(): #教師更改帳號密碼介面
        while True:
            tch_accpwdindex()
            num = int(input("請輸入您執行的項目:"))
            if num == 1:
                tch_accch()
                break
            elif num == 2:
                tch_pwdch()
            elif num == 3:
                studentsmenu()
            else:
                print("輸入指令錯誤，請重新輸入")

def tch_accch(): #教師帳號更改
    while True:
        print()
        print()
        new_acc = input("請輸入您的新帳號")
        new2_acc = input("請再次確認您的新帳號")
        if new_acc == new2_acc:
            sql_1 = "UPDATE testteacher SET account = '" + new_acc +"' WHERE teacherid ='" + tchid + "'"
            cursor.execute(sql_1)
            #print(sql_1)
            print("修改成功")
            print()
            teachersmenu()
            break  
        else:
            print("您輸入的不一樣，請重新輸入")
            continue

def tch_pwdch(): #教師密碼更改
    while True:
        print()
        print()
        new_pwd = input("請輸入您的新密碼")
        new2_pwd = input("請再次確認您的新密碼")
        if new_pwd == new2_pwd:
            sql_1 = "UPDATE testteacher SET password = '" + new_pwd +"' WHERE teacherid ='" +tchid + "'"
            cursor.execute(sql_1)
            #print(sql_1)
            print("修改成功")
            print()
            teachersmenu()
            break  
        else:
            print("您輸入的密碼不一樣，請重新輸入")
            continue

def delstuacc(): #刪除學生帳號
    print()
    print('\x1b['+''+str(91)+'m 此模式為永久刪除學生資料\x1b[m')
    print("為防止誤觸，請您打出 '繼續' 來進行下一步")
    x = input("請輸入:")
    if x =="繼續":
        print("透過 1.名字 2. 學號 刪除學生資料 ")
        choose=input("請選擇您要從哪個選項刪除帳號的 1. 姓名 2. 學號")
    
    if(choose=='1'):
        name=input("請輸入姓名:")
        sql_1="DELETE FROM test where name = '"+ name + "'" 
        cursor.execute(sql_1)  
        print("帳號刪除成功")

    else:
        studentnum=input("請輸入帳號:")
        sql_1="DELETE FROM test where studentnum = '"+ studentnum + "'"
        cursor.execute(sql_1)  
        print("帳號刪除成功")

def addstuacc(): #噌加學生帳號
    print()
    print("此模式為新增個別學生資料")
    name = input("請輸入新增帳號之名稱")
    stuid = input("請輸入新增學生之學號")
    acc = input("請輸入新增學生之帳號")
    pwd = input("請輸入新增學生之密碼")
    cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('" + name + "','" + stuid + "', '" + acc + "','"+ pwd +"')"
    cursor.execute(cmd)
    print("新增帳號成功")
    print()
    teachersmenu()

def ressutrc(): #重製點名欄位
    sql_1 = "UPDATE test SET rollcall = '0'"
    cursor.execute(sql_1)
    print()
    print("修改成功")

def setrcpwd(): #設定當天點名密碼
    print()
    tchrcpwd = int(input("請輸入當天點名密碼(密碼請以數字組成"))
    sql_1 = "UPDATE testteacher SET rollcallpwd = '" + tchrcpwd +"' WHERE teacherid ='" + tchid + "'" 
    cursor.execute(sql_1)
    teachersmenu()

def studentsmenu(): #學生菜單介面
    while True:
        studentsindex()
        item = int(input("請輸入您執行的動作"))
        if item == 1:
            stu_accpwdch()
        elif item == 2:
            studentsRC()
        elif item == 3:
            print()
            mymenu()
            break
        elif item == 4:
            exit()
        else:
            print("請輸入正確指令")

def teachersmenu(): #教師菜單介面
    while True:
        teacherindex()
        item = input("請輸入您執行的動作")
        if item == "":break
        if item == '1':
            staff_info = get_stu_info();
            print(staff_info)
        elif item == '11':
            info = get_stu_info_one()
            print(info)
        elif item == '2':
            tch_stu_accpwd()
        elif item == '3':
            delstuacc()
        elif item == '4':
            addstuacc()
        elif item == '5':
            tch_accpwdch()
        elif item == '6':
            tch_stu_RCcheck()
        elif item == '7':
            ressutrc()
        elif item == '8':
            setrcpwd()
        elif item == '9':
            break
        elif item == '10':
            exit()

def mymenu(): #主程式
    while True:
        anyindex() #呼叫起始介面
        num = input("請輸入您要執行的動作")
        print()
        if num == "":
            print("未填入任何資料，請重新輸入")
            print()
            continue
        if num == 1 :
            teacherlogin() #呼叫老師登入函式
        elif num == '2' :
            studentslogin() #呼叫學生登入函式
        elif num == '3' :
            exit()#結束程式
        else:
            print("輸入錯誤指令，請重新輸入")
            print()
            continue

try:
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='mydb',           # 資料庫名稱
        user='root',               # 帳號
        password='lu0418')           # 密碼
    if connection.is_connected():
        connection.autocommit = True
        print("資料庫版本：", connection.get_server_info())
        cursor = connection.cursor()
        mymenu()

except Error as e:
    print("資料庫連接失敗：", e)
    print()
    print("若出現 1062 (23000): Duplicate entry '您輸入的新帳號' for key 'account'")
    print("代表您輸入的新帳號跟其他人有重複，請重新執行程式")
    print()
finally:
    if (connection.is_connected()):
        #connection.commit()
        #connection.rollback()
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")