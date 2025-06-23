from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Category, Tag

dummy_post = {
    "title": "The Vibe of Coding: A Beginner's Journey",
    "slug": "the-vibe-of-coding-a-beginners-journey",
    "excerpt": "Explore the exciting and sometimes chaotic journey of learning to code. This post is for every beginner who's ever felt overwhelmed or exhilarated at 2 AM with a bug fix.",
    "content": """
    <h2>Welcome to the Flow</h2>
    <p>There’s a moment when you stop Googling and start flowing. When the code you type starts to make sense. When error messages feel less like threats and more like clues. That’s the vibe of coding.</p>

    <h3>It's Okay to Feel Lost</h3>
    <p>Every developer starts out in the deep end. If you're here reading this, you're probably new — and that's great. Confusion is part of the process. Just like learning a new language, it takes time, repetition, and a lot of “why won’t this work?”</p>

    <h3>Tips for Catching the Vibe</h3>
    <ul>
    <li>Set up your workspace: Good music, VS Code, dark theme, and snacks.</li>
    <li>Break your problems down. Then break them down again.</li>
    <li>Don’t copy code blindly. Understand what it does. Google everything — it's not cheating.</li>
    <li>Celebrate small wins. Fixing a bug is a win. Running the server is a win.</li>
    </ul>

    <h3>You’re Not Alone</h3>
    <p>Join communities, talk to other devs, share your struggles. The vibe is real when it’s shared.</p>

    <p>So here's to late nights, broken code, and breakthrough moments. Keep going.</p>

    <blockquote>“The only way to learn to code is by writing bad code, until it becomes good code.”</blockquote>""",
    "status": "published",
    "featured": True,
    "published_date": "2024-06-01T08:00:00Z",
    "category_name": "Career Advice",  # Ensure this exists
    "tag_names": ["Beginners", "Motivation", "Mindset", "Productivity", "Coding Life"],  # Ensure these exist
}

class Command(BaseCommand):
    help = 'Seed a dummy beginner blog post on the vibe of coding'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("❌ No user found. Create a user first."))
            return

        category_name = "Career Advice"
        tag_names = ["Beginners", "Motivation", "Mindset", "Productivity", "Coding Life"]

        category, _ = Category.objects.get_or_create(name=category_name, defaults={"description": "Advice for developers"})
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)

        post, created = Post.objects.get_or_create(
            title="The Vibe of Coding: A Beginner's Journey",
            defaults={
                "excerpt": dummy_post["excerpt"],
                "content": dummy_post["content"],
                "author": user,
                "status": dummy_post["status"],
                "featured": dummy_post["featured"],
                "published_date": dummy_post["published_date"],
                "category": category
            }
        )

        if created:
            post.tags.set(tags)
            post.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Post created: {post.title}'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️ Post already exists: {post.title}'))
