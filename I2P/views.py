from django.http import HttpResponse
from django.shortcuts import render
import geoip2.database
import config
import json
from db.DB import BaseDB

db_topology = BaseDB(config.DB_Topology)
db_hiddensite = BaseDB(config.DB_HIDDENSERVER)


def allindex(request):
    return render(request, "index.html")


def index(request):
    return render(request, 'cover.html')


# i2p topology
def toplogyhandler(request):
    return render(request, 'echarts.html')


def pointshandler(request):
    result = db_topology.get_data_range("info", 0, 95000)
    points = []
    for res in result:
        dic = {"lat": res[2], "lng": res[3]}
        points.append(dic)
    return HttpResponse(json.dumps(points))


def allpointshandler(request):
    result = db_topology.get_data_range("all_info", 0, 95000)
    points = []
    dic = {}
    for res in result:
        print(res)
        reader = geoip2.database.Reader('./I2P/GeoLite2-City.mmdb')
        try:
            if str(res[2]).split('.').__len__() is 4:
                response = reader.city(res[2])
                lat = response.location.latitude
                lng = response.location.longitude
                reader.close()
                dic = {"lat": lat, "lng": lng}
        except geoip2.errors.AddressNotFoundError:
            dic = None
        if dic is not None:
            points.append(dic)
    print(dic.__len__())
    return HttpResponse(json.dumps(points))


# i2p traffic
def traffichandler(request):
    return render(request, 'traffic.html')


def trafficdatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_TRAFFIC, "*")
    num = 1
    for factor in res:
        site.append({"id": num, "srcip": factor[1], "srcport": factor[2], "destip": factor[3],
                     "destport": factor[4], "time": factor[5]})
        num += 1
    site.reverse()
    return HttpResponse(json.dumps(site))


# i2p hiddensite
def hiddensitehandler(request):
    return render(request, "hiddensite.html")


def officaldatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_OFFICIAL, "*")
    for factor in res:
        site.append({"id": factor[0], "site": factor[1], "site32": factor[2], "time": factor[4]})
    return HttpResponse(json.dumps(site))


def searchdatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_SEARCH, "*")
    for factor in res:
        site.append({"id": factor[0], "site": factor[1], "site32": factor[2], "time": factor[4]})
    return HttpResponse(json.dumps(site))


def floodfilldatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_FLOODFILL, "*")
    for factor in res:
        site.append({"id": factor[0], "site": factor[1], "site32": factor[2], "time": factor[4]})
    return HttpResponse(json.dumps(site))


def extenddatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_EXTEND, "*")
    for factor in res:
        site.append({"id": factor[0], "site": factor[1], "site32": factor[2], "time": factor[4]})
    return HttpResponse(json.dumps(site))


def alldatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_ALL, "*")
    for factor in res:
        site.append({"id": factor[0], "site": factor[1], "site32": factor[2], "time": factor[4]})
    return HttpResponse(json.dumps(site))


def onlinedatahandler(request):
    site = []
    res = db_hiddensite.get_attribute(config.DB_HIDDENSITE_ONLINE, "*")
    num = 1
    for factor in res:
        site.append({"id": num, "site": factor[1], "site32": factor[2], "time": factor[4]})
        num += 1
    return HttpResponse(json.dumps(site))
