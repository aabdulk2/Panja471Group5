from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Book, Author, Note
from . import db
import json
#from . import session



views = Blueprint('views', __name__)


# @views.route('/note', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('Note is too short!', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     return render_template('search.html', user=current_user)

#endpoint for search
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        #book_author = session.query(Book).join(Author).filter(Book.book_number == Author.book_number, Book.title.contains(book)).all()
        books = Book.query.filter(Book.title.contains(book)).all()
       # authors = Author.query.filter(Author.book_number=books.book_number).all()
      #  for b in books:
        #authors = Author.query.filter(Author.book_number == Book.query.select(Book.title.contains(book)).all()).all()
        #books = Book.query.get(1)
        # User.query
        # cursor.execute("SELECT name, author from Book WHERE name 
        #                 LIKE %s OR author LIKE %s", (book, book))
        #conn.commit()
        #data = cursor.fetchall()
        # all in the search box will return all the tuples
       # if len(data) == 0 and book == 'all': 
            #cursor.execute("SELECT name, author from Book")
            #conn.commit()
            #data = cursor.fetchall()

        #print(book_author[0].title, book_author[0].first_name)
        
        return render_template('search.html', user=current_user, data=books)
    return render_template('search.html', user=current_user)


@views.route('/search_db', methods=['POST'])
def searchdb():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})