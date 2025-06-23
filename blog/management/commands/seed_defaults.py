from django.core.management.base import BaseCommand
from blog.models import Category, Tag
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Seed default categories and tags into the database'

    def handle(self, *args, **kwargs):
        default_categories = [
            {"name": "Django", "description": "Tips, tutorials, and best practices for Django development"},
            {"name": "REST APIs", "description": "Designing and building APIs with Django and DRF"},
            {"name": "Database Design", "description": "Schemas, migrations, performance, and optimization"},
            {"name": "Authentication", "description": "User login, tokens, JWT, OAuth, and security"},
            {"name": "Testing", "description": "Unit tests, integration testing, and TDD practices"},
            {"name": "DevOps", "description": "Deployment, CI/CD pipelines, and automation"},
            {"name": "Docker", "description": "Containerization and Docker for Django projects"},
            {"name": "Linux & Bash", "description": "Terminal commands, shell scripting, and server ops"},
            {"name": "Software Architecture", "description": "Clean code, modularity, and design principles"},
            {"name": "Version Control", "description": "Git workflows, branching, and collaboration"},
            {"name": "Project Management", "description": "Agile, SCRUM, and team communication"},
            {"name": "APIs & Integrations", "description": "Third-party APIs and integration guides"},
            {"name": "Performance Optimization", "description": "Speed, caching, and async"},
            {"name": "Security", "description": "Best practices to secure Django apps"},
            {"name": "Error Handling", "description": "Debugging and managing exceptions"},
            {"name": "Career Advice", "description": "Tips for backend devs on growth and freelancing"},
            {"name": "Tools & Productivity", "description": "Dev tools, editors, extensions"},
            {"name": "Artificial Intelligence", "description": "Using AI tools in your dev workflow"},
            {"name": "Cloud & Hosting", "description": "Deploying apps on AWS, Heroku, etc."},
            {"name": "Backend Projects", "description": "Case studies, walkthroughs, and code reviews"},
        ]


        default_tags = [
            "Django", "DRF", "JWT", "PostgreSQL", "SQLite",
            "Docker", "Git", "GitHub", "API", "JSON",
            "Unit Testing", "Pytest", "Celery", "Redis", "Nginx",
            "Gunicorn", "Linux", "OAuth2", "VS Code", "ChatGPT"
        ]


        self.stdout.write(self.style.MIGRATE_HEADING('Seeding default categories...'))
        for cat in default_categories:
            category, created = Category.objects.get_or_create(
                name=cat["name"],
                defaults={
                    "slug": slugify(cat["name"]),
                    "description": cat.get("description", "")
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  → Added Category: "{category.name}"'))
            else:
                self.stdout.write(self.style.WARNING(f'  → Category exists: "{category.name}"'))

        self.stdout.write(self.style.MIGRATE_HEADING('Seeding default tags...'))
        for tag_name in default_tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={"slug": slugify(tag_name)}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  → Added Tag: "{tag.name}"'))
            else:
                self.stdout.write(self.style.WARNING(f'  → Tag exists: "{tag.name}"'))

        self.stdout.write(self.style.SUCCESS('✅ Done seeding categories and tags.'))
