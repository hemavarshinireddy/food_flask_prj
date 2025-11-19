from flask import Flask,render_template,request
app = Flask(__name__)
#import sqlite3 as sql
@app.route('/',methods=['GET','POST'])
def home():
    #if request.method=='GET':
        return render_template('home.html')
        pass
@app.route('/details',methods=['GET','POST'])        
def details():
    #if request.method=='GET':
        return render_template('details.html')
@app.route('/menu',methods=['GET','POST'])        
def menu():
    #if request.method=='GET':
        return render_template('menu.html')
item_price={
       "Dosa":50,
       "Idly":50,
       "Noodles":70,
       "Fried Rice":70,
       "veg biriyani":80,
       "mushroom biriyani":100,
       "kabab":100,
       "chilli chicken":110,
       "Chicken Lollipop":120,
       "Chicken Biriyani":150,
       "Egg Fried Rice":120,
       "Mutton Biriyani":180
       }    
@app.route('/billgenerate',methods=['GET','POST'])        
def billgenerate():
    selected=[]
    total=0
    if request.method=='POST':
        selected=request.form.getlist('item')
        total=sum(item_price[item] for item in selected)
        return render_template('billgenerate.html',items=item_price,selected=selected,total=total)
if __name__=='__main__':
    app.run(debug=True)    