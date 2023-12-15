# Rollcall_System_zh-TW
此為中文版本結合SQL的點名系統，專為學校或教育機構設計，以協助老師進行學生點名。  
系統分為學生和教師兩個入口，每個入口都提供了相應的功能和選項。

## 入口說明  
- **學生入口**  
	- 修改帳號和密碼  
	- 進行線上點名  
	- 登出系統

- **教師入口**  
	- 查詢班級所有學生的資料
	- 查詢個別學生的資料
	- 修改學生資料
	- 刪除學生帳號
	- 新增學生帳號
	- 修改帳號密碼
	- 顯示尚未完成點名之學生名條
	- 將所有學生設置為尚未點名狀態
	- 設定點名密碼

## 如何使用  
### 1.安裝相關套件
```
#在終端機中執行以下命令
pip install mysql-connector-python
```

### 2.創建資料庫
- 請使用提供的 MySQL 資料庫相關資訊，手動創建資料庫 mydb。

### 3.執行主程式
```
#在終端機中執行主程式
python 主程式檔案名稱.py
```

### 4.選擇身分
- 根據提示，選擇您的身分（學生或教師）並依指示操作。

### 5.使用系統
- 根據功能特點中的描述，使用相應的功能選項進行操作。

## 注意事項
1. 當出現 1062 (23000): Duplicate entry 錯誤時，請重新執行程式，確保新帳號的唯一性。