from flask import Flask,render_template,request,redirect
#from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np
import os


# global laptop
app = Flask(__name__)
# cors = CORS(app)
# model = pickle.load(open('df.pkl','rb'))
# laptop = pd.read_csv('Cleaned_laptop_data.csv')


@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")


# @app.route('/',methods=['GET','POST'])
# def index():
#     global laptop
#     companies = sorted(laptop['Company'].unique())
#     type = sorted(laptop['TypeName'].unique())
#     ram=sorted(laptop['Ram'].unique())
#     screen=laptop['Touchscreen'].unique()
#     ips=laptop['Ips'].unique()
#     ppi=laptop['ppi'].unique()
#     CPU=laptop['Cpu brand'].unique()
#     HDD=laptop['HDD'].unique()
#     SSD=laptop['SSD'].unique()
#     GPU=laptop['Gpu brand'].unique()
#     OS=laptop['os'].unique()
#
#     companies.insert(0,'Select Company')
#     return render_template('index.html',companies=companies, type=type, ram=ram)

if __name__=='__main__':
    app.run(debug=True)
