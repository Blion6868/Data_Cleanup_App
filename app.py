#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    file_1 = request.files['file1']
    file_2 = request.files['file2']
    file_1.save(os.path.join(app.config['UPLOAD_FOLDER'], file_1.filename))
    file_2.save(os.path.join(app.config['UPLOAD_FOLDER'], file_2.filename))

    file_1_path = os.path.join(app.config['UPLOAD_FOLDER'], file_1.filename)
    file_2_path = os.path.join(app.config['UPLOAD_FOLDER'], file_2.filename)

    file_1_data = pd.read_excel(file_1_path)
    file_2_data = pd.read_excel(file_2_path)

    left_on = request.form['left_on']
    right_on = request.form['right_on']
    how = request.form['how']

    df = pd.merge(left=file_1_data, right=file_2_data, left_on=left_on, right_on=right_on, how=how)
    merged_file_path = './uploads/merged.csv'
    df.to_csv(merged_file_path, index=False)

    return merged_file_path

if __name__ == '__main__':
    app.run(debug=True)

