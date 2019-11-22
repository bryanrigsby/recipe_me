from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.clear),
    url(r'^register_def$', views.register),
    url(r'^register_page$', views.register_page),
    url(r'^login_def$', views.login),
    url(r'^login_page$', views.login_page),
    url(r'^success$', views.success),
    url(r'^main$', views.main),
    url(r'^user_bio/(?P<id>[0-9]+)$', views.user_bio),
    url(r'^edit_user/(?P<id>[0-9]+)$', views.edit_user),
    url(r'^show_recipe/(?P<id>[0-9]+)$', views.show_recipe),
    url(r'^add_recipe_page$', views.add_recipe_page),
    url(r'^add_recipe$', views.add_recipe),
    url(r'^edit_recipe_page/(?P<id>[0-9]+)$', views.edit_recipe_page),
    url(r'^edit_recipe$', views.edit_recipe),
    url(r'^like$', views.like),
    url(r'^unlike$', views.unlike),
    url(r'^comment/(?P<id>[0-9]+)$', views.comment),
    url(r'^delete_comment/(?P<id>[0-9]+)$', views.delete_comment),
    url(r'^delete$', views.delete),
    url(r'^clear$', views.clear),
]