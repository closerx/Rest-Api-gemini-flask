from flask import Flask, jsonify, request
import google.generativeai as genai

app = Flask(__name__)

def myAi(text):
    genai.configure(api_key="AIzaSyCDa2GiUWGd8FA47UAZhw_1zWKTGsMAefA")
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(text)
    return jsonify({
        'status': 'success',
        "data": response.text
    }), 200

@app.route('/', methods=['GET'])
def process_query():
    mytext = request.args.get('text')
    
    if not mytext:  # If no text parameter is provided
        return jsonify({
            'status': 'error',
            'message': 'Missing text query parameter'
        }), 400
    
    print('\033[92m' + mytext + "\033[00m")
    return myAi(mytext)

if __name__ == '__main__':
    app.run()
