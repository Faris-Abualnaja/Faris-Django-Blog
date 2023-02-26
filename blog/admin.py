from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

me = User.objects.get(username='faris')
post1 = Post.objects.create(author=me, title='My first blog post', text='This is a blog. I am writing a blog. This blog is short. Thank you for reading my blog.')
post1.publish()

admin.site.register(Post)