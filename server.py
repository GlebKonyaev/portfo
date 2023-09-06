from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route("/<string:page_name>")
def name_page(page_name):
    return render_template(page_name)
@app.route("/")
def home_page():
    return render_template('index.html')
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' : 
        try:
         data = request.form.to_dict(['email','subject','message'])
         save_data_csv(data)
         return redirect('/thankyou.html')
        except:
            return "did not save to database!"
    else:
        return "something went wrong!Try again"
def save_data_txt(data):
    with open('./database.txt',mode='a') as databas:
        email = data['email']
        subject = data['subject']
        message = data['message']
        txt_file = databas.write(f'\n email : {email} ; subject : {subject} ; message : {message}')
def save_data_csv(data):
    with open('./database.csv','a',newline = '') as databas2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(databas2,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])




