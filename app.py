from flask import Flask, request, jsonify
import requests
import json
import os
from urllib.parse import unquote

app = Flask(__name__)

# استبدل 'YOUR_API_KEY' بمفتاح API الفعلي الخاص بك
api_key = "AIzaSyAYRLj3G-5gMn_m-LbPd-GS0o41R08rG9k"



@app.route('/ask/<path:message>')
def ask_question(message):
    """معالجة الأسئلة مباشرة من URL"""
    try:
        # فك تشفير الرسالة (للمسافات والرموز الخاصة)
        decoded_message = unquote(message)
        
        # رابط API للنموذج
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        # رأس الطلب
        headers = {
            'Content-Type': 'application/json'
        }

        # بيانات الطلب
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": decoded_message
                        }
                    ]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": 150,  # قيمة افتراضية
                "temperature": 0.7
            }
        }

        # إرسال الطلب
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            response_data = response.json()
            try:
                generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
                return jsonify({
                    'question': decoded_message,
                    'answer': generated_text,
                    'status': 'success'
                }), 200, {'Content-Type': 'application/json; charset=utf-8'}
            except (KeyError, IndexError) as e:
                return jsonify({'error': f'خطأ في تحليل الاستجابة: {str(e)}'}), 500
        else:
            return jsonify({'error': f'خطأ في الطلب: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'error': f'خطأ غير متوقع: {str(e)}'}), 500



@app.route('/')
def home():
    return """'<h1>Gemini Flask API</h1>"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
