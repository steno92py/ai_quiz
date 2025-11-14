"""Quiz routes for quiz functionality.

This module handles the quiz logic, including displaying questions,
processing answers, and updating scores with a lives system.
"""

import random
from typing import Optional
from flask import render_template, request, redirect, url_for, flash, current_app, session
from flask_login import login_required, current_user
from app.quiz import quiz_bp
from app.models import Question, UserAnswer, User
from app.extensions import db


def _get_random_question() -> Optional[Question]:
    """Get a random question with topic 'ai_python'.

    Returns:
        Random Question object or None if no questions available.
    """
    questions = Question.query.filter_by(topic='ai_python').all()

    if not questions:
        return None

    return random.choice(questions)


def _get_user_rank() -> int:
    """Get current user's rank in the leaderboard.

    Returns:
        User's position (1-based) in the leaderboard.
    """
    users_above = User.query.filter(User.total_score > current_user.total_score).count()
    return users_above + 1


def _get_total_users() -> int:
    """Get total number of users.

    Returns:
        Total count of users.
    """
    return User.query.count()


@quiz_bp.route('/', methods=['GET', 'POST'])
@login_required
def quiz():
    """Handle quiz page with questions and answers using a lives system.

    GET: Display current user's score, lives, and a random question.
    POST: Process user's answer, update score if correct, decrease lives if wrong.

    Returns:
        Rendered quiz template or game over screen.
    """
    feedback = None
    points_earned = 0
    game_over = False

    # Reset lives on GET (new quiz session)
    if request.method == 'GET':
        session['lives'] = 3
        session['session_score'] = 0

    if request.method == 'POST':
        action = request.form.get('action')

        # Handle restart
        if action == 'restart':
            session['lives'] = 3
            session['session_score'] = 0
            return redirect(url_for('quiz.quiz'))

        # Process answer submission
        question_id = request.form.get('question_id', type=int)
        chosen_option = request.form.get('answer', '').strip().lower()

        if question_id and chosen_option and chosen_option in ['a', 'b', 'c', 'd']:
            # Load question from database
            answered_question = Question.query.get(question_id)

            if answered_question:
                # Check if answer is correct
                is_correct = (chosen_option == answered_question.correct_option.lower())

                # Create UserAnswer record
                try:
                    user_answer = UserAnswer(
                        user_id=current_user.id,
                        question_id=question_id,
                        chosen_option=chosen_option,
                        is_correct=is_correct
                    )
                    db.session.add(user_answer)

                    # Update score and lives
                    if is_correct:
                        points_earned = current_app.config.get('POINTS_PER_CORRECT_ANSWER', 10)
                        session['session_score'] = session.get('session_score', 0) + points_earned
                        feedback = 'correct'
                    else:
                        session['lives'] -= 1
                        feedback = 'incorrect'

                        # Check for game over
                        if session['lives'] <= 0:
                            game_over = True
                            # Update total score only at game over if it's a new record
                            session_score = session.get('session_score', 0)
                            if session_score > current_user.total_score:
                                from datetime import datetime
                                current_user.total_score = session_score
                                current_user.record_date = datetime.utcnow()

                    db.session.commit()

                except Exception as e:
                    db.session.rollback()
                    feedback = 'error'

    # Check if game over
    if session.get('lives', 3) <= 0:
        game_over = True

    # If game over, show game over screen
    if game_over:
        user_rank = _get_user_rank()
        total_users = _get_total_users()
        session_score = session.get('session_score', 0)
        is_new_record = session_score >= current_user.total_score

        return render_template(
            'game_over.html',
            score=current_user.total_score,
            session_score=session_score,
            rank=user_rank,
            total_users=total_users,
            is_new_record=is_new_record
        )

    # Get a new random question
    question = _get_random_question()

    return render_template(
        'quiz.html',
        question=question,
        score=session.get('session_score', 0),
        record_score=current_user.total_score,
        lives=session.get('lives', 3),
        feedback=feedback,
        points_earned=points_earned
    )
