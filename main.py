import os
import json
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
import assemblyai as aai
from groq import Groq

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")


class MovingPriceAgent:
    def __init__(self):
        self.groq = Groq()  # Auto-loads GROQ_API_KEY from .env
        self.dataset = pd.DataFrame(columns=[
            'company', 'route', 'cost', 'services',
            'delivery_days', 'flexibility', 'timestamp'
        ])

    def make_call(self, phone_number, route):
        """Simulate a call with text input/output"""
        questions = [
            f"What's your cost for moving from {route}?",
            "What services are included?",
            "What's the estimated delivery time?",
            "Do you offer flexibility on dates and load sizes?"
        ]

        responses = []
        for q in questions:
            responses.append(input(f"AGENT: {q}\nCOMPANY RESPONSE: "))

        return self.process_conversation(questions, responses, route, "Test Company")

    def process_conversation(self, questions, responses, route, company):
        """Process conversation with AI"""
        transcript = "\n".join([f"Q: {q}\nA: {r}" for q, r in zip(questions, responses)])

        prompt = f"""Extract moving company quote details from this conversation:
        {transcript}
        Return JSON with: company, route (string), cost (number), 
        services (list), delivery_days (number), flexibility (string), 
        timestamp (current ISO date)"""

        try:
            response = self.groq.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="mixtral-8x7b-32768",
                response_format={"type": "json_object"},
                temperature=0.1
            )
            data = json.loads(response.choices[0].message.content)
            data['timestamp'] = datetime.now().isoformat()
            self.update_dataset(data)
            return data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def update_dataset(self, data):
        """Add new entry to dataset"""
        new_row = pd.DataFrame([{
            'company': data.get('company', 'Unknown'),
            'route': data.get('route', ''),
            'cost': float(data.get('cost', 0)),
            'services': ', '.join(data.get('services', [])),
            'delivery_days': int(data.get('delivery_days', 0)),
            'flexibility': data.get('flexibility', ''),
            'timestamp': data.get('timestamp')
        }])
        self.dataset = pd.concat([self.dataset, new_row], ignore_index=True)
        self.dataset.to_csv('moving_prices.csv', index=False)

    def get_price_comparison(self, route):
        """Generate price comparison report"""
        if self.dataset.empty:
            return []
        return self.dataset[self.dataset['route'] == route]


# Initialize agent
agent = MovingPriceAgent()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_quote', methods=['POST'])
def get_quote():
    route = request.form['route']
    phone = request.form['phone']
    result = agent.make_call(phone, route)
    return render_template('results.html', result=result, route=route)


@app.route('/compare')
def compare_prices():
    route = request.args.get('route')
    comparison_data = agent.get_price_comparison(route)
    return render_template('comparison.html',
                           comparison=comparison_data,
                           route=route)



if __name__ == "__main__":
    app.run(debug=True)