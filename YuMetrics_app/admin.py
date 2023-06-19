from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Metric, Mistake, Result

admin.site.register(User)
admin.site.unregister(Group)

admin.site.register(Metric)
admin.site.register(Mistake)
admin.site.register(Result)
