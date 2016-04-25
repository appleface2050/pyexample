# coding=utf-8

from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.





from django.db import models
from util.basemodel import JSONBaseModel



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class BSUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email or not username:
            raise ValueError('Users must have an email address and a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class BSUser(AbstractBaseUser, JSONBaseModel):
    """
    用户表
    """
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    tel = models.CharField(max_length=20, unique=True, null=True, blank=True, help_text=u'手机号')
    email = models.CharField(_('email'), null=True, max_length=128, unique=True)
    # password = models.CharField(_('password'), max_length=128)
    # last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    # realname = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'真实姓名', help_text=u'真实姓名',default="")
    # sex = models.NullBooleanField(default=None, verbose_name=u'性别')
    # icon_url = models.ForeignKey(BaseFile, null=True, blank=True, verbose_name=u'默认头像')
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    create_time = models.DateTimeField(_('date joined'), default=timezone.now)
    # hxpassword = models.CharField(max_length=50, null=True, verbose_name=u'环信密码')
    # hx_reg = models.BooleanField(default=False, db_index=True, verbose_name=u'是否注册过环信')

    # guanzhu = models.ManyToManyField('Project', null=True, blank=True, verbose_name=u'关注项目')

    # objects = BaseUserManager()
    objects = BSUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return unicode(self.name)



