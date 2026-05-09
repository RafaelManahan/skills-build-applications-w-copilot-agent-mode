from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

	def __str__(self):
		return self.name

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='activities')
	date = models.DateField()
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	points = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.user.name} - {self.workout.name} on {self.date}"

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
	points = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.team.name}: {self.points} points"
