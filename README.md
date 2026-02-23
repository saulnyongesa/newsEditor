# 📰 NewsEditor Pro

A robust, Django-based Content Management System (CMS) designed for news publications. This project features a sophisticated Rich Text Editor (CKEditor 5) that allows journalists to draft, format, and publish news stories with the same ease as using Microsoft Word.

## 🚀 Features

* **Rich Text Editing:** Integrated **CKEditor 5** for a seamless writing experience.
* **Advanced Formatting:**
    * **Typography:** Bold, Italic, Underline, Strikethrough.
    * **Headings:** H1, H2, H3 for clear article structure.
    * **Colors:** Change font colors to highlight key text.
    * **Alignment:** Left, Center, Right, and Justify alignment tools.
* **Media Management:**
    * **Image Uploads:** Drag-and-drop image support directly within the editor.
    * **Resizing:** Click and drag to resize images to fit the layout.
    * **Captions:** Add captions directly below images for context.
* **Responsive Design:** Built with **Bootstrap 5**, ensuring news looks great on mobile, tablet, and desktop.
* **Homepage Feed:** A dynamic homepage that lists recent articles with thumbnail previews and publication dates.

## 🛠️ Tech Stack

* **Backend:** Python 3, Django 5.0+
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite (Default)
* **Editor:** `django-ckeditor-5`
* **Image Handling:** Pillow

## ⚙️ Installation & Setup

Follow these steps to get a local copy running on your machine.

### Prerequisites
* Python 3.8 or higher
  ```bash
  pip (Python package manager)
  ```

### 1. Clone the Repository
```bash
git clone https://github.com/saulnyongesa/newsEditor.git
cd newsEditor
```
### 2. Create a Virtual Environment
It is best practice to run Python projects in an isolated environment.

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```
### 3. Install Dependencies
Install all the required Python packages:
```bash
pip install -r requirements.txt
```
### 4. Apply Database Migrations
Set up your SQLite database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser
Create an admin account to test the backend features:
```bash
python manage.py createsuperuser
```
### 6. Run the Development Server
Start the Django application:
```bash
python manage.py runserver
```
* **Public Site:** Visit http://127.0.0.1:8000/ to see the news feed.
* **Create Post:** Visit http://127.0.0.1:8000/create/ to try out the CKEditor.

## 📝 Configuration (CKEditor)

The rich text editor's toolbar is highly customizable. In `newsEditor/settings.py`, you can modify the `CKEDITOR_5_CONFIGS` dictionary to add or remove features:
```bash
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'fontFamily', 'fontColor', 'alignment', '|',
            'bulletedList', 'numberedList', 'blockQuote', '|',
            'imageUpload', 'insertTable', 'link', '|', 'undo', 'redo'
        ],
        'height': 400,
        'width': '100%',
    }
}
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---
**Security Note:** This application uses the `|safe` template filter to render article formatting correctly. This is intended for use by trusted authors and staff only. Do not allow public, unverified users to submit rich text content without implementing a sanitizer (like `bleach`) to prevent Cross-Site Scripting (XSS).
