from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

GOOGLE_API_KEY=os.getenv("AIzaSyBuDNqmup_nZ9GIY9BG1P2kFDvFv_MGbS0")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        responce_raw=chat.send_message(user_input)
        print(responce_raw)
        responce = responce_raw.text
        return jsonify({"response": responce})

    except Exception as e:
        print(f"Error:{e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)









 



