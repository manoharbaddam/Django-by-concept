from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = "Seed database with initial courses"

    def handle(self, *args, **kwargs):
        courses = [
            {
                "title": "Introduction to Python",
                "description": "Learn Python basics including syntax and data types."
            },
            {
                "title": "Web Development with Django",
                "description": "Build full-stack web applications using Django."
            },
            {
                "title": "JavaScript for Beginners",
                "description": "Learn JavaScript fundamentals and browser interactions."
            },
            {
                "title": "HTML & CSS Fundamentals",
                "description": "Create modern, responsive websites."
            },
            {
                "title": "Database Fundamentals",
                "description": "Understand relational databases and SQL."
            },
            {
                "title": "Git and Version Control",
                "description": "Learn Git workflows and collaboration."
            },
            {
                "title": "Introduction to Machine Learning",
                "description": "Explore basic machine learning concepts."
            }
        ]

        created = 0
        for course in courses:
            obj, is_created = Course.objects.get_or_create(
                title=course["title"],
                defaults={"description": course["description"]}
            )
            if is_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(f"{created} courses seeded successfully.")
        )
