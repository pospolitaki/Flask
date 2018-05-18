from django.conf.urls import url

from django.contrib.auth.views import logout_then_login, login
from django.views.generic import CreateView

from pizza_auth_app.forms import CustomCreationForm

app_name = 'pizza_auth_app'

urlpatterns = [
    url(r'^login/', login, {'template_name': 'auth_app/login.html'
    }, name='login'),

    url(r'^logout/', logout_then_login, name='logout'),

    url(r'^register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=CustomCreationForm,
        success_url='/',
    ), name='register'),
]
