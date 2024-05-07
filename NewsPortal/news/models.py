from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        result_sum_rating = (Post.objects.filter(post_author_id=self.pk)
                             .aggregate(r1=Coalesce(Sum('rating'), 0)))['r1']
        result_sum_com_rat = (Comment.objects.filter(comment_user_id=self.author_user)
                              .aggregate(r2=Coalesce(Sum('comment_rating'), 0)))['r2']
        result_sum_post_com_rat = (Comment.objects.filter(comment_post__post_author__author_user=self.author_user)
                                   .aggregate(r3=Coalesce(Sum('comment_rating'), 0)))['r3']

        self.author_rating = result_sum_rating * 3 + result_sum_com_rat + result_sum_post_com_rat
        self.save()

    def __str__(self):
        return self.author_user.username


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = [
        (NEWS, 'NW'),
        (ARTICLE, 'AR'),
    ]
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    creation_date = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    content = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.content[:125]} ...'

    def __str__(self):
        return f'{self.title.title()}: {self.content}'


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date_creation = models.DateTimeField(auto_now_add=True)
    comment_rating = models.SmallIntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
