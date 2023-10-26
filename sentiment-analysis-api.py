# sentiment-analysis-api.py

from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Example data
data = [
    {'id': 1, 'content': 'This is awesome', 'sentiment': 'Positive'},
    {'id': 2, 'content': 'I am so happy', 'sentiment': 'Positive'},
    {'id': 3, 'content': 'I am feeling sad', 'sentiment': 'Negative'}
]

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    content = request.json['content']
    sentiment = analyze_sentiment(content)
    new_item = {'id': len(data) + 1, 'content': content, 'sentiment': sentiment}
    data.append(new_item)
    return jsonify(new_item)

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    item = next((x for x in data if x['id'] == id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    content = request.json['content']
    sentiment = analyze_sentiment(content)
    item['content'] = content
    item['sentiment'] = sentiment
    return jsonify(item)

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    global data
    data = [x for x in data if x['id'] != id]
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)