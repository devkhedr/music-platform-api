# Django Training - 2. Django Admin and Managers

## Materials
1. [Managers](https://docs.djangoproject.com/en/4.0/topics/db/managers/)
2. [Transactions](https://docs.djangoproject.com/en/4.0/topics/db/transactions/)
3. [Database Access Optimization](https://docs.djangoproject.com/en/4.0/topics/db/optimization/)
4. [Django Admin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/) (basics)
5. [Expressions](https://docs.djangoproject.com/en/4.0/ref/models/expressions/)

## Task
We don't want all albums to be put up for sale immediately, first we want to make sure the album name is suitable for out platform, for example
the album name shouldn't contain inappropriate expressions.

1. Add a boolean field to the album model that will help us represent whether an album is approved by an admin or not
    * tip: follow the convention for boolean field names
    * hint: what's the suitable default value for this field, (`True` or `False`)?
2. Add all models you have so far to django admin
3. The admin shouldn't be able to modify the creation time field on the album (this field should be in read-only status on django admin)
4. Add a help text that would show up under the previously mentioned boolean field on the django admin form, it should state: 
    * Approve the album if its name is not explicit
    * bonus: can you add the help text without modifying the boolean field itself? (hint: you'll modify the form)
5. When viewing the list of artists, there must be a column to show the number of approved albums for each artist
6. (bonus) Modify the artist queryset so that I can order the list of artists by the number of their approved albums
    * I should be able to do the following `Artist.objects.....order_by("approved_albums")`
7. Allow the admin to create albums for the artist from from the artist's editing form

## Guidelines
1. Use this gitignore [template](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore)
2. List your environment variables (if any) in a `.env.example` file
3. Don't forget to run `manage.py makemigrations` and `python manage.py migrate`
4. You are allowed to refer to any articles, documentation source, questions on StackOverFlow
5. You are not allowed to consult other people through any medium of communication
6. Your grade will be affected if your code isn't clean, you should maintain code cleanliness as much as you can
