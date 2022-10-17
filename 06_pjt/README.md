# 06_PJT

## 🎁 이번 PJT를 통해 배운 내용

- Authentication System을 이용하여 사용자 권한을 설정하는 법
- DB 테이블 간 N:1 관계를 형성하는 법



## A. movies/models.py

- 요구사항

  - 정의할 모델 클래스의 이름은 Movie이며, 다음과 같은 정보를 저장합니다.

    |   필드명    | 데이터 유형 |            역할            |
    | :---------: | :---------: | :------------------------: |
    |    title    | varchar(20) |         영화 제목          |
    | description |    text     |           줄거리           |
    |   user_id   |   integer   | 외래 키 (User 클래스 참조) |

  - 정의할 모델 클래스의 이름은 Comment이며, 다음과 같은 정보를 저장합니다.

      |  필드명  | 데이터 유형  |            역할             |
      | :------: | :----------: | :-------------------------: |
      | content  | varchar(100) |          댓글 내용          |
      | movie_id |   integer    | 외래 키 (Movie 클래스 참조) |
      | user_id  |   interger   | 외래 키 (User 클래스 참조)  |

- 코드

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

- 내가 생각하는 이 문제의 포인트
  - ForeignKey를 사용해 다른 모델 클래스를 연결하는 것



## B. accounts/models.py

- 요구사항

  - 정의할 모델 클래스의 이름은 User이며, AbstractUser 모델 클래스를 상속받는 커스텀 모델을 사용합니다.

- 코드

    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models
    
    
    # Create your models here.
    class User(AbstractUser):
        pass
    ```



## C. movies/urls.py

- 요구사항

  |                     URL 패턴                     |                           역할                            |
  | :----------------------------------------------: | :-------------------------------------------------------: |
  |                     /movies/                     |                전체 영화 목록 페이지 조회                 |
  |                 /movies/create/                  | 새로운 영화 생성 페이지 조회<br/> & 단일 영화 데이터 저장 |
  |                  /movies/<pk>/                   |                단일 영화 상세 페이지 조회                 |
  |               /movies/<pk>/update/               |  기존 영화 수정 페이지 조회<br/> & 단일 영화 데이터 수정  |
  |               /movies/<pk>/delete/               |                   단일 영화 데이터 삭제                   |
  |              /movies/<pk>/comments               |                   단일 댓글 데이터 저장                   |
  | /movies/<movie_pk>/comments/<comment_pk>/delete/ |                   단일 댓글 데이터 삭제                   |

- 코드

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

- 요구사항
  |      URL 패턴       |                             역할                             |
  | :-----------------: | :----------------------------------------------------------: |
  |  /accounts/login/   |    로그인 페이지 조회 & 세션 데이터 생성 및 저장 (로그인)    |
  |  /accounts/logout/  |                 세션 데이터 삭제 (로그아웃)                  |
  |  /accounts/signup/  |   회원 생성 페이지 조회 & 단일 회원 데이터 생성 (회원가입)   |
  |  /accounts/delete/  |              단일 회원 데이터 삭제 (회원 탈퇴)               |
  |  /accounts/update/  | 회원 정보 수정 페이지 조회 & 단일 회원 데이터 수정 (회원 정보 수정) |
  | /accounts/password/ | 비밀번호 수정 페이지 조회 & 단일 비밀번호 데이터 수정 (비밀번호 변경) |
  
- 코드

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

- 요구사항

    |   View 함수명   |                             역할                             | 허용 HTTP Method |
    | :-------------: | :----------------------------------------------------------: | :--------------: |
    |      index      |          전체 영화 데이터 조회 및 index.html 렌더링          |       GET        |
    |     create      | create.html 렌더링<br/>& 유효성 검증 및 영화 데이터 저장 후 detail.html 리다이렉트 |    GET & POST    |
    |     detail      |         단일 영화 데이터 조회 및 detail.html 렌더링          |       GET        |
    |     update      | 수정 대상 영화 데이터 조회 및 update.html 렌더링<br/>& 유효성 검증 및 영화 데이터 수정 후 detail.html 리다이렉트 |    GET & POST    |
    |     delete      |        단일 영화 데이터 삭제 및 index.html 리다이렉트        |       POST       |
    | comments_create |  유효성 검증 및 댓글 데이터 저장 후 detail.html 리다이렉트   |       POST       |
    | comments_delete |       단일 댓글 데이터 삭제 및 detail.html 리다이렉트        |       POST       |

- 코드

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

- 내가 생각하는 이 문제의 포인트

    - 댓글을 생성하는 함수에서 `.save(commit=False)` 속성으로 외래키를 별도로 지정해준 다음 객체를 저장하는 것



## F. accounts/views.py

- 요구사항

    |   View 함수명   |                             역할                             | 허용 HTTP Method |
    | :-------------: | :----------------------------------------------------------: | :--------------: |
    |      login      |         login.html 렌더링 & 회원의 로그인 과정 진행          |    GET & POST    |
    |     logout      |          DB와 클라이언트 쿠키에서 세션 데이터 삭제           |       POST       |
    |     signup      | signup.html 렌더링<br/>& 유효성 검증 및 회원 데이터 저장 후 index.html 리다이렉트 |    GET & POST    |
    |     update      | 수정 대상 회원 데이터 조회 및 update.html 렌더링<br/>& 유효성 검증 및 회원 데이터 수정 후 index.html 리다이렉트 |    GET & POST    |
    |     delete      |        단일 회원 데이터 삭제 및 index.html 리다이렉트        |       POST       |
    | change_password | change_password.html 렌더링<br/>& 비밀번호 변경 및 index.html 리다이렉트 |    GET & POST    |

- 코드

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

- 요구사항

  - 모델 Movie, Comment를 Admin site에 등록합니다.
  - Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야 합니다.

- 코드

  ```python
  from django.contrib import admin
  
  from .models import Comment, Movie
  
  # Register your models here.
  admin.site.register(Movie)
  admin.site.register(Comment)
  ```

  

## H. accounts/admin.py

- 요구사항

    - 모델 User를 Admin site에 등록합니다.
    - Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야 합니다.

- 코드

    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    
    from .models import User
    
    # Register your models here.
    admin.site.register(User, UserAdmin)
    ```

    

