# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.airplaneBooking
bookings = db.bookings

@app.route('/api/book', methods=['POST'])
def book_flight():
    data = request.json
    name = data['name']
    email = data['email']
    flight = data['flight']
    date = data['date']

    booking = {
        'name': name,
        'email': email,
        'flight': flight,
        'date': date
    }

    try:
        bookings.insert_one(booking)
        return jsonify({'message': 'Booking successful!'})
    except Exception as e:
        return jsonify({'message': 'Booking failed.', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
