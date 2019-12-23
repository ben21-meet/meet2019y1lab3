from turtle import Turtle
import turtle

class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yammi!!" + self.name + "is eating" + food)
	def description(self):
		print(self.name + "is" + self.age + "years older than me and loves the color" + self.favorite_color)
	def make_sound(self,sound):
		print(self.sound + self.sound + self.sound)
	
"------------------------------------------------------------------------------------"

class Person(object):
	def __init__(self,name,age,city,gender,favorite_color):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yammi!!! Im eating my favorite" + food)
	def training(self,sport):
		print("I love doing" + sport)

Person1 = Person("Ben",15,"Jerusalem","male","black")
Person1.eat(' Breakfast')
Person1.training(" gymnastics")
"------------------------------------------------------------------------------------"
class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self,words):
		 print(words)

flower_song = Song("poem")
flower_song.sing_me_a_song(" Roses are red Violets are blue I wrote this poem for you") 
"------------------------------------------------------------------------------------"
class Bird(object):
	def __init__(self,name,color,speed):
		self.name = name
		self.color = color
		self.speed = speed
	def GetSpeed(self,speed):
		print("Bird flying at" + self.speed)
	def Race(self,Bird2):
		print("And the winner of the race is..." + Bird2)
	def Winning_Song(self,sing):
		print("We are the champions!!" + sing)

Bird1 = Bird("Tony","green",50)
Bird1.Race("Bird2!!!!")
Bird1.Winning_Song(" my friends!!")




