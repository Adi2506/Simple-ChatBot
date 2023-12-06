from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Define a function to interact with the GPT-3 model
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['user_input']
    bot_response = chat_with_bot("User: " + user_input + "\n\bBot:")
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
