# TechZone

## Overview
TechZone is an e-commerce website that displays desktops, laptops, and accessories.

## Technologies Used
- Python
- Django
- HTML & CSS (frontend built with AI assistance)

> The backend (models, views, URLs, CRUD logic) was written by me. The frontend was AI-assisted, and I plan to revisit and implement it myself, in sha Allah.

## Features
- View all available products and categories on the home page
- Filter products by category
- Search for products
- Product details view
- Full CRUD operations for managing products (Add, Edit, Update, Delete)

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/menna-khaled16107/Ecommerce-app.git
   cd Ecommerce-app
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

Then open http://127.0.0.1:8000/ in your browser.