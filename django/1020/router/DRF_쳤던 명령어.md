mkdir account_auth
cd account_auth

django-admin startproject tutorialdjango .
python manage.py migrate

# settings.py에서 접속할 수 있는 사람 설정
ALLOWED_HOSTS = ['*'] # 28번째 줄에 접속할 수 있는 사람을 모든 사람으로 변경

python manage.py startapp book

# settings.py 에서 33번째 라인 수정
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book',
]

###################################

'DIRS': [ BASE_DIR / 'templates' ],

###################################

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

###################################

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

###################################

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

###################################

# 폴더 만들기
mysite > static
mysite > media

###################################

python manage.py createsuperuser

leehojun
leehojun@gmail.com
이호준123!@

###################################
# blog > models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

###################################

python manage.py makemigrations
python manage.py migrate