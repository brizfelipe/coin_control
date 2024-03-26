# coin_control

## Django Installation and Setup Guide

This guide will walk you through the process of installing Django, setting up a virtual environment, and starting the development server using `runserver`.

### Prerequisites

- Python installed on your system ([Download Python](https://www.python.org/downloads/))
- Basic understanding of command line/terminal

### Step 1: Create a Virtual Environment

It's a good practice to work within a virtual environment to isolate your Django project's dependencies from other projects.

#### On Windows:

Open a command prompt and navigate to your project directory.

```bash
cd path\to\your\project
```

Create a virtual environment using `venv`.

```bash
python -m venv venv
```

Activate the virtual environment.

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

Open a terminal and navigate to your project directory.

```bash
cd path/to/your/project
```

Create a virtual environment using `venv`.

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```

### Step 2: Install Django

With the virtual environment activated, install Django using pip.

```bash
pip install django
```

This command will install the latest version of Django and its dependencies.

### Step 3: Create a Django Project

Now, you can create a new Django project.

```bash
django-admin startproject myproject
```

Replace `myproject` with the name of your project.

### Step 4: Navigate to Project Directory

Move into your newly created project directory.

```bash
cd myproject
```

### Step 5: Start the Development Server

Finally, you can start the Django development server.

```bash
python manage.py runserver
```

This will start the development server on your local machine. You can access your Django application by visiting `http://127.0.0.1:8000/` in your web browser.

To stop the server, you can press `Ctrl + C` in the terminal.
