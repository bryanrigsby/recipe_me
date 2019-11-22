from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import datetime
from .models import User, Recipe, Comment, UserImage, RecipeImage


#######################################################################
# login/registration and clearing session #
def login_page(request):
    return render(request, 'thanksgiving_recipes_app/login.html')

def register_page(request):
    return render(request, 'thanksgiving_recipes_app/register.html')

def register(request):
    if request.method=='POST':
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register_page')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['email'] = request.POST['email']
            return redirect('/main')

def login(request):
    if request.method=='POST':
        user = User.objects.filter(email=request.POST['email']) 
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['email'] = logged_user.email
                return redirect('/main')
            else:
                messages.error(request, 'Password or Username is incorrect')
                return redirect('/login_page')
        else:
            messages.error(request, 'Password or Username is incorrect')
            return redirect('/login_page')


def main(request):
    return redirect('/success')

def clear(request):
    request.session.clear()
    return redirect('/login_page')

#######################################################################
# redering templates #

def success(request):
    if 'email' in request.session:
        context = {
            'user': User.objects.get(email=request.session['email']),
            'recipes': Recipe.objects.all(),
        }
        return render(request, 'thanksgiving_recipes_app/main.html', context)
    else:
        return redirect('/')

def user_bio(request, id):
    if 'email' in request.session:
        context = {
            'logged_in_user': User.objects.get(email=request.session['email']),
            'user': User.objects.get(id=id),
            'recipes': Recipe.objects.all(),
        }
        return render(request, 'thanksgiving_recipes_app/user_bio.html', context)
    else:
        return redirect('/')

def show_recipe(request, id):
    if 'email' in request.session:
        context = {
            'user': User.objects.get(email=request.session['email']),
            'recipes': Recipe.objects.all(),
            'recipe': Recipe.objects.get(id=id),
            'comment': Comment.objects.all(),
        }
        return render(request, 'thanksgiving_recipes_app/recipe.html', context)
    else:
        return redirect('/')

def add_recipe_page(request):
    if 'email' in request.session:
        context = {
            'user': User.objects.get(email=request.session['email']),
            'recipes': Recipe.objects.all(),
        }
        return render(request, 'thanksgiving_recipes_app/add_recipe.html', context)
    else:
        return redirect('/')

def edit_recipe_page(request, id):
    if 'email' in request.session:
        context = {
            'user': User.objects.get(email=request.session['email']),
            'recipe': Recipe.objects.get(id=id)
        }
        return render(request, 'thanksgiving_recipes_app/edit_recipe.html', context)
    else:
        return redirect('/')

#######################################################################
# action methods #

def add_recipe(request):
    if request.method=='POST':
        errors = Recipe.objects.recipe_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_recipe_page')
        else:
            #create recipe and attach who uploaded it
            print(request.FILES)
            this_recipe = Recipe.objects.create(dish=request.POST['dish'], ingredients=request.POST['ingredients'], instructions=request.POST['instructions'], hours=request.POST['hours'], minutes=request.POST['minutes'], cost=request.POST['cost'], uploaded_by=User.objects.get(email=request.session['email']), )
            RecipeImage.objects.create(cover=request.FILES['image'], recipe_image=this_recipe)
            return redirect('/main')
    else:
        return redirect('/')


def edit_recipe(request):
    if request.method=='POST':
        this_recipe = Recipe.objects.get(id=request.POST['edit'])
        errors = Recipe.objects.recipe_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/edit_recipe_page/{this_recipe.id}')
        else:
            #edit recipe and save
            this_recipe.dish = request.POST['dish']
            this_recipe.ingredients = request.POST['ingredients']
            this_recipe.instructions = request.POST['instructions']
            this_recipe.hours = request.POST['hours']
            this_recipe.minutes = request.POST['minutes']
            this_recipe.cost = request.POST['cost']
            this_recipe.save()
            return redirect('/main')
    else:
        return redirect('/')
    
def delete(request):
    if request.method=='POST':
        this_recipe = Recipe.objects.get(id=request.POST['delete'])
        this_recipe.delete()
        return redirect('/main')
    else:
        return redirect('/')


def edit_user(request, id):
    if request.method=='POST':
        this_user = User.objects.get(id=id)
        errors = User.objects.user_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/user_bio/{this_user.id}')
        else:
            #edit recipe and save
            this_user.first_name = request.POST['first_name']
            this_user.last_name = request.POST['last_name']
            this_user.bio = request.POST['bio']
            this_user.save()
            return redirect('/main')
    else:
        return redirect('/')

def like(request):
    if request.method=='POST':
        this_recipe = Recipe.objects.get(id=request.POST['like'])
        this_user = User.objects.get(email=request.session['email'])
        this_recipe.users_who_like.add(this_user)
        return redirect('/main')
    else:
        return redirect('/')

def unlike(request):
    if request.method=='POST':
        this_recipe = Recipe.objects.get(id=request.POST['unlike'])
        this_user = User.objects.get(email=request.session['email'])
        this_recipe.users_who_like.remove(this_user)
        return redirect('/main')
    else:
        return redirect('/')

def comment(request, id):
    if request.method=='POST':
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/show_recipe/{id}')
        else:
            Comment.objects.create(comment=request.POST['comment'], comment_on_recipe=Recipe.objects.get(id=request.POST['recipe_comment']), comment_by_user=User.objects.get(email=request.session['email']))
            return redirect(f'/show_recipe/{id}')
    else:
        return redirect('/')

def delete_comment(request, id):
    if request.method=='POST':
        this_comment=Comment.objects.get(id=request.POST['delete_comment'])
        this_comment.delete()
        return redirect(f'/show_recipe/{id}')
    else:
        return redirect('/')


