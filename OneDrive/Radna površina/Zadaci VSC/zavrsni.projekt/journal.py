from datetime import datetime
from textblob import TextBlob

def analyze_sentiment(entry):
    try:
        analysis = TextBlob(entry)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
            comment = "I'm glad you're feeling well! Continue in the same spirit!"
        elif polarity < 0:
            sentiment = "Negative"
            comment = "You seem to be feeling bad. Consider taking a short break, taking a walk or talking to someone."
        else:
            sentiment = "Neutral"
            comment = "Your entry is neutral. If you need motivation, maybe an activity or hobby can help."
    
        print(f"Polarity: {polarity}, Sentiment: {sentiment}")
        print(f"Advice: {comment}")

        return sentiment
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return "Undefined"


def add_entry(entry):
    sentiment = analyze_sentiment(entry)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('journal.txt', 'a') as file:

        # Upisuje vrijeme, unos i sentiment u datoteku
        file.write(f"[{current_time}]\n{entry}\nSentiment: {sentiment}\n\n")

def view_entries():
    try:
        with open('journal.txt', 'r') as file:
            content = file.read()
            print("Your entries:\n")
            print(content)
    except FileNotFoundError:
        print("The journal is empty.")

# Glavna petlja programa
while True:
    action = input("Would you like to add entry (1) or show entries (2)? (Enter 3 for exit): ")
    if action == '1':
        entry = input("Enter your diary entry: ")
        add_entry(entry)
        print("The entry has been added!\n")
    elif action == '2':
        view_entries()
    elif action == '3':
        break
    else:
        print("Invalid option. Try again.")

