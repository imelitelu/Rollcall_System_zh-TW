#此程式為製作教師端資料表，僅需要在執行主程式前執行一次建立資料表

import mysql.connector
from mysql.connector import Error
from faker import Faker
fake = Faker(['Zh_TW'])
try:
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='mydb',           # 資料庫名稱
        user='root',               # 帳號
        password='lu0418')           # 密碼
    if connection.is_connected():
        #connection.autocommit = True
        print("資料庫版本：", connection.get_server_info())
        cursor = connection.cursor()

        cmd = "CREATE TABLE IF NOT EXISTS testteacher" \
              "(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
              "name VARCHAR(50) NOT NULL," \
              "teacherid  VARCHAR(10) NOT NULL," \
              "account  VARCHAR(30) NOT NULL UNIQUE," \
              "password  VARCHAR(15) NOT NULL UNIQUE);"
        cursor.execute(cmd)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00001','00001','00001');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00002','00002','00002');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00003','00003','00003');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00004','00004','00004');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00005','00005','00005');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00006','00006','00006');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00007','00007','00007');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00008','00008','00008');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00009','00009','00009');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00010','00010','00010');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00011','00011','00011');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00012','00012','00012');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00013','00013','00013');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00014','00014','00014');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00015','00015','00015');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00016','00016','00016');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00017','00017','00017');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00018','00018','00018');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00019','00019','00019');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('"+fake.name()+"','00020','00020','00020');"
        cursor.execute(sql)
        sql = "INSERT INTO testteacher (name, teacherid, account, password ) VALUES ('測試用','0123','0123','0123');"
        cursor.execute(sql)

        cursor.execute('SELECT * FROM test')
        print('cursor.rowcount', cursor.rowcount)
        print('cursor.description', cursor.description)
        data = cursor.fetchall()
        for row in data:
            print(row)
except Error as e:
    print("資料庫連接失敗：", e)
    connection.rollback()  # 回滾
finally:
    if (connection.is_connected()):
        connection.commit()
        #connection.rollback()
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")
