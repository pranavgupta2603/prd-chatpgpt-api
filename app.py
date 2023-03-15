from flask import Flask, render_template, request, jsonify
from chat import chat
import openai

openai.api_key = 'your-openai-key'
message_history = []
"""
app = Flask(__name__)

@app.route("/")
def hello():
    user_input = input("> ")
    print("User's input was: ", user_input)
    return (chat(user_input, message_history))
from flask import Flask, render_template, request
"""
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product_name = request.form['question1']
        feature_name = request.form['question2']
        overview = request.form['question3']
        user_input = "My product is called " + product_name +". Write a PRD of a feature " + feature_name +"for my product. An overview for the feature is: " + overview
        print(message_history)
        gpt_resp = chat(user_input, message_history)
        #splitted_gpt_resp = gpt_resp.split('\n')
        #   print(splitted_gpt_resp)
        resp = jsonify({'output': gpt_resp})
        #for i in splitted_gpt_resp:
            #resp = jsonify({'output': i})
        return resp
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)
