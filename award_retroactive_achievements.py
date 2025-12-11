"""
Award achievements retroactively to existing users
Run this script once to award badges to users based on their completed quizzes
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartquizarena.settings')
django.setup()

from accounts.models import User
from gamification.services import AchievementService

def award_retroactive_achievements():
    """Check all users and award achievements based on existing progress"""
    all_users = User.objects.all()
    total_users = all_users.count()
    total_achievements_awarded = 0
    
    print(f"🔍 Checking {total_users} users for achievements...\n")
    
    for user in all_users:
        print(f"Checking user: {user.username}")
        
        # Use the existing achievement service to check and award
        newly_awarded = AchievementService.check_and_award_achievements(user)
        
        if newly_awarded:
            print(f"  ✓ Awarded {len(newly_awarded)} achievement(s):")
            for achievement in newly_awarded:
                print(f"    - {achievement.badge.name} {achievement.badge.icon if hasattr(achievement.badge, 'icon') else ''}")
            total_achievements_awarded += len(newly_awarded)
        else:
            print(f"  - No new achievements")
        
        print()  # Blank line for readability
    
    print("="*60)
    print(f"✅ Retroactive achievement awarding complete!")
    print(f"📊 Total users checked: {total_users}")
    print(f"🎖️  Total achievements awarded: {total_achievements_awarded}")
    print("="*60)

if __name__ == "__main__":
    print("🎯 Starting retroactive achievement awarding...\n")
    award_retroactive_achievements()
