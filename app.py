from flask import Flask, render_template, request, redirect, url_for, flash, session
from product_list import get_products
from comment_list import get_comments
from user import User

app = Flask(__name__)
app.secret_key = b'abc'


@app.route("/")
def products():
  return render_template('products.html', products=get_products())


@app.route('/products/<product_id>/')
def product(product_id=None):
  products = get_products()
  for product in products:
    if product['id'] == int(product_id):
      break

  return render_template('product.html', product=product, comments=get_comments())


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    user = User(request.form['first_name'], request.form['last_name'], request.form['username'], request.form['password'], False)
    if user.save_to_db():
      session['user'] = user.__dict__
      return redirect(url_for('profile'))

    flash('Username already taken')
    return redirect(url_for('signup'))

  return render_template('signup.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = User.find(request.form['username'], request.form['password'])
    if user != None:
      session['user'] = user.__dict__
      return redirect(url_for('profile'))

    flash('Wrong username / password combination!')
    return redirect(url_for('login'))

  return render_template('login.html')


@app.route('/profile/')
def profile():
  if session.get('user'):
    user = session['user']
    return render_template('profile.html', user=user, can_edit=True)

  return redirect(url_for('login'))


@app.route('/profile/edit/', methods=['GET', 'POST'])
def profile_edit():
  user = session['user']
  if request.method == 'POST':
    user = User(request.form['first_name'], request.form['last_name'], user['username'], None, False)
    user.update()
    session['user'] = user.__dict__
    flash('Your profile was updated!')
    return redirect(url_for('profile'))

  return render_template('profile_edit.html', user=user)


@app.route('/users/')
def users():
  return render_template('users.html', users=User.list())



@app.route('/users/<username>')
def user(username=None):
  can_edit = False
  user = User.find_by_username(username)

  if session.get('user'):
    if session['user']['username'] == user.username:
      can_edit = True

  return render_template('profile.html', user=user, can_edit=can_edit)



@app.route('/logout/')
def logout():
  session.clear()
  return redirect( url_for('products') )

























