from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Predefined responses for different types of questions
responses = {
    "venue": [
        "We have several venues available: Grand Ballroom, Sunset Garden, and Riverside Hall. Which one would you like to book?",
        "For corporate events, we recommend the Conference Center. For weddings, the Grand Ballroom is popular."
    ],
    "rsvp": [
        "RSVP management is easy! Just provide the guest list, and we'll handle the rest.",
        "How many guests do you expect? We can set up automatic RSVP reminders."
    ],
    "guest": [
        "Your guests can inquire about event details such as the dress code, timings, and location.",
        "Would you like to send a reminder to your guests about the event?"
    ],
    "greeting": [
        "Hello! How can I assist you with your event planning today?",
        "Welcome to Eventopia! How can I help you plan your event?"
    ],
    "default": [
        "I'm sorry, I didn't understand that. Could you please clarify?",
        "I'm here to help with event planning, bookings, and inquiries."
    ]
}

# Function to generate response based on user input
def get_response(user_message):
    # Simple keyword matching to identify user intent
    user_message = user_message.lower()

    if "venue" in user_message:
        return random.choice(responses["venue"])
    elif "rsvp" in user_message:
        return random.choice(responses["rsvp"])
    elif "guest" in user_message or "inquiry" in user_message:
        return random.choice(responses["guest"])
    elif "hello" in user_message or "hi" in user_message:
        return random.choice(responses["greeting"])
    else:
        return random.choice(responses["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get("msg")  # Get user's message from the query
    response = get_response(user_message)  # Generate bot's response
    return response

if __name__ == "__main__":
    app.run(debug=True)
