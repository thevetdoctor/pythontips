# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Tip
from .models import Link

admin.site.register(Tip)
admin.site.register(Link)
