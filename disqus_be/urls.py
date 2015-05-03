"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from core_app.api import SiteResource
from core_app.api import CommentsResource

site_resource = SiteResource()
comment_resource = CommentsResource()

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(site_resource.urls)),
    (r'^api/v1/', include(comment_resource.urls)),
)
