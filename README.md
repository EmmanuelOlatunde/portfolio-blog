# Portfolio‑Blog 🌐✍️

**portfolio-blog** is a responsive, Django‑based personal site combining a portfolio showcase with a blog. Designed for creatives, developers, and professionals who want to present their work, share insights, and connect with visitors in one polished web app.

---

## 🚀 Key Features

* **🎨 Portfolio Showcase**: Highlight projects with images, descriptions, links, and tags.
* **📝 Blog Platform**: Create, edit, delete, and categorize posts with Markdown support.
* **👤 User Authentication**: Sign-up, login, and admin access via Django’s auth system.
* **📱 Responsive Design**: Mobile‑friendly layouts using Bootstrap (or Tailwind).
* **🔍 Search & Filter**: Find posts and projects by keyword or tag.
* **📄 Contact Form**: Secure contact form with email notifications to site owner.
* **🧩 Reusable Templates**: Components that simplify future customization.
* **⚙️ SEO‑Friendly**: Supports custom meta titles, descriptions, and post slugs.

---

## 🛠️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML5, CSS3, JavaScript (Bootstrap or TailwindCSS)
* **Database**: SQLite (default), PostgreSQL optional
* **Form Handling**: Django Forms for posts, projects, and contact
* **Media**: Uploaded images stored via Django `FileField`/`ImageField`
* **Markdown**: Rendered with `django-markdownx`

---

## 📁 Project Structure

```
portfolio-blog/
├── manage.py
├── portfolio_blog/         # Project settings and config
├── blog/                   # Blog app: models, views, forms, templates
├── projects/               # Portfolio app: models, views, forms, templates
├── templates/
│   ├── base.html           # Shared layout
│   ├── blog/               # Blog-specific templates
│   └── projects/           # Project-specific templates
├── static/                 # CSS, JS, images
├── media/                  # Uploaded project/post images
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/EmmanuelOlatunde/portfolio-blog.git
   cd portfolio-blog
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **View your site at**
   `http://127.0.0.1:8000/` – browse your portfolio & blog
   Access Django admin at `http://127.0.0.1:8000/admin/`

---

## 🧠 Usage

* **Add Content**

  * Create Projects and Blog Posts via the admin interface.
  * Use built-in fields for content, images, tags, and publication date.
* **Content Management**

  * Posts support Markdown syntax and preview before publishing.
  * Projects include clickable links and image galleries.
* **Contact Form**

  * Embedded form on the contact page; sends email notifications to admin.

---

## 🌐 Deployment

To deploy to production:

* Configure **DEBUG = False**
* Set up **allowed hosts** and environment variables
* Use **PostgreSQL** for database
* Serve **static/media files** through WhiteNoise or cloud storage (AWS S3)
* Deploy on **Heroku**, **Render**, **DigitalOcean**, or **VPS**
* Set up **HTTPS** using Let’s Encrypt

---


## 🤝 Contributing

Contributions welcome!

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes and commit: `git commit -m "Add feature"`
4. Push your branch: `git push origin feature/your-feature`
5. Open a pull request describing your improvements

---

## 📄 License

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👤 Author

Crafted with ❤️ by **Emmanuel Olatunde**

* GitHub: [@EmmanuelOlatunde](https://github.com/EmmanuelOlatunde)
* Portfolio / Contact: *(link)*

---
