"""Database models for the quiz application.

This module defines the SQLAlchemy models for users, questions, and user answers.
"""

from datetime import datetime
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class User(UserMixin, db.Model):
    """User model for authentication and scoring.

    Attributes:
        id: Primary key.
        login: Unique username for authentication.
        nickname: Unique display name for leaderboard.
        password_hash: Hashed password.
        total_score: Cumulative quiz score.
        record_date: Timestamp when the record score was achieved.
        created_at: Account creation timestamp.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False, index=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    total_score = db.Column(db.Integer, default=0, nullable=False)
    record_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationship
    answers = db.relationship('UserAnswer', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password: str) -> None:
        """Hash and set the user's password.

        Args:
            password: Plain text password to hash.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verify a password against the stored hash.

        Args:
            password: Plain text password to verify.

        Returns:
            True if password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'<User {self.login}>'


class Question(db.Model):
    """Quiz question model.

    Attributes:
        id: Primary key.
        text: Question text.
        option_a, option_b, option_c, option_d: Answer choices.
        correct_option: The correct answer ('a', 'b', 'c', or 'd').
        topic: Question category (default: 'ai_python').
        difficulty: Question difficulty level.
    """

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # 'a', 'b', 'c', or 'd'
    topic = db.Column(db.String(50), default='ai_python', nullable=False)
    difficulty = db.Column(db.String(20), default='medium')

    # Relationship
    answers = db.relationship('UserAnswer', backref='question', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'<Question {self.id}: {self.text[:50]}...>'


class UserAnswer(db.Model):
    """User answer tracking model.

    Attributes:
        id: Primary key.
        user_id: Foreign key to User.
        question_id: Foreign key to Question.
        chosen_option: User's selected answer.
        is_correct: Whether the answer was correct.
        answered_at: Timestamp of the answer.
    """

    __tablename__ = 'user_answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    chosen_option = db.Column(db.String(1), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    answered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f'<UserAnswer user={self.user_id} question={self.question_id} correct={self.is_correct}>'
