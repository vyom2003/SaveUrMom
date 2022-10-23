from crypt import methods
from flask import Flask, render_template, request
# import jinja2
import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://shruti:0208@hackurmom.b9mgca6.mongodb.net/?retryWrites=true&w=majority")
mydb = client["Remote_ICU"]
mycol = mydb["Patients"]

app = Flask(__name__)


@app.route("/sign_up",methods=['POST','GET'])
def push():
    name = request.form.get('name')
    phone = request.form.get('phone')
    blood_grp = request.form.get('blood_group')
    gender = request.form.get('genders')
    desc = request.form.get('description')
    address = request.form.get('address')
    data = {
        "name": name,
        "phone_no": phone,
        "blood_group": blood_grp,
        "gender": gender,
        "description": desc,
        "address":address,
    }
    print(data)
    x = mycol.insert_one(data)
    return render_template('signup_success.html')

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
