Создать двух пользователей (с помощью метода User.objects.create_user('username')).


user1 = User.objects.create_user(username = 'Dominic Torreto')

user2 = User.objects.create_user(username = 'Harry Potter')

user3 = User.objects.create_user(username = 'Ginny Weasley')

user4 = User.objects.create_user(username = 'DodgeTheBest123')



Создать два объекта модели Author, связанные с пользователями.


Author.objects.create(author = user1)

Author.objects.create(author = user2)



Добавить 4 категории в модель Category.


Category.objects.create(name = 'Family')

Category.objects.create(name = 'Hogwarts')

Category.objects.create(name = 'Cars')

Category.objects.create(name = 'Elder Wand')



Добавить 2 статьи и 1 новость.


author = Author.objects.get(id=2)

Post.objects.create(post_author = author, category_type = 'NW', title = 'Hogwarts can breathe easy.', content = 'Hogwarts can breathe easy. Voldemort is dead...')

Post.objects.create(post_author = author, category_type = 'AR', title = 'How I found the Elder Wand.', content = 'Today I will tell you how I found the Elder Wand...')

author = Author.objects.get(id=1)

Post.objects.create(post_author = author, category_type = 'AR', title = 'Nothing Stronger Than Family.', content = 'In this article, we will discuss how to keep the family together no matter what...')



Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).


Post.objects.get(id=1).category_post.add(Category.objects.get(id=2))

Post.objects.get(id=2).category_post.add(Category.objects.get(id=2))

Post.objects.get(id=2).category_post.add(Category.objects.get(id=4))

Post.objects.get(id=3).category_post.add(Category.objects.get(id=1))



Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).


Comment.objects.create(comment_post=Post.objects.get(id=1), comment_user=User.objects.get(id=3), comment_text = 'I want children from you!!!')

Comment.objects.create(comment_post=Post.objects.get(id=1), comment_user=Author.objects.get(id=1).author_user, comment_text = 'Very brave act!')

Comment.objects.create(comment_post=Post.objects.get(id=2), comment_user=User.objects.get(id=4), comment_text = 'I will bay mandrake root! 8(934)422...')

Comment.objects.create(comment_post=Post.objects.get(id=3), comment_user=Author.objects.get(id=2).author_user, comment_text = 'I will need this in the future!')



Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.


Comment.objects.get(id=1).like()

Comment.objects.get(id=1).dislike()

Post.objects.get(id=1).like()

Проверка рейтинга:

Comment.objects.get(id=1).comment_rating

Post.objects.get(id=3).rating




Обновить рейтинги пользователей.


a1 = Author.objects.get(id=1)
a1.update_rating()
a1.author_rating

a2 = Author.objects.get(id=2)
a2.update_rating()
a2.author_rating



Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).


>>> s = Author.objects.order_by('author_rating')[:1]
>>> for i in s:         
...     i.author_rating                           
...     i.author_user 




Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.


>>> p = Post.objects.order_by('-rating')[:1]
for i in p:
...     i.creation_date
...     i.post_author.author_user
...     i.rating
...     i.title
...     i.preview()



Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.



Post.objects.all().order_by('-rating')[0].comment_set.values('comment_date_creation', 'comment_user', 'comment_rating', 'comment_text')
