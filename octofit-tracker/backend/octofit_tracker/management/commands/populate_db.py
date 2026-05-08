from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Workouts
        run = Workout.objects.create(name='Run', description='Running workout')
        swim = Workout.objects.create(name='Swim', description='Swimming workout')
        lift = Workout.objects.create(name='Lift', description='Weight lifting')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        today = timezone.now().date()
        Activity.objects.create(user=ironman, workout=run, date=today, duration=30, points=10)
        Activity.objects.create(user=captain, workout=swim, date=today - timedelta(days=1), duration=45, points=15)
        Activity.objects.create(user=batman, workout=lift, date=today, duration=60, points=20)
        Activity.objects.create(user=superman, workout=run, date=today - timedelta(days=2), duration=25, points=8)

        # Calculate Leaderboard
        marvel_points = sum(a.points for a in Activity.objects.filter(user__team=marvel))
        dc_points = sum(a.points for a in Activity.objects.filter(user__team=dc))
        Leaderboard.objects.create(team=marvel, points=marvel_points)
        Leaderboard.objects.create(team=dc, points=dc_points)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
