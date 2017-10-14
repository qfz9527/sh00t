from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^flags/$', views.flags),
    url(r'^flags/all/', views.flags_all),
    url(r'^flag/([0-9]+)/$', views.flag),
    url(r'^sh0ts/$', views.sh0ts),
    url(r'^sh0t/([0-9]+)/$', views.sh0t),
    url(r'^assessments/$', views.assessments),
    url(r'^assessment/([0-9]+)/$', views.assessment),
    url(r'^projects/$', views.projects),
    url(r'^project/([0-9]+)/$', views.project),
    url(r'^templates/$', views.templates),
    url(r'^template/([0-9]+)/$', views.template),
    url(r'^case-masters/$', views.case_masters),
    url(r'^case-master/([0-9]+)/$', views.case_master),
    url(r'^module-masters/$', views.module_masters),
    url(r'^module-master/([0-9]+)/$', views.module_master),
    url(r'^methodology-masters/$', views.methodology_masters),
    url(r'^methodology-master/([0-9]+)/$', views.methodology_master),
]