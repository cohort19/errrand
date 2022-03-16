from crypt import methods
from flask import render_template,request,redirect,flash,make_response,session,url_for
from  personal import rand
import random,string

@rand.route('/payed')
def payed():
        return 'Transaction completed'

@rand.route('/',methods=['GET','POST'])       
def pay():
    if request.method=='GET':
         return render_template('pay.html') 

    else:
         nam=request.form.get('cname')
         mal=request.form.get('mail')
         amnt=request.form.get('amt')
         return render_template('info.html',nam=nam,mal=mal,amnt=amnt)

@rand.route('/success') 
def success():
    return render_template('success.html')  

 
                  






  
           