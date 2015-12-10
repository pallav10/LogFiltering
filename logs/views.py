import re

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from logs.models import logdata
from logs.serializers import logdataSerializer
from logs.forms import DocumentForm
from django.http import HttpResponse
from django.db.models import Sum, Count, Min, Max, Avg
import json
from datetime import datetime


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'])
            # Redirect to the document list after POST
            #return HttpResponseRedirect('/logs/success')
            return HttpResponseRedirect('/logs/view')
            #return HttpResponseRedirect('logs.views.logdata')
    else:
        form = DocumentForm()   # A empty, unbound form
    # Load documents for the list page
    # Render list page with the documents and the form
    return render_to_response(
        'logs/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def handle_uploaded_file(file):
    expr = re.compile('\"(?P<id1>([^-]*))[^ ]* (?P<elapsed_time>([\d]*)) (?P<client_ip>([.\d]*)) \"(?P<username>([^@]*))[^ ]*\" \"(?P<connection_id>([^ ]*))\" \[(?P<date>([^:]*))\:(?P<time>([^ ]*))] \"(?P<method_url>([^"]*))\" (?P<httpstatus>([\d]*)) (?P<byte_transferred>([\d]*)) \"(?P<referrer_url>([^"]*))\" \"(?P<user_agent>([^"]*))\" (?P<mime>([^ ]*)) \"(?P<filter_name>([^"]*))\" \"(?P<filter_profile>([^"]*))\" \"(?P<interface>([^"]*))')
    for line in file:
        temp = expr.search(line)
        id1 = temp.group("id1")
        elapsed_time1 = temp.group("elapsed_time")
        client_ip1 = temp.group("client_ip")
        username1 = temp.group("username")
        connection_id1 = temp.group("connection_id")
        date1 = temp.group("date")
        date2 = datetime.strptime(date1, "%d/%b/%Y")
        time1 = temp.group("time")
        method_url1 = temp.group("method_url")
        httpstatus1 = temp.group("httpstatus")
        byte_transferred1 = temp.group("byte_transferred")
        byte_transferred1 = int(byte_transferred1)
        referrer_url1 = temp.group("referrer_url")
        user_agent11 = temp.group("user_agent")
        user_agent12 = user_agent11.decode('utf32', 'ignore')#utf8
        mime1 = temp.group("mime")
        filter_name1 = temp.group("filter_name")
        filter_profile1 = temp.group("filter_profile")
        interface1 = temp.group("interface")
        log_store = logdata(
            log_id="%s" % id1,
            elapsed_time="%s" % elapsed_time1,
            client_ip="%s" % client_ip1,
            username="%s" % username1,
            connection_id="%s" % connection_id1,
            date="%s" % date2,
            time="%s" % time1,
            method_url="%s" % method_url1,
            http_status="%s" % httpstatus1,
            byte_transferred="%d" % byte_transferred1,
            referrer_url="%s" % referrer_url1,
            user_agent="%s" % user_agent12,
            mime="%s" % mime1,
            filter_name="%s" % filter_name1,
            filter_profile="%s" % filter_profile1,
            interface="%s" % interface1)
        log_store.save()
    return

def view(request):
    if request.method == 'GET':

        return render_to_response(
        'logs/view3_edited.html',
        context_instance=RequestContext(request)
    )

def success(request):
    if request.method == 'GET':

        return render_to_response(
        'logs/success.html',
        context_instance=RequestContext(request)
    )

        #start_date ="03/feb/2014",datetime.datetime.now()) # defaults to now
        #db_date = datetime.datetime.strptime(form_date,'%d/%m/%y')"""
        """startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('username').annotate(Sum('byte_transferred')).filter(date__range=[startdate, enddate])#logdata.objects.values('username').aggregate(Sum('byte_transferred')).filter(date__range=[startdate, enddate])#.aggregate(Sum(byte_transferred1)).annotate(Sum('byte_transferred')).distinct()
        queryset1= logdata.objects.values('mime').annotate(Count('mime')).filter(date__range=[startdate, enddate])
        queryset2= logdata.objects.values('filter_profile').annotate(Count('filter_profile')).filter(date__range=[startdate, enddate])
        queryset4 = logdata.objects.values('http_status').annotate(Count('http_status')).filter(date__range=[startdate, enddate])
        queryset5 = logdata.objects.values('filter_name').annotate(Count('filter_name')).filter(date__range=[startdate, enddate])
        queryset6 = logdata.objects.values('referrer_url').annotate(Count('referrer_url')).filter(date__range=[startdate, enddate])

        serializer = logdataSerializer(queryset1, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset6)
        return HttpResponse(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)
   """
    #return HttpResponse("Hello, the log file has been successfully parsed.")

def users(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('username').annotate(Sum('byte_transferred')).filter(date__range=[startdate, enddate])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))#(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)

def mime(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('mime').annotate(Count('mime')).filter(date__range=[startdate, enddate])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))#(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)


def profile(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('filter_profile').annotate(Count('filter_profile')).filter(date__range=[startdate, enddate])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))#(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)


def status(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('http_status').annotate(Count('http_status')).filter(date__range=[startdate, enddate])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))#(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)

def filter(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('filter_name').annotate(Count('filter_name')).filter(date__range=[startdate, enddate])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))#(json.dumps(content), content_type='application/json')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)


def weburl(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        queryset = logdata.objects.values('referrer_url').annotate(Count('referrer_url')).filter(date__range=[startdate, enddate])

        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(content)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)

def username(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        user_name = "pb114uvgjc1-16"
        queryset = logdata.objects.values('username', 'referrer_url').annotate(Count('referrer_url')).filter(date__range=[startdate, enddate]).filter(username = user_name)

        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)

def website(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        website_name = "http://192.168.50.252/schoolquizplus/teachers/lectures/mylectures.jsp?Action=New&TeacherID=32"
        queryset = logdata.objects.values('referrer_url', 'http_status', 'username').annotate(Count('referrer_url')).filter(date__range=[startdate, enddate]).filter(referrer_url = website_name)

        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)

def data(request):
    if request.method == 'GET':
        startdate = datetime.strptime("03/Feb/2014", "%d/%b/%Y")
        enddate = datetime.strptime("05/Feb/2014", "%d/%b/%Y")
        FromMB = 10 * 2048
        ToMB = 50 * 2048
        queryset = logdata.objects.values('username').annotate(Sum('byte_transferred')).filter(date__range=[startdate, enddate]).filter(byte_transferred__range=[FromMB, ToMB])
        serializer = logdataSerializer(queryset, many=True)
        #return HttpResponse(JSONRenderer().render(serializer.data))#queryset#serializer.data
        content = JSONRenderer().render(queryset)
        return HttpResponse(JSONRenderer().render(queryset))
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = logdataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render(serializer.data), status=201)
        return HttpResponse(serializer.errors, status=400)