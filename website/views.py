#stores the standard routes of the website, anything not related to the authentication of the user
# this will be the blueprint of the website (roots (URLs))

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user # links to userMixin to access info about current logged in user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST']) #takes in data and loads as json object
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId) #looks for the note with corresponding id
    if note:
        if note.user_id == current_user.id: #if the isgned in user owns this note then delete
            db.session.delete(note)
            db.session.commit()

    return jsonify({})   

