import pandas as pd
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder='templates')

# Read the CSV data containing prompts and [Our Business] inputs
data = pd.read_csv('prompt-database.csv')

# Set up OpenAI API key
api_key = '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'  # Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = api_key

@app.route('/')  # This is the endpoint for the root URL
def index():
    return render_template('index.html')

@app.route('/get_responses', methods=['POST'])
def get_responses():
    our_business_input = request.json.get('our_business_input')

    responses = []

    # Loop through prompts and [Our Business] inputs
    for index, row in data.iterrows():
        prompt = row['Prompt to run']
        prompt_with_input = prompt.replace('[User’s input here]', our_business_input)

        # Send prompt to ChatGPT and get the response using the new OpenAI interface
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=prompt_with_input,
        max_tokens=150
    )   
        # Process and append the response
    responses.append(response['choices'][0]['text'])

    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)
