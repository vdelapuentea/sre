#!/usr/bin/env python
# coding: utf-8



#get_ipython().system('pip install flask_bootstrap')


# In[12]:


from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 
import pandas as pd 
import numpy as np 
import pickle

# In[9]:


modelo  = pickle.load(open("pickle_model.pkl","rb"))


# In[13]:


app = Flask(__name__)
Bootstrap(app)


def form(X):
    #mes,dia,hora,num_sem,orden_dia,año=int(request.form.get("mes")),int(request.form.get("dia")),0,0,0,int(request.form.get("año"))
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36 = int(request.form.get("x0")),int(request.form.get("x1")),int(request.form.get("x2")),int(request.form.get("x3")),int(request.form.get("x4")),int(request.form.get("x5")), int(request.form.get("x6")),int(request.form.get("x7")),int(request.form.get("x8")),int(request.form.get("x9")),int(request.form.get("x10")),int(request.form.get("x11")), int(request.form.get("x12")),int(request.form.get("x13")),int(request.form.get("x14")),int(request.form.get("x15")),int(request.form.get("x16")),int(request.form.get("x17")), int(request.form.get("x18")),int(request.form.get("x19")),int(request.form.get("x20")),int(request.form.get("x21")),int(request.form.get("x22")),int(request.form.get("x23")), int(request.form.get("x24")),int(request.form.get("x25")),int(request.form.get("x26")),int(request.form.get("x27")),int(request.form.get("x28")),int(request.form.get("x29")), int(request.form.get("x30")),int(request.form.get("x31")),int(request.form.get("x32")),int(request.form.get("x33")),int(request.form.get("x34")),int(request.form.get("x35")),int(request.form.get("x36"))
    return x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36

@app.route('/', methods=['GET', 'POST'])
def index(): return render_template('index.html')


@app.route('/Predecir', methods=['POST'])
def Predecir():
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36=form(1)[0],form(1)[1],form(1)[2],form(1)[3],form(1)[4],form(1)[5],form(1)[6],form(1)[7],form(1)[8],form(1)[9],form(1)[10],form(1)[11],form(1)[12],form(1)[13],form(1)[14],form(1)[15],form(1)[16],form(1)[17],form(1)[18],form(1)[19],form(1)[20],form(1)[21],form(1)[22],form(1)[23],form(1)[24],form(1)[25],form(1)[26],form(1)[27],form(1)[28],form(1)[29],form(1)[30],form(1)[31],form(1)[32],form(1)[33],form(1)[34],form(1)[35],form(1)[36]

    if request.method == 'POST':
            my_predictionA_dia = modelo.predict(pd.DataFrame({'x0':[x0],'x1':[x1],'x2':[x2],'x3':[x3],'x4':[x4],'x5':[x5],'x6':[x6],'x7':[x7],'x8':[x8],'x9':[x9],'x10':[x10],'x11':[x11], 'x12':[x12],'x13':[x13],'x14':[x14],'x15':[x15],'x16':[x16],'x17':[x17],'x18':[x18],'x19':[x19],'x20':[x20],'x21':[x21],'x22':[x22],'x23':[x23],'x24':[x24],'x25':[x25],'x26':[x26],'x27':[x27], 'x28':[x28],'x29':[x29],'x30':[x30],'x31':[x31], 'x32':[x32],'x33':[x33],'x34':[x34],'x35':[x35], 'x36':[x36] }))

            return render_template('Predecir.html',my_predictionA_dia=int(my_predictionA_dia)) 	


# In[ ]:


if __name__ == '__main__': app.run(host='0.0.0.0', port=80)

