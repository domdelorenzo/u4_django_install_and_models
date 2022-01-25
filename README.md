## Django lessons 1 and 2 of 5 - Setting up the app and creating models.



![](data:image/jpeg;base64,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)



# How to Set Up a Django Application & Virtual Environment

## Python 3 Installation

1. In your terminal, check the version of Python running on your machine:

  ```
  python -V
  ```

  If you are **_not_** on a version of Python that is 3 or greater, then you'd have to install Python3 on your machine. Run the following command from terminal:
  ```
  brew install python3
  ```

## Setting Up a New Django Application - tunr_django

We'll be using Django as our backend framework for the next few lectures of Unit 4. Let's set up our Django project in advance of our Django lectures. In this tutorial, we will create and install Django on a new project called `tunr_django`. Follow the steps below.

1. Navigate to your sandbox folder and make a `tunr_django` directory inside your sandbox folder. Navigate into your folder.

  ```
  mkdir tunr_django
  cd tunr_django
  ```

2. Next, we're going to build a virtual environment. Virtual environments allow us to have multiple versions of Python on the same system and manage project dependencies and to use a specific version of Python for different projects. To manage our dependencies and virtual environments, we're going to use a tool called [pipenv](https://pipenv.readthedocs.io/) so make sure you have it installed with `pipenv --version`.

  If you don't have pipenv installed, easy! Homebrew to the rescue:

  ```
  brew install pipenv
```

3. Let's "activate" our virtual environment to ensure every subsequent command will use the virtual environment we created. Run the following command from the project root:

  ```
  pipenv shell
  ```

4. Open up the project in VS Code and take a look at the `Pipfile`. It should look similar to this:

  ```
  [[source]]
  name = "pypi"
  url = "https://pypi.org/simple"
  verify_ssl = true

  [dev-packages]

  [packages]
  django = "*"
  psycopg2-binary = "*"

  [requires]
  python_version = "3.7"
  ```

  Make sure `python_version` is set to a version that is 3 or greater. If the version mentioned in the `Pipfile` is already 3 or greater, then you can skip to the next step (i.e., install django).
  
  If it's set to an older version of Python (e.g., `2.7`), then you'd need to change it to the version of Python 3 that's available on your machine. You can check the version number by running `python3 -V` from your terminal. For example, if the version is `3.7.6`, then you'd have to update the `python_version` line in the `Pipfile` to `python_version="3.7.6"`.

5. Install django inside your `/tunr_django` folder:

  ```
  pipenv install django
  ```

  Running the above command will install Django and create the virtual environment where your dependencies for this project will be managed. Pipenv works a lot like npm does: it'll install our dependencies and track them in a `Pipfile`. This is similar to how `npm` works, the main difference being that pipenv does all the work for us by putting the dependencies in a separate location, so we don't have to worry about adding things to `.gitignore`.

6. Next, we're going to install the library for connecting Django to PostgreSQL:

  ```
  pipenv install psycopg2-binary
  ```

7. All we've done so far is install our dependencies and create our virtual environment. Now, we want to start our Django project:

  ```
  pipenv run django-admin startproject tunr_django .
  ```

  > Make sure you put the . on the end! This creates the project in the current directory instead of creating a new subfolder.

  Let's break down this command, because there are a few parts to it:

  - `django-admin` is the command line interface for interacting with Django. It
    has a few commands, of which `startproject` is the one to start a new Django
    project.
  - `tunr_django` is the name of our project. We add `.` after it so that the
    project is created in the current directory (the default is to create a new
    Django project in a new director).
  - `pipenv run` is required because we want to use the version of Django that we
    just installed using pipenv. If we leave off this part of the command, we'll
    use the version of the Django CLI that is installed globally (if there is
    one).

8. Let's also create our app (make sure you're running the following command within the virtual environment you created in step 3):

  ```
  $ django-admin startapp tunr
  ```

  Note: if django-admin doesn't work, you can replace it with `python3 manage.py`, assuming `manage.py` is in your current directory. Again, make sure you're running the following command within the virtual environment you created in step 3.

  This step creates an "app" inside of our project repo called `tunr`. `tunr_django` is the base django project, where we handle our routes. `tunr` is where we write our models, controllers, and templates.

  We can have many "apps" inside of a django project. This allows us to modularize our code, giving us flexibility and separation of concerns and making our code self-contained.

