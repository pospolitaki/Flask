from django.urls import path
#from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#router = routers.SimpleRouter()
#router.register(r'users', )


app_name = 'rest_app'

urlpatterns=[
    path('statuses/', views.StatusList.as_view()),
    path('statuses/<int:pk>', views.StatusDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

