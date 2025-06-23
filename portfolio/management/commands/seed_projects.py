from django.core.management.base import BaseCommand
from portfolio.models import Project  # Replace 'portfolio' with your app name
from portfolio.models import Skill


class Command(BaseCommand):
    help = 'Seed sample projects into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('Seeding projects...'))

        project_data = [
            {
                "title": "Automated Teller",
                "short_description": "C++ simulation of ATM functionality with secure transactions.",
                "description": "A simulation project in C++ demonstrating ATM functionality with secure transaction handling.",
                "technologies": ["C++"],
                "github_url": "",
                "live_url": "",
                "featured": False,
            },
            {
                "title": "Online Food Rental System",
                "short_description": "C++ system for renting food services online.",
                "description": "A system designed in C++ to simulate food service rentals.",
                "technologies": ["C++"],
                "github_url": "",
                "live_url": "",
                "featured": False,
            },
            {
                "title": "Car Rental System",
                "short_description": "C++ desktop-based rental system for managing cars.",
                "description": "A car rental system built in C++ for vehicle bookings, returns, and payment.",
                "technologies": ["C++"],
                "github_url": "",
                "live_url": "",
                "featured": False,
            },
            {
                "title": "Age and Gender Detection System",
                "short_description": "ML project using Python for age and gender prediction.",
                "description": "A Python-based project utilizing machine learning techniques for accurate demographic analysis.",
                "technologies": ["Python"],
                "github_url": "",
                "live_url": "",
                "featured": False,
            },
            {
                "title": "Online Library System",
                "short_description": "A Django web app to manage books, users, and resources.",
                "description": "A Django web application designed for managing digital resources efficiently.",
                "technologies": ["Django", "Python"],
                "github_url": "",
                "live_url": "",
                "featured": True,
            },
            {
                "title": "PayTrack",
                "short_description": "Payment tracking app for internal company use.",
                "description": "A Django Web App designed to track and manage payments within an organization.",
                "technologies": ["Django", "Python"],
                "github_url": "",
                "live_url": "",
                "featured": True,
            },
        ]

        for data in project_data:
            project, created = Project.objects.get_or_create(
                title=data["title"],
                defaults={
                    "short_description": data["short_description"],
                    "description": data["description"],
                    "github_url": data["github_url"],
                    "live_url": data["live_url"],
                    "featured": data["featured"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  → Added Project: {project.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'  → Project exists: {project.title}'))

            # Attach technologies
            tech_names = data.get("technologies", [])
            for tech_name in tech_names:
                try:
                    skill = Skill.objects.get(name__iexact=tech_name)
                    project.technologies.add(skill)
                    self.stdout.write(f'     + Linked Skill: {skill.name}')
                except Skill.DoesNotExist:
                    self.stdout.write(self.style.NOTICE(f'     ! Skill not found: {tech_name}'))

        self.stdout.write(self.style.SUCCESS('✅ Project seeding complete.'))