9. We need to include the app we generated. In `tunr_django/settings.py` find the `INSTALLED_APPS` constant dictionary. On the bottom line of the `INSTALLED_APPS` list, add `tunr`. Whenever you create a new app, you have to include it in the project.

  ```
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'tunr'
  ]
  ```

10. Next, we need to create our database. By default, Django uses sqlite for its database. We'll use postgres instead, because it's more robust and better for web applications. 

- To ensure Postgres is running on your computer, **on macOS** type:

```bash
brew services list
```

- To ensure Posgres is running on your computer, **on Linux** type:

```bash
service postgresql status
```

(_macOS_) Postgres will only work if you see a service with a `Name` of postgresql and `Status` say `started` in green. If it is yellow, try running `brew services restart postgresql`. 

(_Linux_) Postgres will only work if you see a green circle and the words
"active (running)" somewhere in the output.

After running postgres, create a new file called `settings.sql` in the project root directory:

  ```
  touch settings.sql
  ```

  Inside `settings.sql`, add the following:

  ```
  -- settings.sql
  CREATE DATABASE tunr;
  CREATE USER tunruser WITH PASSWORD 'tunr';
  GRANT ALL PRIVILEGES ON DATABASE tunr TO tunruser;
  ```

  Then run the following command from the root directory:

  ```
  $ psql -U postgres -f settings.sql
  ```
  
 If you are getting a fatal error, try removing the '-U postgres' from the command 

