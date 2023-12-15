#此程式為製作學生資料表，僅需要在執行主程式前執行一次建立資料表

import mysql.connector
from mysql.connector import Error
#from faker import Faker
#fake = Faker(['Zh_TW'])
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

        cmd = "CREATE TABLE IF NOT EXISTS test" \
              "(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
              "name VARCHAR(50) NOT NULL," \
              "studentnum  VARCHAR(80) NOT NULL," \
              "account  VARCHAR(30) NOT NULL UNIQUE," \
              "password  VARCHAR(15) NOT NULL UNIQUE);"
        cursor.execute(cmd)

        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('吳育安', '50833132', '50833132', '50833132');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('聶士翔', '50933101', '50933101', '50933101');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('黃晨光', '50933102', '50933102', '50933102');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('黃耀宗', '50933103', '50933103', '50933103');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('林柏佑', '50933104', '50933104', '50933104');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('廖偉宸', '50933105', '50933105', '50933105');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('張家翰', '50933106', '50933106', '50933106');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('李昀澍', '50933107', '50933107', '50933107');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('林鼎勛', '50933108', '50933108', '50933108');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('盧子齊', '50933109', '50933109', '50933109');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('劉子誠', '50933110', '50933110', '50933110');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('沈郁凱', '50933112', '50933112', '50933112');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('張凱勛', '50933113', '50933113', '50933113');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('曾聖允', '50933114', '50933114', '50933114');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('謝葆庭', '50933115', '50933115', '50933115');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('丁彥宇', '50933116', '50933116', '50933116');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('盧宥愷', '50933117', '50933117', '50933117');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('陳翊嘉', '50933118', '50933118', '50933118');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('楊展銘', '50933119', '50933119', '50933119');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('葉乃倫', '50933120', '50933120', '50933120');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('李侑霖', '50933121', '50933121', '50933121');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('詹家愷', '50933122', '50933122', '50933122');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('鄭光佑', '50933123', '50933123', '50933123');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('鍾偉倫', '50933124', '50933124', '50933124');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('陳宥廷', '50933125', '50933125', '50933125');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('侯博翔', '50933126', '50933126', '50933126');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('謝士中', '50933127', '50933127', '50933127');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('陳堃誠', '50933128', '50933128', '50933128');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('廖子銓', '50933129', '50933129', '50933129');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('徐維謙', '50933130', '50933130', '50933130');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('陳雍天', '50933131', '50933131', '50933131');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('陳雍元', '50933132', '50933132', '50933132');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('廖彥翔', '50933133', '50933133', '50933133');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('林偉賢', '50933134', '50933134', '50933134');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('程敬惠', '50933135', '50933135', '50933135');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('黃元柏', '50933136', '50933136', '50933136');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('張晉睿', '50933137', '50933137', '50933137');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('許冠昱', '50933138', '50933138', '50933138');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('蘇丞湟', '50933139', '50933139', '50933139');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('廖珮羽', '50933140', '50933140', '50933140');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('何彥慶', '50933141', '50933141', '50933141');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('徐如寶', '50933142', '50933142', '50933142');"
        cursor.execute(cmd)
        cmd = "INSERT INTO test (name, studentnum, account, password) VALUES ('測試用', '0123', '0123', '0123');"
        cursor.execute(cmd)
        
        cursor.execute('SELECT * FROM test')
        print('cursor.rowcount', cursor.rowcount)
        print('cursor.description', cursor.description)
        data = cursor.fetchall()
        for row in data:
            print(row)
except Error as e:
    print("資料庫連接失敗：", e)
finally:
    if (connection.is_connected()):
        connection.commit()
        #connection.rollback()
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")
