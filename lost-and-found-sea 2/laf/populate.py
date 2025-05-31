import os
import django
import random
from datetime import timedelta
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()
fake = Faker()

CATEGORIES = ["LOST", "FOUND"]
ITEMS = [
    "wallet",
    "phone",
    "keys",
    "backpack",
    "laptop",
    "watch",
    "glasses",
    "umbrella",
    "book",
    "water bottle",
    "jacket",
    "shoes",
    "headphones",
    "charger",
    "documents",
    "bag",
]


def clean_data():
    User.objects.all().delete()
    Post.objects.all().delete()
    print("Cleaned up all data!")


def create_users(n=15):
    users = []
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = f"{first_name[:3]}{last_name[:3]}{random.randint(100, 999)}".lower()
        email = f"{first_name}.{last_name}@{fake.domain_name()}".lower()
        password = "TestPass123!"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        users.append(user)
        print(f"Created user: {username}")
    return users


def create_posts(users, n=50):
    for _ in range(n):
        author = random.choice(users)
        category = random.choice(CATEGORIES)
        item = random.choice(ITEMS)
        title = f"{category.title()} {item.title()}"
        description = fake.paragraph(nb_sentences=6)

        # Create post with random date in last 30 days
        created_at = timezone.now() - timedelta(days=random.randint(0, 30))

        Post.objects.create(
            title=title,
            description=description,
            category=category,
            author=author,
            created_at=created_at,
        )
    print(f"Created {n} posts")


def populate():
    print("Creating users...")
    users = create_users(15)

    print("\nCreating posts...")
    create_posts(users, 50)

    # Print summary
    print("\n=== Population complete ===")
    print(f"Total users created: {User.objects.count()}")
    print(f"Total posts created: {Post.objects.count()}\n")


if __name__ == "__main__":
    clean_data()
    populate()
