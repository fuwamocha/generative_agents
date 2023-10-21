"""frontend_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from translator import views as translator_views

urlpatterns = [
    path('', translator_views.landing, name='landing'),
    path('simulator_home/', translator_views.home, name='home'),
    path('demo/<slug:sim_code>/<slug:step>/<slug:play_speed>/',
         translator_views.demo, name='demo'),
    path('replay/<slug:sim_code>/<slug:step>/',
         translator_views.replay, name='replay'),
    path('replay_persona_state/<slug:sim_code>/<slug:step>/<slug:persona_name>/',
         translator_views.replay_persona_state, name='replay_persona_state'),
    path('process_environment/', translator_views.process_environment,
         name='process_environment'),
    path('update_environment/', translator_views.update_environment,
         name='update_environment'),
    path('path_tester/', translator_views.path_tester, name='path_tester'),
    path('path_tester_update/', translator_views.path_tester_update,
         name='path_tester_update'),
    path('admin/', admin.site.urls),
]
