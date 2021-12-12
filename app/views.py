from flask import render_template,redirect,flash
from app import app,models,db
from .forms import registerForm, loginForm,updatePass

@app.route('/', methods =['GET','POST'])
def loginPage():
    form = loginForm()  
    account = models.Account.query.all()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        for user in account:
            if username == user.username and password == user.password:
                global curUser
                curUser = user
                app.logger.info("login successful")
                return redirect('/allMov')
        flash("Incorrect username or password")
        app.logger.error("login unsuccessful")
    return render_template('loginPage.html', title='login', form = form)


@app.route('/registerPage', methods=['GET','POST'])
def registerPage():
    form = registerForm() 
    accounts = models.Account.query.all()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        fname = form.fname.data
        lname = form.lname.data
        dob = form.dob.data
        gender = form.gender.data
        for user in accounts:
            if user.username == username:
                flash("Please choose another username")
                app.logger.error("Please choose another username")
                return render_template('registerPage.html',title='register', form =form)
        
        newAcc = models.Account(username=username, password=password,
        fname=fname,lname=lname,dob = dob, gender = gender)
        db.session.add(newAcc)
        db.session.commit()
        app.logger.info('Account created successfuly')
        return redirect('/')
    return render_template('registerPage.html', title='register', form = form)

@app.route('/allMov', methods=['GET', 'POST'])
def allMov():
    films = models.films.query.all()
    user = models.Account.query.filter_by(username = curUser.username).first()
    interested = user.interested
    return render_template('allMov.html', title='home',interested=interested, films=films)

@app.route('/myMov', methods=['GET', 'POST'])
def myMov():
    user = models.Account.query.filter_by(username = curUser.username).first()
    return render_template('myMov.html', title='All Assessment',user=user)
@app.route('/interest/<film_id>', methods=['GET', 'POST'])
def interestFilm(film_id):
	# get the book from the book id
    film = models.films.query.get(film_id)
    user = models.Account.query.filter_by(username = curUser.username).first()
    user.interested.append(film)
    db.session.add(user)
    db.session.commit()
    return(redirect('/allMov'))
@app.route('/unInterest/<use_id>', methods=['GET', 'POST'])
def uninterestFilm(use_id):
	# get the book from the book id
	film = models.films.query.get(use_id)
	user = models.Account.query.filter_by(username = curUser.username).first()
	film.interest.remove(user)
	#commit the changes
	db.session.add(film)
	db.session.commit()
	return(redirect('/myMov'))

@app.route('/security', methods=['GET', 'POST'])
def security():
    form = updatePass()
    user = models.Account.query.filter_by(username = curUser.username).first()
    if form.validate_on_submit():
        current = form.current.data
        new = form.new.data
        if (current !=user.password):
            flash("Incorrect current password")
            app.logger.error('problem with changing password')
            return render_template('security.html', title='Complete Assessment',user=user, form = form)
        user.password = new
        db.session.commit()
        flash("Password changed")
        app.logger.info("Password changed")
        return render_template('security.html', title='Complete Assessment',user=user, form = form)
    return render_template('security.html', title='Complete Assessment',user=user, form = form)
