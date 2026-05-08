from django.test import TestCase
from core.models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        workout = Workout.objects.create(name='Run', description='Running')
        Activity.objects.create(user=user, workout=workout, date='2026-05-08', duration=30, points=10)
        Leaderboard.objects.create(team=marvel, points=10)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)
    def test_team(self):
        self.assertEqual(Team.objects.count(), 1)
    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