11. Next, we need to connect our app to the database. In `tunr_django/settings.py`, find the `DATABASES` constant dictionary. Let's edit it to look like this:

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'tunr',
          'USER': 'tunruser',
          'PASSWORD': 'tunr',
          'HOST': 'localhost'
      }
  }
  ```

12. Now, in the terminal start the Django server by running

  ```
  python3 manage.py runserver
  ```

  `manage.py` contains a lot of management commands for Django. We'll see more later, but [here](https://docs.djangoproject.com/en/2.1/ref/django-admin/) is the full documentation if you are interested in what's going on behind the scenes. You can see a list of commands that `manage.py` offers by typing:

  ```
  python3 manage.py
  ```


13. Finally, navigate to `localhost:8000`. You should see a page welcoming you to Django!


## Next, lets make some models for our data  

## Models 

Let's start working with some data. In Django, we will write out models. Models
represent the data layer of our application. We store that data in our database.

First, lets create a Python class that inherits from the Django built in
`models.Model` class. Let's also define the fields within it. We do so like
this:

```python
# tunr/models.py
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
```

Here, we are defining three fields (which will be represented as columns in our
database): `name`, `photo_url` and `nationality`. `name` and `nationality` are
character fields which means that we must add an upper limit to how many
characters are in that database field. The `photo_url` will have unlimited
length. The full listing of the available fields are
[here](https://docs.djangoproject.com/en/2.1/ref/models/fields/).

Let's also add the magic method `__str__`. This method defines what an instance
of the model will show up as by default. It will be really helpful for debugging
in the future!

```python
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
```

This is a brief example of how to write models in Django. The
[documentation](https://docs.djangoproject.com/en/2.1/topics/db/models/) is
fantastic and there are a number of
[built in field types](https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types)
that you can use for making very detailed models.

## Migrations

In the SQL class, we talked about how schema is enforced on the database side
when we use SQL databases. But here we are writing our schema on the Python
side! We have to translate that code into the schema for our database. We will
do so using migrations. In some frameworks, you have to write your migrations
yourself, but in Django the framework writes them for us!

In order to migrate this model to the database, we will run two commands. The
first is:

Windows users, you may need to add 'python -m' before some of your pipenv commands


```bash
$ python3 manage.py makemigrations
```

This will generate a migration file that gets all of its data from the code in
the `models.py` file. Go ahead and open it up - it should be in
`tunr/migrations/0001_initial.py`.

Every time you make changes to your models, run `makemigrations` again.

You should **NEVER** edit the migration files manually, as Django automatically takes care
of generating these migration files based on our model changes. Instead, edit the models
files and let django figure out what to generate from them by running
`makemigrations` again.

You **should** commit the migration files into git, however. They are crucial
for other people who want to run their own app.

When you've made all the changes you think you need, go ahead and run:\


```bash
$ python3 manage.py migrate
```

This will commit the migration to the database.

If you open up `psql`:
```
$ psql
```

and connect to the `tunr` database:
```
\c tunr
```
you'll see all the tables have now been created!

This is quite different than mongoDB, where the databases and collections get
created automatically as soon as you insert data into them.

<details>
<summary>What is a migration?</summary>
A set of changes/modifications intended for a database. They can be anything that makes a permanent change - creating columns, creating tables, changing properties, etc.
</details>



### Foreign Keys 

Let's also start filling out the Song model. We will define the class and then
add a foreign key. We do so like this:

```python
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
```

A foreign key is a field or column in one table that uniquely identifies a row
of another table. In this case, `Song` will contain a column called `artist`
that contains the ID of the associated artist. We don't have to define `id` in
the model, django and psql add them for us.

The `related_name` refers to how the model will be referred to in relation to
its parent -- you will see this in use later on. `on_delete` specifies how we
want the models to act when their parent is deleted. By using cascade, related
children will be deleted.

<details>
    <summary>What kind of relationship is implied by giving the Song table the foreign key from the artist table?</summary>

    1 -> Many
    Artist -> Song
    An artist can have many songs

</details>

What needs to happen now that we made a change to the model file?

```bash
python3 manage.py makemigrations
```

Check out the migrations folder. You should see something like `0002_song.py`.

Python automatically sequences the migration files and tries to give a
description for them - in this case, we added a song model, so it gives it the
name `song`.

Now run:

```
python3 manage.py migrate
```

And notice that it's all updated!

You can read more about migrations
[in the Migrations section of the documentation](https://docs.djangoproject.com/en/2.1/topics/migrations/)

If you want to see which migrations have been run already, use the command
`python3 manage.py showmigrations`.



### Admin Console 

Before we get too far, let's also create a superuser for our app. Django has
authentication (and authorization) right out of the box, so you don't have to
write it yourself or add a plugin.

In the terminal, run:

```bash
$ python3 manage.py createsuperuser
```

Then fill in the information in the boxes that pop up!

So far in this class, we have used seed files to add initial data to our
databases. We can also do that in Django
([see this article](https://docs.djangoproject.com/en/2.1/howto/initial-data/)),
but let's try something a little bit different instead.

Django has an admin dashboard built in, which gives us full CRUD functionality
straight out of the box.

Let's set it up! In `tunr/admin.py`, add the following code:

```python
from django.contrib import admin
from .models import Artist

admin.site.register(Artist)
```

**Now! Bear Witness To the Awesomeness of Django!!!**

Run your server again, then navigate to `localhost:8000/admin`. You can login
and get a full admin view where you have CRUD functionality for your model!

Create two Artists here using the interface.

## Finish the Song model 

- Add `title`, `album` and `preview_url` fields, then create and run the
  migrations.
- Register your Song model like you did with Artist.
- Finally create three songs using the admin site.

<details>
<summary>Solution: Modify Song Model</summary>

```python
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, default='no song title')
    album = models.CharField(max_length=100, default='no album title')
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
```

</details>

<details>
<summary>Solution: Modify admin.py</summary>

```python
from django.contrib import admin
from .models import Artist, Song
admin.site.register(Artist)
admin.site.register(Song)
```

</details>

<details>
<summary>Solution: create migration</summary>

```bash
python3 manage.py makemigrations
```

</details>

<details>
<summary>Solution: run migration</summary>

```bash
python3 manage.py migrate
```

</details>


