�
�w�Pc           @   sB   d  Z  d d l Z e j j d d � d d l m Z e �  Z d S(   s�  
WSGI config for brabsite project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

i����Nt   DJANGO_SETTINGS_MODULEs   brabsite.settings(   t   get_wsgi_application(   t   __doc__t   ost   environt
   setdefaultt   django.core.wsgiR   t   application(    (    (    s:   /Users/criticus/virtual_projects/brabsite/brabsite/wsgi.pyt   <module>   s   