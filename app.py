import pymysql
import department, information, SME
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


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



#첫 화면
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        phonenumber = request.form.get('phonenumber')

        physics_user = int(request.form.get('physics'))
        code_user = int(request.form.get('code'))
        team_user = int(request.form.get('team'))
        optimization_user = int(request.form.get('optimization'))
        
    
        conn = get_db_connection()
        cursor = conn.cursor()


        cursor.execute("SELECT physics, code, team, optimization, department FROM department_new")
        department_df = cursor.fetchall()
        selected_department = None 
        selected_department = department.department(department_df, physics_user, code_user, team_user, optimization_user)

        

        #chatgpt 
        gpt =''
        gpt = information.major(selected_department)

        SME_text = SME.department_text(username, selected_department)
        #DB 저장 
        query = """INSERT INTO input (name, phone, similardepartment) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (username, phonenumber, selected_department))

        dic = {"건설환경공학부":"CEE", "기계공학부":"ME", 
            "나노공학과": "NE", "시스템경영공학과":"SME1",
            "화학공학&고분자공학부":"CE", "신소재공학부":"AMSE"}
        selected_department_English = dic[selected_department]

        conn.commit()
        cursor.close()
        conn.close()

        return render_template("result.html",
                       selected_department = selected_department , gpt= gpt, SME_text = SME_text, selected_department_English = selected_department_English)
    
    return render_template('index.html')


@app.route("/result", methods=["POST"])
def result():
    selected_department  = request.args.get('selected_department', default="", type=str)
    selected_department_English  = request.args.get('selected_department_English', default="", type=str)
    gpt = request.args.get('gpt', default="", type=str)
    SME_text = request.args.get('SME_text', default="", type=str)



    return render_template("result.html", selected_department  = selected_department , gpt = gpt, SME_text = SME_text, selected_department_English = selected_department_English)


if __name__ == "__main__":
    app.run(debug=True)

