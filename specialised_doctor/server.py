from flask import Flask, render_template
import jinja2
import pymongo 
client = pymongo.MongoClient("mongodb+srv://shruti:0208@hackurmom.b9mgca6.mongodb.net/?retryWrites=true&w=majority")
mydb = client["Remote_ICU"]
mycol = mydb["Patients"]
app = Flask(__name__)

@app.route('/')
def index():
    x = mycol.find_one()
    mycol.delete_one(x)
    # print(x)
    return render_template('index.html',x=x)
@app.route('/Low/')
def func():
    return render_template('Low.html')
@app.route('/Med/')
def func2():
    return render_template('Med.html')
@app.route('/High/')
def func3():
    return render_template('highout.html')
@app.route('/lowout/')
def func4():
    return render_template('lowout.html')
@app.route('/medout/')
def func5():
    return render_template('medout.html')
if __name__ == '__main__':
  app.run(debug=True)
