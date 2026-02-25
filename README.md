# St Thomas School Website

A lightweight Flask-based web application developed to provide essential information about the school including facilities, overview, and contact details. This project demonstrates backend deployment, static asset handling, and responsive UI design.

## Live Demo

https://st-thomas-site.onrender.com

## Features

* Informational homepage
* About section with school overview
* Facilities showcase
* Responsive layout
* Static image assets
* Flask backend server
* Production deployment using Gunicorn
* Cloud deployment on Render

## Tech Stack

**Backend**

* Python
* Flask
* Gunicorn

**Frontend**

* HTML
* CSS
* Inline templates

**Deployment**

* Render Cloud Platform

## Project Structure

```
st_thomas_website/
│
├── app.py
├── requirements.txt
├── render.yaml
└── static/
    └── images/
```

## Installation (Local Setup)

1. Clone the repository

```
git clone https://github.com/Madhan-Kdev/st-thomas-site.git
cd st-thomas-site
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000
```

## Deployment

The application is deployed on Render using Gunicorn as the production server.

Build Command:

```
pip install -r requirements.txt
```

Start Command:

```
gunicorn app:app
```

## Purpose of the Project

This project was developed to demonstrate:

* Full-stack web development fundamentals
* Flask application structure
* Deployment workflow
* Cloud hosting setup
* Real-world informational website design

## Future Improvements

* Add database integration
* Implement contact form backend
* Improve SEO optimization
* Add admin dashboard
* Convert inline templates to Jinja templates
* Add custom domain
* Improve UI/UX styling

## Author

Madhan

## License

This project is for educational purposes.
