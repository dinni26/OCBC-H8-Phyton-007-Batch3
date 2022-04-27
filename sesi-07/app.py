from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route('/')
# def hello_world() :
#     return "<h1>Hello, World! Hello Dini</h1>"

@app.route('/<name>')
#localhost:5000/Dini > Hello, Dini!
def hello_name(name):
    # Hello(Dini)
    # import escape dahulu
    # escape = ngambil sembarang nama yang di-input setelah (/)
    return f"Hello, {escape(name)}!"

@app.route('/')
# http://localhost:5000/
def index():
    # return 'Index Page'
    return (render_template('hello.html'))

@app.route('/hello/')
# @app.route('/world')
@app.route('/hello/<name>')
def hello(name=None):
    # return 'Hello, World'
    return (render_template('hello_name.html', name=name))
    
# Variable Rules 

@app.route('/user/<username>')
# http://localhost:5000/user/Dini
# User Dini
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/book/<string:title>')
# http://localhost:5000/book/In Wonderland
def show_book_title(title):
    # show the post with the given id, the id is an integer
    return f'Detail Book {escape(title)}'

@app.route('/post/<int:post_id>')
# http://localhost:5000/post/4o
# Not Found (gak bisa karna tipe integer)
# http://localhost:5000/post/40
# Post 40
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/post/<string:post_id_str>')
# http://localhost:5000/post/4wolves
def show_post_str(post_id_str):
    # show the post with the given id in string, the id can be a string
    return f'Post {post_id_str} #Post id str'
 
@app.route('/path/<path:subpath>')
# http://localhost:5000/path/f
# http://localhost:5000/path/foo/bar
# http://localhost:5000/path/fruits/apple/green_apple
# Out : Subpath fruits/apple/green_apple
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# HTTP Methods

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_from()
        
def do_the_login():
    return 'Do the login ....'

def show_the_login_from():
    return 'Displaying login to form ...'

if __name__ == '__main__':
    #panggil = python app.py
    #debug=True u/melakukan reload auto
    app.run(debug=True) 