from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^choice/$', views.SubjectView.as_view(), name='choice'),
    url(r'^physics/$', views.PhysicsView.as_view(), name='Physics'),
    url(r'^mathematics/$', views.MathematicsView.as_view(), name='Mathematics'),
    url(r'^chemistry/$', views.ChemistryView.as_view(), name='Chemistry'),
    url(r'^english/$', views.EnglishView.as_view(), name='English'),
    url(r'^result/$', views.result, name='result'),
]
