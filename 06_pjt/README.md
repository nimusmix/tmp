# 06_PJT

## ๐ ์ด๋ฒ PJT๋ฅผ ํตํด ๋ฐฐ์ด ๋ด์ฉ

- Authentication System์ ์ด์ฉํ์ฌ ์ฌ์ฉ์ ๊ถํ์ ์ค์ ํ๋ ๋ฒ
- DB ํ์ด๋ธ ๊ฐ N:1 ๊ด๊ณ๋ฅผ ํ์ฑํ๋ ๋ฒ



## A. movies/models.py

- ์๊ตฌ์ฌํญ

  - ์ ์ํ  ๋ชจ๋ธ ํด๋์ค์ ์ด๋ฆ์ Movie์ด๋ฉฐ, ๋ค์๊ณผ ๊ฐ์ ์ ๋ณด๋ฅผ ์ ์ฅํฉ๋๋ค.

    |   ํ๋๋ช    | ๋ฐ์ดํฐ ์ ํ |            ์ญํ             |
    | :---------: | :---------: | :------------------------: |
    |    title    | varchar(20) |         ์ํ ์ ๋ชฉ          |
    | description |    text     |           ์ค๊ฑฐ๋ฆฌ           |
    |   user_id   |   integer   | ์ธ๋ ํค (User ํด๋์ค ์ฐธ์กฐ) |

  - ์ ์ํ  ๋ชจ๋ธ ํด๋์ค์ ์ด๋ฆ์ Comment์ด๋ฉฐ, ๋ค์๊ณผ ๊ฐ์ ์ ๋ณด๋ฅผ ์ ์ฅํฉ๋๋ค.

      |  ํ๋๋ช  | ๋ฐ์ดํฐ ์ ํ  |            ์ญํ              |
      | :------: | :----------: | :-------------------------: |
      | content  | varchar(100) |          ๋๊ธ ๋ด์ฉ          |
      | movie_id |   integer    | ์ธ๋ ํค (Movie ํด๋์ค ์ฐธ์กฐ) |
      | user_id  |   interger   | ์ธ๋ ํค (User ํด๋์ค ์ฐธ์กฐ)  |

- ์ฝ๋

    ```python
    from django.conf import settings
    from django.db import models
    
    
    # Create your models here.
    class Movie(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=20)
        description = models.TextField()
    
    class Comment(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
        content = models.CharField(max_length=100)
    ```

- ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ
  - ForeignKey๋ฅผ ์ฌ์ฉํด ๋ค๋ฅธ ๋ชจ๋ธ ํด๋์ค๋ฅผ ์ฐ๊ฒฐํ๋ ๊ฒ



## B. accounts/models.py

- ์๊ตฌ์ฌํญ

  - ์ ์ํ  ๋ชจ๋ธ ํด๋์ค์ ์ด๋ฆ์ User์ด๋ฉฐ, AbstractUser ๋ชจ๋ธ ํด๋์ค๋ฅผ ์์๋ฐ๋ ์ปค์คํ ๋ชจ๋ธ์ ์ฌ์ฉํฉ๋๋ค.

