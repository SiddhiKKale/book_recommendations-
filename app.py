import os

# Define the updated Streamlit + Firebase app.py with reading & writing to Firestore
updated_app_py = """
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_config.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Add book to Firestore

def add_book_to_firestore(book):
    db.collection("books").add(book)

# Load books from Firestore

def load_books_from_firestore():
    books = db.collection("books").stream()
    book_list = []
    for doc in books:
        data = doc.to_dict()
        data["id"] = doc.id
        book_list.append(data)
    return book_list

# UI - Book Addition
st.title("📘 Smart Book Recommender (Firebase)")
st.header("Add a New Book")

name = st.text_input("Book Name")
author = st.text_input("Author")
genres = st.text_input("Genres (comma separated)")
types = st.text_input("Types (comma separated)")

if st.button("Add Book to Firestore"):
    book = {
        "name": name,
        "author": author,
        "genres": [g.strip() for g in genres.split(",") if g.strip()],
        "types": [t.strip() for t in types.split(",") if t.strip()]
    }
    add_book_to_firestore(book)
    st.success("✅ Book added to Firebase!")

# UI - Display Books from Firestore
st.header("📚 Books in Firestore")
books = load_books_from_firestore()

if books:
    for book in books:
        st.markdown(f"**{book.get('name')}** by {book.get('author')}")
        st.markdown(f"*Genres:* {', '.join(book.get('genres', []))}  \n*Types:* {', '.join(book.get('types', []))}")
        st.markdown("---")
else:
    st.info("No books found in Firestore.")
"""

# Save it to streamlit-app/app.py
app_py_path = app_py_path = r"C:\Users\psidd\Desktop\bookproject\streamlit-app\app.py"

with open('yourfile.txt', 'w', encoding='utf-8') as f:
    f.write('📘 This is a test.')
