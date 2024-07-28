# from tkinter import *
# from chat import get_response, bot_name

# BG_GRAY = "#ABB2B9"
# BG_COLOR = "#17202A"
# TEXT_COLOR = "#EAECEE"

# FONT = "Helvetica 14"
# FONT_BOLD = "Helvetica 13 bold"

# class ChatApplication:
    
#     def __init__(self):
#         self.window = Tk()
#         self._setup_main_window()
        
#     def run(self):
#         self.window.mainloop()
        
#     def _setup_main_window(self):
#         self.window.title("Chat")
#         self.window.resizable(width=False, height=False)
#         self.window.configure(width=570, height=550, bg=BG_COLOR)
        
#         # head label
#         head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
#                            text="Welcome", font=FONT_BOLD, pady=10)
#         head_label.place(relwidth=1)
        
#         # tiny divider
#         line = Label(self.window, width=450, bg=BG_GRAY)
#         line.place(relwidth=1, rely=0.07, relheight=0.012)
        
#         # text widget
#         self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
#                                 font=FONT, padx=5, pady=5)
#         self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
#         self.text_widget.configure(cursor="arrow", state=DISABLED)
        
#         # scroll bar
#         scrollbar = Scrollbar(self.text_widget)
#         scrollbar.place(relheight=1, relx=0.974)
#         scrollbar.configure(command=self.text_widget.yview)
        
#         # bottom label
#         bottom_label = Label(self.window, bg=BG_GRAY, height=80)
#         bottom_label.place(relwidth=1, rely=0.825)
        
#         # message entry box
#         self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
#         self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
#         self.msg_entry.focus()
#         self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
#         # send button
#         send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
#                              command=lambda: self._on_enter_pressed(None))
#         send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
#     def _on_enter_pressed(self, event):
#         msg = self.msg_entry.get()
#         self._insert_message(msg, "You")
        
#     def _insert_message(self, msg, sender):
#         if not msg:
#             return
        
#         self.msg_entry.delete(0, END)
#         msg1 = f"{sender}: {msg}\n\n"
#         self.text_widget.configure(state=NORMAL)
#         self.text_widget.insert(END, msg1)
#         self.text_widget.configure(state=DISABLED)
        
#         msg2 = f"{bot_name}: {get_response(msg)}\n\n"
#         self.text_widget.configure(state=NORMAL)
#         self.text_widget.insert(END, msg2)
#         self.text_widget.configure(state=DISABLED)
        
#         self.text_widget.see(END)
             
        
# if __name__ == "__main__":
#     app = ChatApplication()
#     app.run()






# from flask import Flask, render_template, request, jsonify
# from chat import get_response, bot_name
# from pymongo import MongoClient

# app = Flask(__name__)

# # Connect to MongoDB
# client = MongoClient('mongodb://127.0.0.1:27017/')
# db = client['vit-parking']
# reviews_collection = db['reviews']
# replies_collection = db['replies']

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/ask")
# def ask():
#     return render_template("ask.html")

# @app.route("/recomend")
# def recomend():
#     return render_template("recomend.html")

# @app.route("/get", methods=["POST"])
# def chatbot_response():
#     msg = request.json.get("msg")
#     if not msg:
#         return jsonify({"response": "Error: no message provided."})
    
#     response = get_response(msg)
#     return jsonify({"response": response, "bot_name": bot_name})


# @app.route("/post_review", methods=["POST"])
# def post_review():
#     content = request.json.get("content")
#     if not content:
#         return jsonify({"error": "No content provided"}), 400
    
#     review = {"content": content}
#     result = reviews_collection.insert_one(review)
#     if result.acknowledged:
#         return jsonify({"message": "Review posted successfully", "id": str(result.inserted_id)})
#     else:
#         return jsonify({"error": "Failed to post review"}), 500

# @app.route("/get_reviews", methods=["GET"])
# def get_reviews():
#     # Convert ObjectId to string format
#     reviews = list(reviews_collection.find({}, {"_id": 1, "content": 1}))
#     for review in reviews:
#         review['_id'] = str(review['_id'])  # Convert ObjectId to string
#     return jsonify(reviews)

# @app.route("/get_replies/<parent_id>", methods=["GET"])
# def get_replies(parent_id):
#     try:
#         replies = list(replies_collection.find({"parent_id": parent_id}, {"_id": 0, "content": 1}))
#         # for reply in replies:
#         #     reply['_id'] = str(reply['_id'])  # Convert ObjectId to string
#         return jsonify(replies)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/post_reply", methods=["POST"])
# def post_reply():
#     parent_id = request.json.get("parent_id")
#     content = request.json.get("content")
#     if not parent_id or not content:
#         return jsonify({"error": "parent_id and content are required"}), 400
    
#     reply = {"parent_id": parent_id, "content": content}
#     result = replies_collection.insert_one(reply)
#     if result.acknowledged:
#         return jsonify({"message": "Reply posted successfully", "id": str(result.inserted_id)})
#     else:
#         return jsonify({"error": "Failed to post reply"}), 500


# if __name__ == "__main__":
#     app.run(debug=True, port=5001)


from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from chat import get_response, bot_name

app = Flask(__name__)

# Connect to MongoDB
# client = MongoClient('mongodb://127.0.0.1:27017/')
client = MongoClient('mongodb+srv://sampilutla:MONGOcherry05@ask-vit.lgpfz82.mongodb.net/?retryWrites=true&w=majority&appName=ASK-VIT')
db = client['ask-vit']
# db = client
reviews_collection = db['questions']
replies_collection = db['replies']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ask")
def ask():
    return render_template("ask.html")

@app.route("/recomend")
def recomend():
    return render_template("recomend.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.json.get("msg")
    if not msg:
        return jsonify({"response": "Error: no message provided."})
    
    response = get_response(msg)
    return jsonify({"response": response, "bot_name": bot_name})



@app.route("/post_review", methods=["POST"])
def post_review():
    content = request.json.get("content")
    if not content:
        return jsonify({"error": "No content provided"}), 400
    
    review = {"content": content}
    result = reviews_collection.insert_one(review)
    if result.acknowledged:
        return jsonify({"message": "Review posted successfully", "id": str(result.inserted_id)})
    else:
        return jsonify({"error": "Failed to post review"}), 500

@app.route("/get_reviews", methods=["GET"])
def get_reviews():
    # Convert ObjectId to string format
    reviews = list(reviews_collection.find({}, {"_id": 1, "content": 1}))
    for review in reviews:
        review['_id'] = str(review['_id'])  # Convert ObjectId to string
    return jsonify(reviews)

@app.route("/get_replies/<parent_id>", methods=["GET"])
def get_replies(parent_id):
    try:
        replies = list(replies_collection.find({"parent_id": parent_id}, {"_id": 0, "content": 1}))
        # for reply in replies:
        #     reply['_id'] = str(reply['_id'])  # Convert ObjectId to string
        return jsonify(replies)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/post_reply", methods=["POST"])
def post_reply():
    parent_id = request.json.get("parent_id")
    content = request.json.get("content")
    if not parent_id or not content:
        return jsonify({"error": "parent_id and content are required"}), 400
    
    reply = {"parent_id": parent_id, "content": content}
    result = replies_collection.insert_one(reply)
    if result.acknowledged:
        return jsonify({"message": "Reply posted successfully", "id": str(result.inserted_id)})
    else:
        return jsonify({"error": "Failed to post reply"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)