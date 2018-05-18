from django.urls import path, include

#ViewSets
from rest_framework import routers

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#ViewSets
router = routers.DefaultRouter()



app_name = 'rest_app'

router.register(r'albums', views.AlbumViewSet)
router.register(r'tracks', views.TrackViewSet)

urlpatterns=[
    #ViewSets
    path('', include(router.urls)),
]
#    path('albums/', views.AlbumList.as_view()),
    # generics
#    path('albums/<int:pk>', views.AlbumDetail.as_view()),
#    path('tracks/', views.TrackList.as_view()),
#    path('tracks/<int:pk>', views.TrackDetail.as_view()),

#urlpatterns = format_suffix_patterns(urlpatterns)