## I. movies/forms.py

- 요구사항

    - Movie 모델과 Comment 모델의 데이터 검증, 저장, 에러메시지, HTML을 모두 관리하기 위해 적절한 ModelForm을 사용합니다.

- 코드

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

- 내가 생각하는 이 문제의 포인트

    - exclude 속성을 사용하여 외래 키 필드를 출력에서 제외하는 것



## J. accounts/forms.py

- 요구사항

    - User 모델의 데이터 검증, 저장, 에러메시지, HTML을 모두 관리하기 위해 적절한 Form과 ModelForm 그리고 커스텀 ModelForm을 사용합니다.

- 코드

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

- 내가 생각하는 이 문제의 포인트

    - `get_user_model()`을 이용하여 현재 활성화된 User 모델을 지정해주는 것



## K. base.html

- 공통 부모 템플릿
- 요구사항
    - 모든 템플릿 파일은 base.html을 상속받아 사용합니다.
    - nav 태그를 사용한 상단 네비게이션 바가 있습니다.
    - 네비게이션 바는 회원의 로그인, 비로그인 상태에 따라 다른 링크를 출력합니다.

- 코드

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
          <b><a href="{% url 'accounts:profile' user.username %}">{{ user.first_name }}&nbsp;{{ user.last_name }}</a></b><p>님 반갑습니다.</p>
          
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

![스크린샷 2022-10-16 오후 8.54.16](README.assets/스크린샷 2022-10-16 오후 8.54.16.png)

- 전체 영화 목록 조회 페이지

- 요구사항

    - 데이터베이스에 존재하는 모든 영화의 목록을 표시합니다.
    - 적절한 HTML 요소를 사용하여 영화 제목을 표시하며,
        제목 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동합니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.05.37](README.assets/스크린샷 2022-10-16 오후 9.05.37.png)
- 영화 상세 정보 페이지
- 요구사항
    - 특정 영화의 상세 정보를 표시합니다.
    - 댓글을 작성할 수 있는 form을 표시합니다.
    - 댓글 삭제 버튼은 댓글 작성자에게만 표시합니다.
    - 해당 영화의 수정 및 삭제 버튼을 표시합니다.
    - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.07.45](README.assets/스크린샷 2022-10-16 오후 9.07.45.png)

- 영화 생성 페이지
- 요구사항
  - 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
  - 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
  - 작성한 정보는 제출(submit) 시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송됩니다.
  - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.12.24](README.assets/스크린샷 2022-10-16 오후 9.12.24.png)

- 영화 수정 페이지
- 요구사항
  - 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
  - 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
  - HTML input 요소에는 기존 데이터를 출력합니다.
  - Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정합니다.
  - 작성한 정보는 제출(submit) 시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송됩니다.
  - 영화 상세 정보 페이지(detail.html)로 이동하는 링크를 표시합니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.14.41](README.assets/스크린샷 2022-10-16 오후 9.14.41.png)

- 로그인 페이지

- 요구사항

    - 로그인을 위한 HTML form 요소를 표시합니다.
    - 작성한 정보는 제출(submit) 시 로그인 URL로 요청과 함께 전송됩니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.16.15](README.assets/스크린샷 2022-10-16 오후 9.16.15.png)

- 회원가입 페이지

- 요구사항

    - 회원가입을 위한 HTML form 요소를 표시합니다.
    - 작성한 정보는 제출(submit) 시 회원가입 URL로 요청과 함께 전송됩니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.17.51](README.assets/스크린샷 2022-10-16 오후 9.17.51.png)

- 회원 정보 수정 페이지
- 요구사항
    - 회원 정보 수정을 위한 HTML form 요소를 표시합니다.
    - 작성한 정보는 제출(submit) 시 회원 정보 수정 URL로 요청과 함께 전송됩니다.

- 코드

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

![스크린샷 2022-10-16 오후 9.20.33](README.assets/스크린샷 2022-10-16 오후 9.20.33.png)

- 비밀번호 변경 페이지
- 요구사항
    - 비밀번호 변경을 위한 HTML form 요소를 표시합니다.
    - 작성한 정보는 제출(submit) 시 비밀번호 변경 URL로 요청과 함께 전송됩니다.