- ์ฝ๋

    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models
    
    
    # Create your models here.
    class User(AbstractUser):
        pass
    ```



## C. movies/urls.py

- ์๊ตฌ์ฌํญ

  |                     URL ํจํด                     |                           ์ญํ                             |
  | :----------------------------------------------: | :-------------------------------------------------------: |
  |                     /movies/                     |                ์ ์ฒด ์ํ ๋ชฉ๋ก ํ์ด์ง ์กฐํ                 |
  |                 /movies/create/                  | ์๋ก์ด ์ํ ์์ฑ ํ์ด์ง ์กฐํ<br/> & ๋จ์ผ ์ํ ๋ฐ์ดํฐ ์ ์ฅ |
  |                  /movies/<pk>/                   |                ๋จ์ผ ์ํ ์์ธ ํ์ด์ง ์กฐํ                 |
  |               /movies/<pk>/update/               |  ๊ธฐ์กด ์ํ ์์  ํ์ด์ง ์กฐํ<br/> & ๋จ์ผ ์ํ ๋ฐ์ดํฐ ์์   |
  |               /movies/<pk>/delete/               |                   ๋จ์ผ ์ํ ๋ฐ์ดํฐ ์ญ์                    |
  |              /movies/<pk>/comments               |                   ๋จ์ผ ๋๊ธ ๋ฐ์ดํฐ ์ ์ฅ                   |
  | /movies/<movie_pk>/comments/<comment_pk>/delete/ |                   ๋จ์ผ ๋๊ธ ๋ฐ์ดํฐ ์ญ์                    |

- ์ฝ๋

    ```python
    from django.urls import path
    
    from . import views
    
    app_name = 'movies'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name='detail'),
        path('<int:pk>/update/', views.update, name='update'),
        path('<int:pk>/delete/', views.delete, name='delete'),
        path('<int:pk>/comments/', views.comments_create, name='comments_create'),
        path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    ]
    ```



## D. accounts/urls.py

- ์๊ตฌ์ฌํญ
  |      URL ํจํด       |                             ์ญํ                              |
  | :-----------------: | :----------------------------------------------------------: |
  |  /accounts/login/   |    ๋ก๊ทธ์ธ ํ์ด์ง ์กฐํ & ์ธ์ ๋ฐ์ดํฐ ์์ฑ ๋ฐ ์ ์ฅ (๋ก๊ทธ์ธ)    |
  |  /accounts/logout/  |                 ์ธ์ ๋ฐ์ดํฐ ์ญ์  (๋ก๊ทธ์์)                  |
  |  /accounts/signup/  |   ํ์ ์์ฑ ํ์ด์ง ์กฐํ & ๋จ์ผ ํ์ ๋ฐ์ดํฐ ์์ฑ (ํ์๊ฐ์)   |
  |  /accounts/delete/  |              ๋จ์ผ ํ์ ๋ฐ์ดํฐ ์ญ์  (ํ์ ํํด)               |
  |  /accounts/update/  | ํ์ ์ ๋ณด ์์  ํ์ด์ง ์กฐํ & ๋จ์ผ ํ์ ๋ฐ์ดํฐ ์์  (ํ์ ์ ๋ณด ์์ ) |
  | /accounts/password/ | ๋น๋ฐ๋ฒํธ ์์  ํ์ด์ง ์กฐํ & ๋จ์ผ ๋น๋ฐ๋ฒํธ ๋ฐ์ดํฐ ์์  (๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ) |
  
- ์ฝ๋

    ```python
    from django.urls import path
    
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('signup/', views.signup, name='signup'),
        path('delete/', views.delete, name='delete'),
        path('update/', views.update, name='update'),
        path('password/', views.change_password, name='change_password'),
        path('profile/<username>/', views.profile, name='profile'),
    ]
    ```



## E. movies/views.py

- ์๊ตฌ์ฌํญ

    |   View ํจ์๋ช   |                             ์ญํ                              | ํ์ฉ HTTP Method |
    | :-------------: | :----------------------------------------------------------: | :--------------: |
    |      index      |          ์ ์ฒด ์ํ ๋ฐ์ดํฐ ์กฐํ ๋ฐ index.html ๋ ๋๋ง          |       GET        |
    |     create      | create.html ๋ ๋๋ง<br/>& ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ์ํ ๋ฐ์ดํฐ ์ ์ฅ ํ detail.html ๋ฆฌ๋ค์ด๋ ํธ |    GET & POST    |
    |     detail      |         ๋จ์ผ ์ํ ๋ฐ์ดํฐ ์กฐํ ๋ฐ detail.html ๋ ๋๋ง          |       GET        |
    |     update      | ์์  ๋์ ์ํ ๋ฐ์ดํฐ ์กฐํ ๋ฐ update.html ๋ ๋๋ง<br/>& ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ์ํ ๋ฐ์ดํฐ ์์  ํ detail.html ๋ฆฌ๋ค์ด๋ ํธ |    GET & POST    |
    |     delete      |        ๋จ์ผ ์ํ ๋ฐ์ดํฐ ์ญ์  ๋ฐ index.html ๋ฆฌ๋ค์ด๋ ํธ        |       POST       |
    | comments_create |  ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ๋๊ธ ๋ฐ์ดํฐ ์ ์ฅ ํ detail.html ๋ฆฌ๋ค์ด๋ ํธ   |       POST       |
    | comments_delete |       ๋จ์ผ ๋๊ธ ๋ฐ์ดํฐ ์ญ์  ๋ฐ detail.html ๋ฆฌ๋ค์ด๋ ํธ        |       POST       |

- ์ฝ๋

    ```python
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import redirect, render
    from django.views.decorators.http import (require_http_methods, require_POST,
                                              require_safe)
    
    from .forms import CommentForm, MovieForm
    from .models import Comment, Movie
    
    
    # Create your views here.
    @require_safe
    def index(request):
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'movies/index.html', context)
    
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def create(request):
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user = request.user
                movie.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm()
        context = {
            'form': form,
        }
        return render(request, 'movies/create.html', context)
    
    
    @require_safe
    def detail(request, pk):
        movie = Movie.objects.get(pk=pk)
        comments = movie.comment_set.all()
        comment_form = CommentForm()
        context = {
            'movie': movie,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'movies/detail.html', context)
    
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
        movie = Movie.objects.get(pk=pk)
        if request.user == movie.user:
            if request.method == 'POST':
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                    form.save()
                    return redirect('movies:detail', movie.pk)
            else:
                form = MovieForm(instance=movie)
            context = {
                'movie': movie,
                'form': form,
            }
        return render(request, 'movies/update.html', context)
    
    
    @require_POST
    def delete(request, pk):
        movie = Movie.objects.get(pk=pk)
        if request.user.is_authenticated:
            if request.user == movie.user:
                movie.delete()
                return redirect('movies:index')
        return redirect('movies:detail', movie.pk)
    
    
    @require_POST
    def comments_create(request, pk):
        if request.user.is_authenticated:
            movie = Movie.objects.get(pk=pk)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.movie = movie
                comment.user = request.user
                comment.save()
            return redirect('movies:detail', movie.pk)
        return redirect('accounts:login')
    
    
    @require_POST
    def comments_delete(request, movie_pk, comment_pk):
        if request.user.is_authenticated:
            comment = Comment.objects.get(pk=comment_pk)
            if request.user == comment.user:
                comment.delete()
        return redirect('movies:detail', movie_pk)
    ```

- ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ

    - ๋๊ธ์ ์์ฑํ๋ ํจ์์์ `.save(commit=False)` ์์ฑ์ผ๋ก ์ธ๋ํค๋ฅผ ๋ณ๋๋ก ์ง์ ํด์ค ๋ค์ ๊ฐ์ฒด๋ฅผ ์ ์ฅํ๋ ๊ฒ



## F. accounts/views.py

- ์๊ตฌ์ฌํญ

    |   View ํจ์๋ช   |                             ์ญํ                              | ํ์ฉ HTTP Method |
    | :-------------: | :----------------------------------------------------------: | :--------------: |
    |      login      |         login.html ๋ ๋๋ง & ํ์์ ๋ก๊ทธ์ธ ๊ณผ์  ์งํ          |    GET & POST    |
    |     logout      |          DB์ ํด๋ผ์ด์ธํธ ์ฟ ํค์์ ์ธ์ ๋ฐ์ดํฐ ์ญ์            |       POST       |
    |     signup      | signup.html ๋ ๋๋ง<br/>& ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ํ์ ๋ฐ์ดํฐ ์ ์ฅ ํ index.html ๋ฆฌ๋ค์ด๋ ํธ |    GET & POST    |
    |     update      | ์์  ๋์ ํ์ ๋ฐ์ดํฐ ์กฐํ ๋ฐ update.html ๋ ๋๋ง<br/>& ์ ํจ์ฑ ๊ฒ์ฆ ๋ฐ ํ์ ๋ฐ์ดํฐ ์์  ํ index.html ๋ฆฌ๋ค์ด๋ ํธ |    GET & POST    |
    |     delete      |        ๋จ์ผ ํ์ ๋ฐ์ดํฐ ์ญ์  ๋ฐ index.html ๋ฆฌ๋ค์ด๋ ํธ        |       POST       |
    | change_password | change_password.html ๋ ๋๋ง<br/>& ๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ ๋ฐ index.html ๋ฆฌ๋ค์ด๋ ํธ |    GET & POST    |

- ์ฝ๋

    ```python
    from django.contrib.auth import login as auth_login
    from django.contrib.auth import logout as auth_logout
    from django.contrib.auth import update_session_auth_hash, get_user_model
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
    from django.shortcuts import redirect, render
    from django.views.decorators.http import require_http_methods, require_POST
    
    from .forms import CustomUserChangeForm, CustomUserCreationForm
    
    
    # Create your views here.
    @require_http_methods(['GET', 'POST'])
    def login(request):
        if request.user.is_authenticated:
            return redirect('movies:index')
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'movies:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    
    
    @require_POST
    def logout(request):
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('movies:index')
    
    
    @require_http_methods(['GET', 'POST'])
    def signup(request):
        if request.user.is_authenticated:
            return redirect('movies:index')
            
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('movies:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    
    
    @require_POST
    def delete(request):
        if request.user.is_authenticated:
            request.user.delete()
            auth_logout(request)
        return redirect('movies:index')
    
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def update(request):
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('movies:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    
    
    @login_required
    @require_http_methods(['GET', 'POST'])
    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('movies:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    
    
    def profile(request, username):
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person': person,
        }
        return render(request, 'accounts/profile.html', context)
    ```

    

## G. movies/admin.py

- ์๊ตฌ์ฌํญ

  - ๋ชจ๋ธ Movie, Comment๋ฅผ Admin site์ ๋ฑ๋กํฉ๋๋ค.
  - Admin site์์ ๋ฐ์ดํฐ์ ์์ฑ, ์กฐํ, ์์ , ์ญ์ ๊ฐ ๊ฐ๋ฅํด์ผ ํฉ๋๋ค.

- ์ฝ๋

  ```python
  from django.contrib import admin
  
  from .models import Comment, Movie
  
  # Register your models here.
  admin.site.register(Movie)
  admin.site.register(Comment)
  ```

  

## H. accounts/admin.py

- ์๊ตฌ์ฌํญ

    - ๋ชจ๋ธ User๋ฅผ Admin site์ ๋ฑ๋กํฉ๋๋ค.
    - Admin site์์ ๋ฐ์ดํฐ์ ์์ฑ, ์กฐํ, ์์ , ์ญ์ ๊ฐ ๊ฐ๋ฅํด์ผ ํฉ๋๋ค.

- ์ฝ๋

    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    
    from .models import User
    
    # Register your models here.
    admin.site.register(User, UserAdmin)
    ```

    

## I. movies/forms.py

- ์๊ตฌ์ฌํญ

    - Movie ๋ชจ๋ธ๊ณผ Comment ๋ชจ๋ธ์ ๋ฐ์ดํฐ ๊ฒ์ฆ, ์ ์ฅ, ์๋ฌ๋ฉ์์ง, HTML์ ๋ชจ๋ ๊ด๋ฆฌํ๊ธฐ ์ํด ์ ์ ํ ModelForm์ ์ฌ์ฉํฉ๋๋ค.

- ์ฝ๋

    ```python
    from django import forms
    
    from .models import Comment, Movie
    
    
    class MovieForm(forms.ModelForm):
        title = forms.CharField(
            widget = forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
        )
    
        description = forms.CharField(
            widget = forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
            })
        )
    
        class Meta:
            model = Movie
            exclude = ('user',)
            
    
    class CommentForm(forms.ModelForm):
        
        class Meta:
            model = Comment
            exclude = ('user', 'movie',)
    ```

- ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ

    - exclude ์์ฑ์ ์ฌ์ฉํ์ฌ ์ธ๋ ํค ํ๋๋ฅผ ์ถ๋ ฅ์์ ์ ์ธํ๋ ๊ฒ



## J. accounts/forms.py

- ์๊ตฌ์ฌํญ

    - User ๋ชจ๋ธ์ ๋ฐ์ดํฐ ๊ฒ์ฆ, ์ ์ฅ, ์๋ฌ๋ฉ์์ง, HTML์ ๋ชจ๋ ๊ด๋ฆฌํ๊ธฐ ์ํด ์ ์ ํ Form๊ณผ ModelForm ๊ทธ๋ฆฌ๊ณ  ์ปค์คํ ModelForm์ ์ฌ์ฉํฉ๋๋ค.

- ์ฝ๋

    ```python
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserChangeForm, UserCreationForm
    
    
    class CustomUserCreationForm(UserCreationForm):
    
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',)
    
    
    class CustomUserChangeForm(UserChangeForm):
    
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('first_name', 'last_name',)
    ```

- ๋ด๊ฐ ์๊ฐํ๋ ์ด ๋ฌธ์ ์ ํฌ์ธํธ

    - `get_user_model()`์ ์ด์ฉํ์ฌ ํ์ฌ ํ์ฑํ๋ User ๋ชจ๋ธ์ ์ง์ ํด์ฃผ๋ ๊ฒ



## K. base.html

- ๊ณตํต ๋ถ๋ชจ ํํ๋ฆฟ
- ์๊ตฌ์ฌํญ
    - ๋ชจ๋  ํํ๋ฆฟ ํ์ผ์ base.html์ ์์๋ฐ์ ์ฌ์ฉํฉ๋๋ค.
    - nav ํ๊ทธ๋ฅผ ์ฌ์ฉํ ์๋จ ๋ค๋น๊ฒ์ด์ ๋ฐ๊ฐ ์์ต๋๋ค.
    - ๋ค๋น๊ฒ์ด์ ๋ฐ๋ ํ์์ ๋ก๊ทธ์ธ, ๋น๋ก๊ทธ์ธ ์ํ์ ๋ฐ๋ผ ๋ค๋ฅธ ๋งํฌ๋ฅผ ์ถ๋ ฅํฉ๋๋ค.

- ์ฝ๋

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  {% block title %}
  {% endblock title %}
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');

    body {
        font-family: 'Nanum Myeongjo', serif;
        background-color: black;
        color: white;
    }
  </style>
  <style type="text/css">
      a:link { color: #ffffff;}	
      a:visited { color: #ffffff;}
      a:hover { color: gray;}
  </style>
</head>
<body>
  <div class="container mt-3">
    {% if request.user.is_authenticated %}
      <nav class="d-flex justify-content-between my-2">
        <div class="d-flex">
          <b><a href="{% url 'accounts:profile' user.username %}">{{ user.first_name }}&nbsp;{{ user.last_name }}</a></b><p>๋ ๋ฐ๊ฐ์ต๋๋ค.</p>
          
        </div>
        <div class="d-flex">
          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout" style="border: none; background-color: black; color: white; text-decoration: underline;">
          </form>
        </div>
      </nav>
    {% else %}
      <nav class="d-flex justify-content-end my-2">
        <a href="{% url 'accounts:login' %}">Login</a>
        <p>&nbsp;</p>
        <a href="{% url 'accounts:signup' %}">Signup</a>
      </nav>
    {% endif %}
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```



## L. movies/index.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 8.54.16](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 8.54.16.png)

- ์ ์ฒด ์ํ ๋ชฉ๋ก ์กฐํ ํ์ด์ง

- ์๊ตฌ์ฌํญ

    - ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์กด์ฌํ๋ ๋ชจ๋  ์ํ์ ๋ชฉ๋ก์ ํ์ํฉ๋๋ค.
    - ์ ์ ํ HTML ์์๋ฅผ ์ฌ์ฉํ์ฌ ์ํ ์ ๋ชฉ์ ํ์ํ๋ฉฐ,
        ์ ๋ชฉ ํด๋ฆญ ์ ํด๋น ์ํ์ ์์ธ ์กฐํ ํ์ด์ง(detail.html)๋ก ์ด๋ํฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>Movies</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">Movies</h1>
      <br>
      {% for movie in movies %}
        <a href="{% url 'movies:detail' movie.pk %}" class="d-flex justify-content-center">{{ movie.title }}</a>
        <hr>
      {% endfor %}
    {% endblock content %}
    ```



## M. movies/detail.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.05.37](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.05.37.png)
- ์ํ ์์ธ ์ ๋ณด ํ์ด์ง
- ์๊ตฌ์ฌํญ
    - ํน์  ์ํ์ ์์ธ ์ ๋ณด๋ฅผ ํ์ํฉ๋๋ค.
    - ๋๊ธ์ ์์ฑํ  ์ ์๋ form์ ํ์ํฉ๋๋ค.
    - ๋๊ธ ์ญ์  ๋ฒํผ์ ๋๊ธ ์์ฑ์์๊ฒ๋ง ํ์ํฉ๋๋ค.
    - ํด๋น ์ํ์ ์์  ๋ฐ ์ญ์  ๋ฒํผ์ ํ์ํฉ๋๋ค.
    - ์ ์ฒด ์ํ ๋ชฉ๋ก ์กฐํ ํ์ด์ง(index.html)๋ก ์ด๋ํ๋ ๋งํฌ๋ฅผ ํ์ํฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>{{ movie.title }}</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">{{ movie.title }}</h1>
      <div class="d-flex justify-content-end">
        <p style="opacity: 0.8;">Written by</p>&nbsp;
        <a href="{% url 'accounts:profile' movie.user.username %}" style="opacity: 0.8;">{{ user.first_name }}&nbsp;{{ user.last_name }}</a>
      </div>
      <p>{{ movie.description }}</p>
      {% if request.user == movie.user %}
        <div class="d-flex justify-content-end">
        <a href="{% url 'movies:update' movie.pk %}" style="opacity: 0.8;">Update</a>
        <form action="{% url 'movies:delete' movie.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="Delete" style="border: none; background-color: black; color: white; text-decoration: underline; opacity: 0.8;">
        </form>
        </div>
      {% endif %}
      <hr>
      <h4>Comments</h4>
      {% if comments %}
        <p style="opacity: 0.8;">There are {{ comments|length }} comments.</p>
      {% endif %}
      <ul>
        {% for comment in comments %}
          <li class="d-flex justify-content-between">
            {{ comment.user }} - {{ comment.content }}
            {% if request.user == comment.user %}
              <form action="{% url 'movies:comments_delete' movie.pk comment.pk %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="Delete" style="border: none; background-color: black; color: white; text-decoration: underline; opacity: 0.8;">
              </form>
            {% endif %}
          </li>
        {% empty %}
          <li>No comments yet.</li>
        {% endfor %}
      </ul>
      {% if request.user.is_authenticated %}
        <form action="{% url 'movies:comments_create' movie.pk %}" method="POST">
          {% csrf_token %}
          {{ comment_form }}
          <input type="submit" value="Submit">
        </form>
      {% else %}
        <a href="{% url 'accounts:login' %}">Log in to write comment.</a>
      {% endif %}
      <hr>
      <a href="{% url 'movies:index' %}" style="opacity: 0.8;">Back</a>
    {% endblock content %}
    ```



## N. movies/create.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.07.45](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.07.45.png)

- ์ํ ์์ฑ ํ์ด์ง
- ์๊ตฌ์ฌํญ
  - ํน์  ์ํ๋ฅผ ์์ฑํ๊ธฐ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
  - ํ์๋๋ form์ Movie ๋ชจ๋ธ ํด๋์ค์ ๊ธฐ๋ฐํ ModelForm์ด์ด์ผ ํฉ๋๋ค.
  - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ๋จ์ผ ์ํ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๋ URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.
  - ์ ์ฒด ์ํ ๋ชฉ๋ก ์กฐํ ํ์ด์ง(index.html)๋ก ์ด๋ํ๋ ๋งํฌ๋ฅผ ํ์ํฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>Create</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">Create</h1>
      <form action="{% url 'movies:create' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
      </form>
      <hr>
      <a href="{% url 'movies:index' %}">Back</a>
    {% endblock content %}
    ```



## O. movies/update.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.12.24](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.12.24.png)

- ์ํ ์์  ํ์ด์ง
- ์๊ตฌ์ฌํญ
  - ํน์  ์ํ๋ฅผ ์์ ํ๊ธฐ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
  - ํ์๋๋ form์ Movie ๋ชจ๋ธ ํด๋์ค์ ๊ธฐ๋ฐํ ModelForm์ด์ด์ผ ํฉ๋๋ค.
  - HTML input ์์์๋ ๊ธฐ์กด ๋ฐ์ดํฐ๋ฅผ ์ถ๋ ฅํฉ๋๋ค.
  - Reset ๋ฒํผ์ ์ฌ์ฉ์์ ๋ชจ๋  ์๋ ฅ์ ์ด๊ธฐ ๊ฐ์ผ๋ก ์ฌ์ค์ ํฉ๋๋ค.
  - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ๋จ์ผ ์ํ ๋ฐ์ดํฐ๋ฅผ ์์ ํ๋ URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.
  - ์ํ ์์ธ ์ ๋ณด ํ์ด์ง(detail.html)๋ก ์ด๋ํ๋ ๋งํฌ๋ฅผ ํ์ํฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>{{ movie.title }}</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">{{ movie.title }}</h1>
      <form action="{% url 'movies:update' movie.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="reset" value="Reset">
        <input type="submit" value="Submit">
      </form>
      <hr>
      <a href="{% url 'movies:detail' movie.pk %}">Back</a>
    {% endblock content %}
    ```



## P. accounts/login.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.14.41](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.14.41.png)

- ๋ก๊ทธ์ธ ํ์ด์ง

- ์๊ตฌ์ฌํญ

    - ๋ก๊ทธ์ธ์ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
    - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ๋ก๊ทธ์ธ URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>Login</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">Login</h1>
      <br>
      <form action="" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
      </form>
    {% endblock content %}
    ```



## Q. accounts/signup.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.16.15](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.16.15.png)

- ํ์๊ฐ์ ํ์ด์ง

- ์๊ตฌ์ฌํญ

    - ํ์๊ฐ์์ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
    - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ํ์๊ฐ์ URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>Signup</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">Signup</h1>
      <br>
      <form action="{% url 'accounts:signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
      </form>
    {% endblock content %}
    ```



## R. accounts/update.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.17.51](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.17.51.png)

- ํ์ ์ ๋ณด ์์  ํ์ด์ง
- ์๊ตฌ์ฌํญ
    - ํ์ ์ ๋ณด ์์ ์ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
    - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ํ์ ์ ๋ณด ์์  URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.

- ์ฝ๋

    ```html
    {% extends 'base.html' %}
    
    {% block title %}
      <title>User Information Edit</title>
    {% endblock title %}
    
    {% block content %}
      <h1 class="d-flex justify-content-center">User Information Edit</h1>
      <br>
      <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
      </form>
    {% endblock content %}
    ```

    

## S. accounts/change_password.html

![แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.20.33](README.assets/แแณแแณแแตแซแแฃแบ 2022-10-16 แแฉแแฎ 9.20.33.png)

- ๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ ํ์ด์ง
- ์๊ตฌ์ฌํญ
    - ๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ์ ์ํ HTML form ์์๋ฅผ ํ์ํฉ๋๋ค.
    - ์์ฑํ ์ ๋ณด๋ ์ ์ถ(submit) ์ ๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ URL๋ก ์์ฒญ๊ณผ ํจ๊ป ์ ์ก๋ฉ๋๋ค.
