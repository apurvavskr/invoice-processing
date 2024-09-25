# Invoice Processing Django Application

This is a Django application designed to convert an uploaded invoice image into an editable HTML invoice template using OCR and AI-based text extraction. The focus of this README is solely on the Django web interface, excluding the image processing aspect, which is covered in other parts of the repository.

## Features
- Upload invoice images for template generation.
- Simple and minimalistic UI for uploading images.
- Download generated HTML invoice template.
- Implements the use of Django forms and OpenAI API for processing.
  
## Application Structure
The application follows the MVC (Model-View-Controller) architecture provided by Django. Below is a brief overview of key files:

### `manage.py`
This is the command-line utility that allows interaction with the Django project. It is used to start the server and run administrative tasks.

### `settings.py`
Contains all configurations for the Django project, including:
- Database settings (SQLite3)
- Static files directory setup
- Media files directory setup
- Installed apps, middleware, and other project settings
- OpenAI API Key integration via environment variables.

### `urls.py`
Defines URL patterns for the web app. Currently, it supports:
- Uploading an invoice image via `upload_invoice`.

### `views.py`
Handles logic for the image upload, processing, and HTML invoice generation:
- The `upload_invoice` view processes the image via the `ImageUploadForm` and passes it to the OCR-based invoice processing module.
- Upon success, a downloadable HTML file is returned to the user.

### `forms.py`
Defines the `ImageUploadForm` using Django's `forms.Form` for handling the image upload input.

### `upload.html`
This is the main template used for rendering the invoice upload page. It contains:
- A Joblogic logo.
- A form for image upload.
- JavaScript to handle file submission and status updates.

### `style.css`
Defines the styles for the upload page, providing a clean, responsive interface with styling for the form, logo, and button elements.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shashankbaraisrh/deep-learning.git
cd deep-learning/OCR/final_working_interface/jl_interface
```

### 2. Set up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. To set it up:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
Install the required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4. Set up .env file
Create a .env file in the root of the project with the following content:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Access the web app at http://127.0.0.1:8000/.


## Folder Structure
.
├── jl_interface
│   ├── document_template
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── image_processing.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── .env
│   ├── db.sqlite3
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

## Notes
Ensure that the .env file is properly configured with the OpenAI API key.
Static files (CSS, JS, and images) are already configured in settings.py.

## License
This project is licensed under the MIT License.
