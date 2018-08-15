from django.conf.urls import url
from django.contrib import admin
from main.views import (
    quiz_crm, quiz_create
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz_crm/', quiz_crm, name='quiz_crm'),
    url(r'^quiz_create/', quiz_create, name='quiz_create'),
]
