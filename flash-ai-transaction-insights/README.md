Flash AI Transaction Insight Assistant
The goal is to help users understand why a Bitcoin or Lightning transaction behaved the way it did — for example, whether fees were reasonable, why a transaction was slow, and when Lightning would be a better option.

What This Project Does

- Accepts basic Bitcoin or Lightning transaction details
- Analyzes fee efficiency and confirmation time
- Provides a clear, human-readable insight
- Suggests better payment options (e.g. Lightning for small or urgent payments)
- Includes a simple web UI with validation and loading state

Tech Stack

- Python
- FastAPI
- Jinja2 (server-rendered HTML)
- HTML / CSS / JavaScript (minimal UI)

- install dependencies
pip install -r requirements.txt

# run the app
uvicorn main:app --reload

 http://127.0.0.1:8000
