import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

# -------- Chatbot Logic --------
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hi": ["Hello!", "Hi there!", "Hey 👋"],
        "hello": ["Hello!", "Hi!"],
        "how are you": ["I'm doing great! How about you?"],
        "your name": ["I'm PyBot, your Python chatbot."],
        "who created you": ["I was created using Python and Tkinter."],
        "tell me a joke": [
            "Why do programmers hate nature? Too many bugs!",
            "Why was the computer cold? It forgot to close its Windows!"
        ],
        "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
        "help": ["I can chat, tell jokes, and show time!"],
        "thank you": ["You're welcome!", "Happy to help!"],
        "bye": ["Goodbye!", "See you soon!"],
        "good morning": ["Good morning! ☀️"],
        "good night": ["Good night! 🌙"]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that yet."

# -------- Send Message --------
def send_message(event=None):
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: ", "user")
    chat_area.insert(tk.END, user_input + "\n", "user_msg")

    response = chatbot_response(user_input)

    chat_area.insert(tk.END, "Bot: ", "bot")
    chat_area.insert(tk.END, response + "\n\n", "bot_msg")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

# -------- GUI Setup --------
window = tk.Tk()
window.title("PyBot - GUI Chatbot")
window.geometry("550x600")
window.configure(bg="#1e1e1e")

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    state=tk.DISABLED
)
chat_area.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="#4FC3F7", font=("Arial", 12, "bold"))
chat_area.tag_config("user_msg", foreground="white")
chat_area.tag_config("bot", foreground="#81C784", font=("Arial", 12, "bold"))
chat_area.tag_config("bot_msg", foreground="#e0e0e0")

entry = tk.Entry(
    window,
    bg="#333333",
    fg="white",
    insertbackground="white",
    font=("Arial", 12)
)
entry.pack(padx=15, pady=10, fill=tk.X)

entry.bind("<Return>", send_message)

send_button = tk.Button(
    window,
    text="Send",
    bg="#4FC3F7",
    fg="black",
    font=("Arial", 11, "bold"),
    command=send_message
)
send_button.pack(pady=5)

window.mainloop()