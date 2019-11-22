from __future__ import unicode_literals
from django.db import models
from django.core.validators import *
from datetime import date
from datetime import datetime
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}

        #validate first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 letters'
        if str.isalpha(postData['first_name']) == False:
            errors['first_name'] = 'Only letters are allowed in first name'

        #validate last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 letters'
        if str.isalpha(postData['last_name']) == False:
            errors['last_name'] = 'Only letters are allowed last name'

        #validate email
        if len(postData['email']) < 1:
            errors['email_length'] = 'Email too short'
        if User.objects.filter(email=postData['email']).exists():
            errors['same_email'] = 'Email already used'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9-.]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'

        #validate password and password confirmation
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['confirm_password'] != postData['password']:
            errors['password'] = 'Passwords much match'

        if len(postData['bio']) < 2:
            errors['bio'] = 'Bio must be at least 2 characters'

        return errors

    def user_validator(self, postData):
        errors={}

        #validate first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 letters'
        if str.isalpha(postData['first_name']) == False:
            errors['first_name'] = 'Only letters are allowed in first name'

        #validate last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 letters'
        if str.isalpha(postData['last_name']) == False:
            errors['last_name'] = 'Only letters are allowed last name'

        #validate bio
        if len(postData['bio']) < 2:
            errors['bio'] = 'Bio must be at least 2 characters'
        
        return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors={}

        if len(postData['comment']) < 2:
            errors['comment'] = 'Comment must be at least 2 characters'

        return errors


class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        errors = {}

        if len(postData['dish']) < 2:
            errors['dish'] = 'Dish must be at least 2 characters'

        if len(postData['ingredients']) < 2:
            errors['ingredients'] = 'Ingredients must be at least 2 characters'

        if len(postData['instructions']) < 2:
            errors['instructions'] = 'Instructions must be at least 2 characters'

        INT_REGEX = re.compile(r'^\d+$')
        if not INT_REGEX.match(postData['hours']):
            errors['hours'] = 'Cook time hours must be numeric'

        if not INT_REGEX.match(postData['minutes']):
            errors['minutes'] = 'Cook time minutes must be numeric'

        if not INT_REGEX.match(postData['cost']):
            errors['cost'] = 'Cost must be numeric'

        return errors


    

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #recipes_uploaded
    #liked_recipes
    #user_has_comments
    #user_has_image
    objects = UserManager()

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<User id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Password: {self.password}, Bio: {self.bio}>'

class Recipe(models.Model):
    dish = models.CharField(max_length=45)
    ingredients = models.TextField()
    instructions = models.TextField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    cost = models.IntegerField()
    uploaded_by = models.ForeignKey(User, related_name='recipes_uploaded')
    users_who_like = models.ManyToManyField(User, related_name='liked_recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #recipe_has_comments
    #recipe_has_images
    objects = RecipeManager()

    def __repr__(self):
        return f'<Dish id: {self.id}, Ingredients: {self.ingredients}, Instructions: {self.instructions}, Cook Time: {self.cook_time}, Cost: {self.cost}>'


class Comment(models.Model):
    comment = models.TextField()
    comment_on_recipe = models.ForeignKey(Recipe, related_name='recipe_has_comments')
    comment_by_user = models.ForeignKey(User, related_name='user_has_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __repr__(self):
        return f'<User id: {self.id}, Comment: {self.comment}>'


class UserImage(models.Model):
    cover = models.ImageField(upload_to='images/')
    user_image = models.ForeignKey(User, related_name='user_has_image')

class RecipeImage(models.Model):
    cover = models.ImageField(upload_to='images/')
    recipe_image = models.ForeignKey(Recipe, related_name='recipe_has_images')
