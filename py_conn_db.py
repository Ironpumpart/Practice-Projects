import pymysql

try:
    print("Connecting...")
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='#######',
        database='school',
        port=3306,
        connect_timeout=5
    )
    print("Connected!")
except Exception as e:
    print("Error:", e)
cursor = conn.cursor()
cursor.execute("SELECT * FROM class")
results = cursor.fetchall()
print("Script is running...")
for row in results:
    print(row)
cursor.close()
conn.close()