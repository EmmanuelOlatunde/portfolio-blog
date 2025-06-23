from django.core.management.base import BaseCommand
from portfolio.models import Skill  # Change 'skills' to your actual app name


class Command(BaseCommand):
    help = 'Seed default skills with proficiency, category, and icons'

    def handle(self, *args, **kwargs):
        default_skills = [
            # Backend
            {"name": "Python", "proficiency": 90, "category": "backend", "icon": "fas fa-code"},
            {"name": "Django", "proficiency": 88, "category": "backend", "icon": "fas fa-code"},
            {"name": "Django REST Framework", "proficiency": 85, "category": "backend", "icon": "fas fa-code"},
            {"name": "FastAPI", "proficiency": 65, "category": "backend", "icon": "fas fa-code"},
            {"name": "C++", "proficiency": 30, "category": "backend", "icon": "fas fa-code"},
            
            # Frontend
            {"name": "HTML", "proficiency": 70, "category": "frontend", "icon": "fas fa-code"},
            {"name": "CSS", "proficiency": 60, "category": "frontend", "icon": "fas fa-code"},
            {"name": "JavaScript", "proficiency": 50, "category": "frontend", "icon": "fas fa-code"},
            {"name": "React", "proficiency": 40, "category": "frontend", "icon": "fas fa-code"},
            
            # Database
            {"name": "PostgreSQL", "proficiency": 75, "category": "database", "icon": "fas fa-code"},
            {"name": "SQLite", "proficiency": 80, "category": "database", "icon": "fas fa-code"},
            {"name": "MySQL", "proficiency": 65, "category": "database", "icon": "fas fa-code"},
            {"name": "MongoDB", "proficiency": 50, "category": "database", "icon": "fas fa-code"},
            
            # Tools & DevOps
            {"name": "Git", "proficiency": 85, "category": "tools", "icon": "fas fa-git"},
            {"name": "Docker", "proficiency": 70, "category": "tools", "icon": "fas fa-code"},
            {"name": "Linux", "proficiency": 75, "category": "tools", "icon": "fas fa-linux"},
            {"name": "Heroku", "proficiency": 60, "category": "tools", "icon": "fas fa-cloud"},
            {"name": "GitHub", "proficiency": 80, "category": "tools", "icon": "fas fa-github"},
            
            # Other
            {"name": "VS Code", "proficiency": 90, "category": "other", "icon": "fas fa-code"},
            {"name": "Postman", "proficiency": 85, "category": "other", "icon": "fas fa-envelope"},
            {"name": "ChatGPT", "proficiency": 95, "category": "other", "icon": "fas fa-android"},
        ]

        self.stdout.write(self.style.MIGRATE_HEADING('Seeding skills...'))

        for skill_data in default_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "proficiency": skill_data["proficiency"],
                    "category": skill_data["category"],
                    "icon": skill_data.get("icon", "")
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  → Added Skill: {skill.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'  → Skill exists: {skill.name}'))

        self.stdout.write(self.style.SUCCESS('✅ Skill seeding complete.'))
