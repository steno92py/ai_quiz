"""Authentication routes for registration, login, and logout.

This module handles user authentication flows including registration,
login, and logout functionality.
"""

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth import auth_bp
from app.models import User
from app.extensions import db


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration.

    GET: Display registration form.
    POST: Process registration with validation.

    Returns:
        Rendered registration template or redirect to login.
    """
    # Redirect if already logged in
    if current_user.is_authenticated:
        flash('Sei già autenticato.', 'info')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        login = request.form.get('login', '').strip()
        nickname = request.form.get('nickname', '').strip()
        password = request.form.get('password', '')
        password_confirm = request.form.get('password_confirm', '')

        # Validation
        errors = []

        if not login:
            errors.append('Il campo login è obbligatorio.')
        if not nickname:
            errors.append('Il campo nickname è obbligatorio.')
        if not password:
            errors.append('Il campo password è obbligatorio.')
        if not password_confirm:
            errors.append('Il campo conferma password è obbligatorio.')

        if password and password_confirm and password != password_confirm:
            errors.append('Le password non corrispondono.')

        # Check uniqueness
        if login and User.query.filter_by(login=login).first():
            errors.append('Questo login è già in uso.')

        if nickname and User.query.filter_by(nickname=nickname).first():
            errors.append('Questo nickname è già in uso.')

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('register.html')

        # Create new user
        try:
            user = User(login=login, nickname=nickname)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash('Registrazione completata con successo! Ora puoi effettuare il login.', 'success')
            return redirect(url_for('auth.login'))

        except Exception as e:
            db.session.rollback()
            flash(f'Errore durante la registrazione: {str(e)}', 'danger')
            return render_template('register.html')

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login.

    GET: Display login form.
    POST: Process login credentials.

    Returns:
        Rendered login template or redirect to home.
    """
    # Redirect if already logged in
    if current_user.is_authenticated:
        flash('Sei già autenticato.', 'info')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        login_input = request.form.get('login', '').strip()
        password = request.form.get('password', '')

        if not login_input or not password:
            flash('Per favore, compila tutti i campi.', 'warning')
            return render_template('login.html')

        # Find user by login
        user = User.query.filter_by(login=login_input).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f'Benvenuto, {user.nickname}!', 'success')

            # Redirect to next page or home
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('main.home'))
        else:
            flash('Login o password non corretti.', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    """Handle user logout.

    Returns:
        Redirect to home page.
    """
    if current_user.is_authenticated:
        logout_user()
        flash('Logout effettuato con successo.', 'success')
    else:
        flash('Non sei autenticato.', 'warning')

    return redirect(url_for('main.home'))
