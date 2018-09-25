"""I2P URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from I2P import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.allindex),
    # i2p home
    url(r'^i2p/$', views.index),
    # i2p topology
    url(r'^topology/$', views.toplogyhandler),
    url(r'^points/$', views.pointshandler),
    # i2p traffic
    url(r'^traffic/$', views.traffichandler),
    url(r'^trafficdata/$', views.trafficdatahandler),
    # i2p hiddensite
    url(r'^hiddensite/$', views.hiddensitehandler),
    url(r'^officialdata/$', views.officaldatahandler),
    url(r'^searchdata/$', views.searchdatahandler),
    url(r'^floodfilldata/$', views.floodfilldatahandler),
    url(r'^extendata/$', views.extenddatahandler),
    url(r'^alldata/$', views.alldatahandler),
    url(r'^onlinedata/$', views.onlinedatahandler),
]
