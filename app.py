from flask import Flask, flash, render_template, redirect, request, url_for
from db_setup import *
from sqlalchemy import or_
from helper_functions import check_un_and_email

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/home')
def home():
    with Session() as session:
        words = session.query(Word).all()
        # print([word.creator.first_name for word in words])
    return render_template('home.html', words = words, title='Home')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.errorhandler(404)
def page_not_found(the_error):
    return render_template('404.html', title = '404 Error'), 404

@app.errorhandler(500)
def internal_server_error(the_error):
    return render_template('500.html'), 500

@app.route('/word_list')
def word_list():
    with Session() as session:
        words = session.query(Word).all()
    return render_template('word_list.html', banana_words=words)


@app.route('/word_instance/<string:word_name>', methods=['GET', 'POST'])
def word_instance(word_name):
    print(word_name)
    with Session() as session:
            word = session.query(Word).filter_by(word_name=word_name).one()
            print(word.word_name)
            print(word.definition)
    return render_template('word_instance.html', html_word_name=word)

@app.route('/creator_list')
def creator_list():
    with Session() as session:
        creators = session.query(Creator).all()
        for creator in creators:
            print(creator.username)
            print(creator.id)
    return render_template('creator_list.html', html_creators_list=creators)

@app.route('/creator_instance/<string:id>')
def creator_instance(id):
    print(id)
    with Session() as session:
        creator = session.query(Creator).get(id)
    return render_template('creator_instance.html', creator=creator)


@app.route('/create_or_update_word', defaults={'word_id': -1}, methods=['GET','POST'])
@app.route('/create_or_update_word/<int:word_id>', methods=['GET','POST'])
def create_or_update_word(word_id):
    with Session() as session:
        # here request.method will equal 'GET'
        # below we are getting the the word from word_id from the GET call, to update that word_id
        if request.method == 'GET':
            creator_list = [creator.first_name for creator in session.query(Creator).all()]
            if word_id < 0:
                word = None
            else:
                word = session.query(Word).get(word_id)
            # print(creator_list)
            return render_template('create_or_update_word.html', html_creator_list = creator_list, word=word)
        else:
            # here request.method will equal 'POST'
            # below we are creating a form pythonically
            # with Session() as session:
            word_name = request.form['apple_word_name']
            definition = request.form['definition']
            example = request.form['example']
            creator_first_name = request.form['creator']
            creator = session.query(Creator).filter_by(first_name=creator_first_name).one()
            if word_id < 0:
                word = Word(word_name=word_name, definition=definition, example=example, creator=creator, creator_id=creator.id)
                session.add(word)
            else:
                word = session.query(Word).get(word_id)
                word.word_name = word_name
                word.definition = definition
                word.example = example
                word.creator = creator
                print(word.word_name, word.definition, word.example)
                print(word_name, definition, creator.get_creator_name())
                session.commit()
            session.commit()
            return redirect('/home')


@app.route('/word_list/delete_word/<int:word_id>', methods=['GET','POST'])
def delete_word(word_id):
    # if request.method == "POST":
        with Session() as session:
            word = session.query(Word).get(word_id)
            session.delete(word)
            # presumably at some point we add an ARE YOU SURE popup?
        return redirect('/word_list')

# @app.route('/create_or_update_creator', defaults={'creator_id': 0}, methods=['GET', 'POST'])
@app.route('/create_or_update_creator/', defaults={'creator_id': -1}, methods=['GET', 'POST'])
@app.route('/create_or_update_creator/<int:creator_id>', methods=['GET', 'POST'])
def create_or_update_creator(creator_id):
    if request.method == 'GET':
        with Session() as session:
            if creator_id < 0:
                creator = None
            else:
                creator = session.query(Creator).get(creator_id)
        return render_template('create_or_update_creator.html', creator=creator)
    else:
        with Session() as session:
            username = request.form['sex_username']
            first_name = request.form['sex_first_name']
            last_name = request.form['apple_last_name']
            email = request.form['apple_email']
            password = request.form['apple_password']

            # if username and/or email already exists then True flash exists
            check_un_and_email = session.query(Creator).filter(or_(Creator.username==username, Creator.email==email)).one_or_none()
            # check_email = session.query(Creator).filter(or_(Creator.username==username, Creator.email==email)).one()

            if check_un_and_email:
                flash(f'Username or Email already exists, please choose another')
                print('Username/Email already exists, please choose another')

                return redirect('/create_or_update_creator')
            else:
                # create creator world
                if request.form['submit'] == "Create":
                    creator = Creator(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    session.add(creator)
                else:
                # update creator world
                    creator = session.query(Creator).get(creator_id)
                    creator.username = request.form['sex_username']
                    creator.first_name = request.form['sex_first_name']
                    creator.last_name = request.form['apple_last_name']
                    creator.email = request.form['apple_email']
                
                db_username = session.query(Creator).filter_by(username=creator.username).one()
                if db_username:
                    return redirect('/create_or_update_creator')
                if not db_username:
                    session.commit()
            return redirect('/home')






if __name__ == '__main__':
    app.run(debug=True)

