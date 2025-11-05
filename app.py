from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import db, User, Topic, Question, UserProgress
from forms import LoginForm, QuestionForm, TopicForm
from config import Config
import json
from datetime import datetime
import os  # Add this import

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Sample data for topics (initial topics)
INITIAL_TOPICS = [
    "Basic Declarations", "Variables", "Loops", "Arrays", "Structures", 
    "Pointers", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs", 
    "Functions", "File Handling", "Searching and Sorting"
]

def reset_database():
    """Drop all tables and recreate them"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database reset successfully!")

def init_db():
    with app.app_context():
        try:
            # Try to create all tables
            db.create_all()
            
            # Create admin user
            if not User.query.filter_by(username=app.config['ADMIN_USERNAME']).first():
                admin_user = User(
                    username=app.config['ADMIN_USERNAME'],
                    password=generate_password_hash(app.config['ADMIN_PASSWORD']),
                    is_admin=True
                )
                db.session.add(admin_user)
            
            # Create initial topics
            for topic_name in INITIAL_TOPICS:
                if not Topic.query.filter_by(name=topic_name).first():
                    topic = Topic(name=topic_name, description=f"Practice questions about {topic_name}")
                    db.session.add(topic)
            
            db.session.commit()
            print("Database initialized successfully!")
            
        except Exception as e:
            print(f"Error initializing database: {e}")
            print("Attempting to reset database...")
            reset_database()
            # Try initialization again after reset
            init_db()

# Routes
@app.route('/')
def index():
    try:
        topics = Topic.query.order_by(Topic.name).all()
        return render_template('index.html', topics=topics)
    except Exception as e:
        return f"Error loading index: {str(e)}", 500

@app.route('/debug')
def debug_page():
    topics_count = Topic.query.count()
    questions_count = Question.query.count()
    return render_template('debug.html', 
                         current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                         topics_count=topics_count,
                         questions_count=questions_count)

@app.route('/topic/<topic_name>')
def topic_questions(topic_name):
    topic = Topic.query.filter_by(name=topic_name).first_or_404()
    questions = Question.query.filter_by(topic_id=topic.id).order_by(Question.difficulty, Question.id).all()
    return render_template('topic.html', topic=topic, questions=questions)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, is_admin=True).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('admin/login.html', form=form)

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    topics = Topic.query.order_by(Topic.name).all()
    total_questions = Question.query.count()
    total_topics = Topic.query.count()
    
    return render_template('admin/dashboard.html', 
                         topics=topics, 
                         total_questions=total_questions,
                         total_topics=total_topics)

@app.route('/admin/add-question', methods=['GET', 'POST'])
@login_required
def add_question():
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    form = QuestionForm()
    # Get all topics for the dropdown
    topics = Topic.query.order_by(Topic.name).all()
    form.topic.choices = [(str(t.id), t.name) for t in topics]
    
    if form.validate_on_submit():
        question = Question(
            question=form.question.data,
            answer=form.answer.data,
            difficulty=form.difficulty.data,
            topic_id=int(form.topic.data)
        )
        db.session.add(question)
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_question.html', form=form)

@app.route('/admin/add-topic', methods=['GET', 'POST'])
@login_required
def add_topic():
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    form = TopicForm()
    
    if form.validate_on_submit():
        # Check if topic already exists
        existing_topic = Topic.query.filter_by(name=form.name.data).first()
        if existing_topic:
            flash('Topic with this name already exists!', 'error')
            return render_template('admin/add_topic.html', form=form)
        
        topic = Topic(
            name=form.name.data,
            description=form.description.data or f"Practice questions about {form.name.data}"
        )
        db.session.add(topic)
        db.session.commit()
        flash(f'Topic "{form.name.data}" added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/add_topic.html', form=form)

@app.route('/admin/delete-topic/<int:topic_id>', methods=['POST'])
@login_required
def delete_topic(topic_id):
    if not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    topic = Topic.query.get_or_404(topic_id)
    topic_name = topic.name
    
    # Delete the topic (this will also delete associated questions due to cascade)
    db.session.delete(topic)
    db.session.commit()
    
    flash(f'Topic "{topic_name}" deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/reset-db')  # Add this route for manual reset
def reset_database_route():
    if not current_user.is_authenticated or not current_user.is_admin:
        flash('Access denied!', 'error')
        return redirect(url_for('index'))
    
    reset_database()
    flash('Database reset successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/api/mark-complete/<int:question_id>', methods=['POST'])
def mark_complete(question_id):
    if not current_user.is_authenticated:
        return jsonify({'error': 'Login required'}), 401
    
    progress = UserProgress.query.filter_by(
        user_id=current_user.id, 
        question_id=question_id
    ).first()
    
    if not progress:
        progress = UserProgress(
            user_id=current_user.id,
            question_id=question_id,
            completed=True
        )
        db.session.add(progress)
    else:
        progress.completed = not progress.completed
    
    db.session.commit()
    return jsonify({'completed': progress.completed})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)