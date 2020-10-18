from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)
    username = models.CharField('Никнейм (показывается на сайте)', max_length=30, null=True, blank=False, unique=True)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    avatar = models.ImageField(upload_to='TeamLearning/user_avatars/', null=True, blank=True, verbose_name='Фото',
                               default='/TeamLearning/user_avatars/default_group_avatar.png')

    professionalism_coefficient = models.IntegerField(verbose_name='Коэффициент профессионализма', default=5,
                                                      null=False, blank=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Team(models.Model):
    creator = models.ForeignKey('User', on_delete=models.CASCADE, related_name='my_teams', verbose_name='Создатель')
    users = models.ManyToManyField(User, related_name='teams', verbose_name='Участники')
    requests = models.ManyToManyField(User, related_name='requests', verbose_name='Заявки')
    name = models.CharField(max_length=30, verbose_name='Название команды', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True)
    avatar = models.ImageField(upload_to='TeamLearning/team_avatars/', null=True, blank=True, verbose_name='Фото',
                               default='/TeamLearning/team_avatars/default_group_avatar.png')
    is_open = models.BooleanField(verbose_name='Открытое вступление?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class News(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор новости')
    post_header = models.CharField(max_length=255, verbose_name='Заголовок')
    post_text = models.TextField(verbose_name='Текст поста')
    post_image = models.ImageField(upload_to='TeamLearning/news_images/', null=True, blank=True, verbose_name='Фото',
                                   default='/TeamLearning/news_images/default_post_image.png')
    date = models.DateTimeField(verbose_name='Дата создания')

    def __str__(self):
        return self.post_header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Project(models.Model):
    creator = models.ForeignKey('User', on_delete=models.CASCADE, related_name='my_projects', verbose_name='Создатель',
                                null=False)
    project_name = models.CharField(max_length=30, verbose_name='Название проекта/хакатона')
    project_description = models.TextField(verbose_name='Описание проекта/хакатона')
    teams = models.ManyToManyField('Team', related_name='projects', verbose_name='Команды')
    requests = models.ManyToManyField('Team', related_name='projects_request',
                                      verbose_name='Заявки на участие в проекте/хакатоне')
    start_date = models.DateField(verbose_name='Дата начала проекта', null=False)
    dead_line = models.DateField(verbose_name='Deadline', null=True)
    is_open = models.BooleanField(verbose_name='Открытая запись?', null=False, default=False)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
