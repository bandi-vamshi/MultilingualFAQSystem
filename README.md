# MultilingualFAQSystem

# Overview

This project is a Django-based REST API designed to manage FAQs with multilingual support. It provides API endpoints to:

List, create, update, and delete FAQs. Automatically translate FAQ questions into Hindi and Bengali. The system uses Django REST Framework (DRF) for handling API requests and responses. We leverage a translation library to provide multilingual capabilities.

## Installation

Follow the steps below to get started with the project.

# Clone the Repository

git clone https://github.com/your-repo/multilangfaq.git
cd multilangfaq

# Install Dependencies Install the required dependencies using pip:

pip install -r requirements.txt

# Set Up the Database Run the migrations to set up your database schema:

python manage.py migrate

# Create a Superuser Create a superuser to access the Django admin panel:

python manage.py createsuperuser

# Start the Django Development Server Run the following command to start your Django application:

python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

# API Endpoints

Below are the API endpoints to manage the FAQs.

List All FAQs GET /api/faqs/ This endpoint retrieves a list of all FAQs.

# cURL:

curl -X GET http://127.0.0.1:8000/api/faqs/
You can also visit http://127.0.0.1:8000/api/faqs/ in your browser.

# Create a New FAQ POST /api/faqs/

curl -X POST http://127.0.0.1:8000/api/faqs/ \
 -H "Content-Type: application/json" \
 -d '{"question": "What is Django?", "answer": "Django is a high-level Python framework."}'
Postman: Method: POST
URL: http://127.0.0.1:8000/api/faqs/
Headers:
Content-Type: application/json

# Body (raw JSON)

{
"question": "What is Django?",
"answer": "Django is a high-level Python framework."
}

# Retrieve a Specific FAQ GET /api/faqs/{id}/

This endpoint retrieves a specific FAQ based on the provided ID.
cURL:
curl -X GET http://127.0.0.1:8000/api/faqs/1/
Update an FAQ PUT /api/faqs/{id}/

# This endpoint updates an existing FAQ by ID. Provide a JSON body with updated question and answer fields.

cURL:
curl -X PUT http://127.0.0.1:8000/api/faqs/1/ \
 -H "Content-Type: application/json" \
 -d '{"question": "Updated Question?", "answer": "Updated Answer"}'

# Delete an FAQ DELETE /api/faqs/{id}/

This endpoint deletes an FAQ by ID.
curl -X DELETE http://127.0.0.1:8000/api/faqs/1/
Get a Translated FAQ GET /api/faqs/{id}/translate/?lang=hi

# This endpoint translates the FAQ question into the specified language. The supported languages include hi (Hindi) and bn (Bengali).

cURL:
curl -X GET "http://127.0.0.1:8000/api/faqs/1/translate/?lang=hi"

# This will return:

{
"question": "Django क्या है?",
"answer": "Django एक उच्च स्तरीय पायथन फ्रेमवर्क है।"
}

## Git & Version Control

# Version Control with Git

This project uses Git for version control. It is essential to follow best practices and ensure the commit history is clean, descriptive, and follows conventional commit messages. Atomic commits should be made for each significant change, and each commit should have a clear and concise message that explains the change.

# Conventional Commit Messages

To maintain a clean Git history, the following commit message convention is used:

feat: Adds a new feature to the project.
fix: Fixes a bug or issue in the code.
docs: Updates documentation such as README, API documentation, etc.
style: Changes related to code style (formatting, spacing, etc.)
refactor: Refactors code for improvement without changing functionality.
test: Adds or modifies tests.
chore: Changes that don't fall under other categories (e.g., updates dependencies).

# Conclusion

This setup allows you to manage FAQs with multilingual support in your Django application. You can create, update, retrieve, and delete FAQs via API endpoints, and translate the FAQ questions to Hindi or Bengali using the translation feature. The DRF browsable API makes it easier to test the endpoints directly in the browser.
