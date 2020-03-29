from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import FileResponse
from elasticsearch import Elasticsearch
from waflog.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import connection
import time,re,os
from . import dircopy

# Create your views here.
def index(request):
    return render(request,'index.html')
    #user = models.log.objects.get(pk=1)
    #return render(request,'index.html',{'user':user})

def page_not_found(request,exception,template_name='404.html'):
    return render(request,template_name)

def show_log(request):
    es = Elasticsearch({"101.132.128.97:9200"})
    ret = es.search(index="logstash-nginxaccesslog-2020.03.17",
                    body={
                        "query":{
                            "term":{"message":"cluster"}
                        }
                    })
    resultback = ret["hits"]["hits"]
    log_rs = {"results":resultback}
    return render(request, 'nodelist.html', log_rs)

def nodelist(request):
    node_list = models.NodeInfo.objects.all()
    return render(request,'nodelist.html',{'nodelist':node_list})

def nodeinfo(request,node_id):
    return HttpResponse("You are looking at node%s" % node_id)

def node_add(request):
    file_path = os.path.dirname(__file__)
    node_name = request.POST.get('node_name','node_name')
    node_ip = request.POST.get('node_ip','node_ip')
    file_dir = os.path.join(file_path,'static','file',node_name)
    init_dir = os.path.join(file_path,'static','file','default')
    if os.path.exists(file_dir):
        print("节点名称 %s 已存在" %(node_name))
        return render(request,'nodeadd.html',{'result':'当前节点已存在'})
    else:
        #os.makedirs(file_path)   #创建文件夹
        dircopy.copy_file(file_dir,init_dir)  #初始化配置
        print('节点文件 %s 已创建' %(node_name))
    models.NodeInfo.objects.create(node_name=node_name,node_ip=node_ip,node_active='on')
    node_list = models.NodeInfo.objects.all()
    return render(request,'nodelist.html',{'nodelist':node_list})

def login(request):
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method== 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username,password = password)
        try:
            users = models.User.objects.get(username=username)
            if users.password == password:
                return render(request,'index.html', {'user': user,'nowtime': nowtime })
            else:
                err_msg = "密码输入错误"
        except:
            err_msg = "用户名不存在"
        return render(request,'login.html',{'err_msg':err_msg,'nowtime': nowtime})
    else:
        return render(request,'login.html', {'nowtime': nowtime})

'''if user:
            #response = HttpResponseRedirect('/index/')              #重定向到index
            #response.set_cookie('cookie_username',username,36)      #设置cookie
            #return response
            return render(request,'index.html', {'user': user,'nowtime': nowtime })
        else:
            err_msg = "用户名或者密码输入错误"
            return render(request,'login.html',{'err_msg':err_msg})
    else:
        return render(request, 'login.html', {'nowtime': nowtime})'''


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')
    #return render(request,'login.html')
    #response.delete_cookie('cookie_username')                            #删除cookie_username对应的用户的cookie
    #return  response

def conf_download(request):
    conf = open('static/file/default/config.lua', 'rb')
    response = FileResponse(conf)
    response['Content-Type'] = 'application/octer-stream'
    response['Content-Disposition'] = 'attachment;filename = "conf.lua"'
    return response

def conf_display(request):
    guard_list = models.Guard.objects.all()
    return render(request,'confdispaly.html',{'guradlist':guard_list})


def conf_init(request):
    file_dir = os.path.dirname(__file__)
    print(file_dir)
    node = 'default'
    path = os.path.join(file_dir,'static','file',node,'config.lua')
    print(path)
    conf = open(path, 'rb')
    if os.path.exists(path):
        print("节点名称 %s 已存在" %(node))
    else:
        #os.makedirs(path)   #创建文件夹
        print('节点文件 %s 不存在' %(node))
    message =conf.read()

    txt = message.decode('UTF-8')
    guard1 = 'waf_enable'
    pattern1 = r'((%s+) = "(.*)")'%(guard1)
    matchObj1 = re.search(pattern1,txt,re.M|re.I)
    value1 = matchObj1.group(3)

    guard2 = 'white_ip_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard2)
    matchObj2 = re.search(pattern2,txt,re.M|re.I)
    value2 = matchObj2.group(3)

    guard3 = 'black_ip_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard3)
    matchObj3 = re.search(pattern2,txt,re.M|re.I)
    value3 = matchObj3.group(3)

    guard4 = 'url_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard4)
    matchObj4 = re.search(pattern2,txt,re.M|re.I)
    value4 = matchObj4.group(3)

    guard5 = 'user_agent_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard5)
    matchObj5 = re.search(pattern2,txt,re.M|re.I)
    value5 = matchObj5.group(3)

    guard6 = 'cookie_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard6)
    matchObj6 = re.search(pattern2,txt,re.M|re.I)
    value6 = matchObj6.group(3)

    guard7 = 'cc_check'
    pattern2 = r'((%s+) = "(.*)")'%(guard7)
    matchObj7 = re.search(pattern2,txt,re.M|re.I)
    value7 = matchObj7.group(3)

    guard8 = 'waf_output'
    pattern2 = r'((%s+) = "(.*)")'%(guard8)
    matchObj8 = re.search(pattern2,txt,re.M|re.I)
    value8 = matchObj8.group(3)

    list = models.Guard(node_guard=node,waf_enable=value1,white_ip_check=value2,black_ip_check=value3,url_check=value4,user_agent_check=value5,cookie_check=value6,cc_check=value7,waf_output=value8)
    list.save()
    guardlist = models.Guard.objects.all()
    conf.close()
    return render(request,'confdispaly.html',{'guradlist':guardlist})


