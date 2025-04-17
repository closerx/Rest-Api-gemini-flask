from flask import Flask,jsonify,request

import google.generativeai as genai
import os

app=Flask(__name__)
def myAi(text):
	genai.configure(api_key="AIzaSyCDa2GiUWGd8FA47UAZhw_1zWKTGsMAefA")
	model = genai.GenerativeModel(model_name='gemini-1.5-flash')
	response = model.generate_content(text)
	return jsonify({
            'status': 'success',
            "data": response.text
        }), 200
	
@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == "GET":
        return """
          <div class="container">
        <h1>AI Hadi Hakami</h1>
        <form id="aiForm" method="POST">
            <textarea id="prompt" name="text" placeholder="اكتب طلبك هنا" required></textarea>
            <button type="submit">إرسال</button>
        </form>
       
        
    </div>
        """
        
              
    if request.method == 'POST':
     mytext = request.form.get('text')
     
     print('\033[92m'+mytext+"\033[00m")
     
     return myAi(mytext)
app.run()
