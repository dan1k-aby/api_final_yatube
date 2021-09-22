from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

import api.views


router = routers.DefaultRouter()
router.register(r'posts', api.views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', api.views.CommentViewSet,
                basename='comments')
router.register(r'groups', api.views.GroupViewSet, basename='group')
router.register(r'follow', api.views.FollowViewSet, basename='follow')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/', include('api.urls')),
    path('api/v1/', include(router.urls)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
