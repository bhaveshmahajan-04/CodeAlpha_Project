import tkinter as tk
from tkinter import scrolledtext

# ---------- Chatbot Logic ----------
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi! 😊"
    elif user_input == "hi":
        return "Hello! How are you?"
    elif user_input == "hey":
        return "Hey there! 😄"
    elif user_input == "how are you":
        return "I'm fine, thanks! How can I help you?"
    elif user_input == "what's up":
        return "Not much, just chatting with you!"
    elif user_input == "how's it going":
        return "Going great! How about you?"
    elif user_input == "good":
        return "Glad to hear that! 😃"
    elif user_input == "bad":
        return "Oh no! Hope things get better soon."
    elif user_input == "what is your name":
        return "I'm your friendly chatbot!"
    elif user_input == "who are you":
        return "I am a simple chatbot created with Python."
    elif user_input == "help":
        return "You can say: hello, hi, hey, how are you, bye, and more!"
    elif user_input == "bye":
        return "Goodbye! Have a great day 👋"
    elif user_input == "see you":
        return "See you soon! Take care."
    elif user_input == "thank you":
        return "You're welcome! 😄"
    elif user_input == "thanks":
        return "No problem!"
    elif user_input == "what can you do":
        return "I can chat with you, answer simple questions, and keep you company!"
    elif user_input == "are you a robot":
        return "Yes, I am a chatbot 🤖"
    elif user_input == "joke":
        return "Why did the computer go to the doctor? Because it caught a virus! 😆"
    elif user_input == "funny":
        return "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep!' 😂"
    elif user_input == "favorite color":
        return "I like all colors, but I think blue is calming."
    elif user_input == "love":
        return "Love is beautiful! Spread it around 💖"
    elif user_input == "music":
        return "I enjoy music too! What's your favorite song?"
    elif user_input == "movie":
        return "I love watching sci-fi movies! What about you?"
    elif user_input == "food":
        return "Yum! I wish I could taste food."
    elif user_input == "sports":
        return "I enjoy chatting about sports! Which one do you like?"
    elif user_input == "weather":
        return "I can't feel weather, but I hope it's nice outside!"
    elif user_input == "school":
        return "School is important. What subject do you like?"
    elif user_input == "college":
        return "College life is fun and busy!"
    elif user_input == "work":
        return "Work hard and stay motivated!"
    elif user_input == "game":
        return "Gaming is awesome! What's your favorite game?"
    elif user_input == "coding":
        return "I love coding! Python is my favorite language."
    elif user_input == "python":
        return "Python is simple and powerful!"
    elif user_input == "java":
        return "Java is cool for large projects."
    elif user_input == "javascript":
        return "JS is great for web development!"
    elif user_input == "ai":
        return "Artificial Intelligence is the future! 🤖"
    elif user_input == "machine learning":
        return "Machine Learning helps computers learn from data."
    elif user_input == "deep learning":
        return "Deep Learning uses neural networks to solve complex problems."
    elif user_input == "chatbot":
        return "That's me! I can chat with you."
    elif user_input == "time":
        return "I don't have a clock, but you can check your system time."
    elif user_input == "date":
        return "Today's date is whatever your device says! 😄"
    elif user_input == "morning":
        return "Good morning! Have a great day ☀️"
    elif user_input == "afternoon":
        return "Good afternoon! Hope your day is going well 🌤️"
    elif user_input == "evening":
        return "Good evening! Relax and enjoy 🌙"
    elif user_input == "night":
        return "Good night! Sleep tight 😴"
    elif user_input == "hungry":
        return "Maybe grab some food! 🍕"
    elif user_input == "thirsty":
        return "Drink some water! 💧"
    elif user_input == "tired":
        return "Take a short break or nap 😌"
    elif user_input == "happy":
        return "That's wonderful! 😄"
    elif user_input == "sad":
        return "I'm here for you. Hope you feel better soon."
    elif user_input == "angry":
        return "Take a deep breath, it helps! 😤"
    elif user_input == "bored":
        return "Let's chat! I can keep you company."
    elif user_input == "fun":
        return "Life is fun! Let's make it even more enjoyable!"
    elif user_input == "party":
        return "Yay! Party time 🎉"
    elif user_input == "travel":
        return "Traveling is exciting! Where do you want to go?"
    elif user_input == "holiday":
        return "Holidays are the best! Any plans?"
    elif user_input == "vacation":
        return "I wish I could go too! 😆"
    elif user_input == "weekend":
        return "Weekend vibes! Relax and have fun."
    elif user_input == "monday":
        return "Monday blues? Stay motivated!"
    elif user_input == "tuesday":
        return "Tuesday is a good day to keep moving!"
    elif user_input == "wednesday":
        return "Halfway through the week!"
    elif user_input == "thursday":
        return "Almost Friday! 😄"
    elif user_input == "friday":
        return "Weekend is here! 🎉"
    elif user_input == "saturday":
        return "Enjoy your Saturday! 😎"
    elif user_input == "sunday":
        return "Relax and recharge today!"
    elif user_input == "exercise":
        return "Exercise is important for health!"
    elif user_input == "fitness":
        return "Stay fit and healthy! 💪"
    elif user_input == "meditation":
        return "Meditation calms your mind."
    elif user_input == "yoga":
        return "Yoga is great for body and mind!"
    elif user_input == "news":
        return "Check your favorite news site for latest updates."
    elif user_input == "book":
        return "Reading books is amazing! What's your favorite?"
    elif user_input == "author":
        return "I like all authors! Who do you like?"
    elif user_input == "story":
        return "I love stories! Tell me yours."
    elif user_input == "dream":
        return "Dream big and work hard! 🌟"
    elif user_input == "goal":
        return "Setting goals helps you achieve more!"
    elif user_input == "success":
        return "Success comes with patience and effort!"
    elif user_input == "failure":
        return "Failure is just a step to success!"
    elif user_input == "friend":
        return "Friends make life beautiful! 😄"
    elif user_input == "family":
        return "Family is precious. Love them!"
    elif user_input == "relationship":
        return "Healthy relationships are based on trust and respect."
    elif user_input == "happy birthday":
        return "Happy Birthday! 🎂🥳"
    elif user_input == "congratulations":
        return "Congrats! 🎉"
    elif user_input == "cheers":
        return "Cheers! 🥂"
    elif user_input == "motivation":
        return "Believe in yourself! You can do it! 💪"
    elif user_input == "inspiration":
        return "Inspiration is everywhere. Stay positive!"
    elif user_input == "study":
        return "Study hard! Knowledge is power 📚"
    elif user_input == "exam":
        return "Good luck for your exams! 🍀"
    elif user_input == "sleep":
        return "Sleep well! 😴"
    elif user_input == "dreaming":
        return "Sweet dreams! 🌙"
    elif user_input == "relax":
        return "Relax and take it easy 😌"
    elif user_input == "stress":
        return "Take a deep breath. You got this!"
    elif user_input == "funny story":
        return "I know tons of funny stories, but I love hearing yours!"
    elif user_input == "random":
        return "Random things are fun! Tell me something random."
    elif user_input == "question":
        return "Ask me anything, I’ll try to answer!"
    elif user_input == "fact":
        return "Did you know? Honey never spoils! 🍯"
    elif user_input == "riddle":
        return "I love riddles! Try me!"
    elif user_input == "game time":
        return "Let's play a word game! 😄"
    elif user_input == "challenge":
        return "I accept your challenge! 💪"
    elif user_input == "advice":
        return "Always be yourself and stay positive."
    elif user_input == "quote":
        return "Here's a quote: 'The best way to get started is to quit talking and begin doing.'"
    elif user_input == "poem":
        return "Roses are red, violets are blue… I love chatting with you! 😊"
    else:
        return "Sorry, I don't understand that." 

