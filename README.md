# C Programming Practice Portal 🚀

[![C-Programming](https://img.shields.io/badge/C-Programming-blue)](https://en.wikipedia.org/wiki/C_(programming_language))
[![Flask-Framework](https://img.shields.io/badge/Flask-Framework-green)](https://palletsprojects.com/p/flask/)
[![Bootstrap-5.3](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![Database-SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)](https://www.sqlite.org/)

A web-based learning platform built with Flask that helps learners practice and master C programming through categorized questions from basic to advanced levels.

## ✨ Features

- Categorized Questions: 14+ topics from Basics to Advanced Algorithms
- Interactive Learning: Expandable answer cards with one-click reveal
- Built-in Code Editor: Experiment and run C code in the browser
- Progress Tracking: Mark questions as complete and track progress
- Responsive UI: Built with Bootstrap 5 for mobile/desktop compatibility
- Dark/Light Mode: Comfortable coding in any theme
- Admin Panel: CRUD for topics and questions with secure auth

## 🛠 Technology Stack

- Backend: Flask, SQLAlchemy, Flask-Login
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
- Database: SQLite (development)
- Forms: WTForms, Flask-WTF

## Project Structure

```
c-programming-portal/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── forms.py              # WTForms definitions
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not checked in)
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── dark-mode.css
│   └── js/
│       ├── main.js
│       └── code-editor.js
└── templates/
    ├── base.html
    ├── index.html
    ├── topic.html
    └── admin/
        ├── login.html
        ├── dashboard.html
        ├── add_question.html
        └── add_topic.html
```

## Quick Start

Prerequisites:

- Python 3.8+
- pip

Installation and run (local development):

```bash
git clone <repository-url>
cd c-programming-portal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# create a .env with SECRET_KEY, ADMIN_USERNAME, ADMIN_PASSWORD, DATABASE_URI
python app.py
# then open http://localhost:5000
```

Environment variables example (create `.env` in project root):

```
SECRET_KEY=your-secret-key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
DATABASE_URI=sqlite:///c_programming.db
```

## Admin Panel

The admin UI is available at `/admin/login`. In the default setup the admin link is also accessible via the footer's copyright link.

## API Endpoints (selected)

- GET `/` — Homepage listing topics
- GET `/topic/<name>` — Questions for a topic
- GET `/admin/login` — Admin login page
- GET `/admin/dashboard` — Admin panel
- POST `/api/mark-complete/<id>` — Mark question complete

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add feature"`
4. Push and open a PR

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Acknowledgments

- Flask community
- Bootstrap team
- Font Awesome

Happy Coding! 💻✨
