"""
Populate database with initial topics for SmartQuiz Arena
Run this script once to add topics to production database
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartquizarena.settings')
django.setup()

from quizzes.models import Topic

# Define topics to add
TOPICS = [
    {"name": "Python Programming", "description": "Test your Python programming knowledge"},
    {"name": "JavaScript", "description": "Master JavaScript concepts and best practices"},
    {"name": "Data Structures", "description": "Learn about arrays, trees, graphs, and more"},
    {"name": "Algorithms", "description": "Sorting, searching, and algorithmic thinking"},
    {"name": "Web Development", "description": "HTML, CSS, and modern web technologies"},
    {"name": "Databases", "description": "SQL, PostgreSQL, and database design"},
    {"name": "Machine Learning", "description": "AI and ML fundamentals"},
    {"name": "System Design", "description": "Architecture and scalability concepts"},
]

def populate_topics():
    """Add topics to the database"""
    created_count = 0
    
    for topic_data in TOPICS:
        topic, created = Topic.objects.get_or_create(
            name=topic_data["name"],
            defaults={"description": topic_data["description"]}
        )
        
        if created:
            print(f"✓ Created topic: {topic.name}")
            created_count += 1
        else:
            print(f"- Topic already exists: {topic.name}")
    
    print(f"\n✅ Successfully populated {created_count} new topics!")
    print(f"📊 Total topics in database: {Topic.objects.count()}")

if __name__ == "__main__":
    print("🚀 Populating database with topics...\n")
    populate_topics()