# ---------- Send Message ----------
def send_message():
    user_text = user_entry.get()
    if user_text.strip() == "":
        return

    # Add user message
    chat_frame.config(state=tk.NORMAL)
    chat_frame.insert(tk.END, f"You: {user_text}\n", "user")
    
    # Get bot response
    bot_reply = chatbot_response(user_text)
    chat_frame.insert(tk.END, f"Bot: {bot_reply}\n\n", "bot")
    
    chat_frame.config(state=tk.DISABLED)
    chat_frame.yview(tk.END)
    user_entry.delete(0, tk.END)

    if user_text.lower() == "bye":
        root.after(1500, root.destroy)

# ---------- UI Design ----------
root = tk.Tk()
root.title("Basic Chatbot")
root.geometry("500x600")
root.config(bg="#f5f5f5")

# Header
header = tk.Label(
    root,
    text="Chatbot Assistant",
    font=("Helvetica", 18, "bold"),
    bg="#232f3e",
    fg="white",
    pady=15
)
header.pack(fill=tk.X)

# Chat Area Frame
chat_frame = tk.Text(
    root,
    bg="#ffffff",
    fg="#0f1111",
    font=("Helvetica", 12),
    wrap=tk.WORD,
    state=tk.DISABLED,
    padx=10,
    pady=10
)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tag config for bubbles
chat_frame.tag_configure("user", background="#d1e7dd", foreground="#0f1111", lmargin1=50, lmargin2=10, rmargin=10, spacing3=5)
chat_frame.tag_configure("bot", background="#e9ecef", foreground="#0f1111", lmargin1=10, lmargin2=10, rmargin=50, spacing3=5)

# Bottom Frame
bottom_frame = tk.Frame(root, bg="#f5f5f5")
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

# Input Box
user_entry = tk.Entry(
    bottom_frame,
    font=("Helvetica", 12),
    bg="#ffffff",
    fg="#0f1111",
    insertbackground="#0f1111"
)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
user_entry.bind("<Return>", lambda event: send_message())

# Send Button
send_btn = tk.Button(
    bottom_frame,
    text="Send",
    font=("Helvetica", 12, "bold"),
    bg="#232f3e",
    fg="white",
    command=send_message
)
send_btn.pack(side=tk.RIGHT)

# Initial bot message
chat_frame.config(state=tk.NORMAL)
chat_frame.insert(tk.END, "Bot: Hello! I am your assistant. Type 'help' to see commands.\n\n", "bot")
chat_frame.config(state=tk.DISABLED)

root.mainloop()
