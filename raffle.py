import pymysql
import pandas as pd 

def get_db_connection():
    return pymysql.connect(
        host='systemmanagement.mysql.database.azure.com',
        user='minseok',
        password='seok9745@@',
        db='project',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        ssl={'ca': "./DigiCertGlobalRootCA.crt.pem"},
        ssl_disabled=False
    )


conn = get_db_connection()
cursor = conn.cursor()


cursor.execute("SELECT name, phone, similardepartment FROM input")
output_df = cursor.fetchall()
output_df = pd.DataFrame(output_df)

output_df.dropna(subset=['phone'], inplace=True)
output_df.drop_duplicates(subset=['phone'], inplace=True)

systemmanagement_df = output_df.loc[output_df['similardepartment'] == "시스템경영공학과"]

random_for_starbucks = output_df.sample(n=10)
random_for_charger = systemmanagement_df.sample(n=5)

print(random_for_starbucks)
print(random_for_charger)