from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class log(models.Model):
    source_ip = models.CharField(max_length=100,default='127.0.0.1',verbose_name='源IP')
    log_type = models.CharField(max_length=10,default='error',verbose_name='日志类型')
    log_context = models.TextField(max_length=300,null=True,verbose_name='日志内容')
    log_date = models.DateTimeField(verbose_name='报告时间')
    post_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.source_ip + " " + self.log_type

class NodeInfo(models.Model):
    node_name = models.CharField(max_length=20,default='节点名称')
    node_ip = models.GenericIPAddressField(verbose_name='节点地址')
    node_active = models.CharField(max_length=10,verbose_name='开启')
    change_time = models.DateTimeField(null=True,verbose_name='更新时间')
    #node_guard = models.ForeignKey(Guard,on_delete=models.CASCADE)
    def __str__(self):
        return "Node " + self.node_name

class Guard(models.Model):
    node_guard = models.CharField(max_length=20,default='节点名称',primary_key=True)
    Guard_choices = (
        (u'N',u'NO'),
        (u'C',u'Close'),
    )
    waf_enable = models.CharField(max_length=10,choices=Guard_choices)
    white_ip_check = models.CharField(max_length=10,choices=Guard_choices)
    black_ip_check = models.CharField(max_length=10,choices=Guard_choices)
    url_check = models.CharField(max_length=10,choices=Guard_choices)
    user_agent_check = models.CharField(max_length=10,choices=Guard_choices)
    cookie_check = models.CharField(max_length=10,choices=Guard_choices)
    cc_check = models.CharField(max_length=10,choices=Guard_choices)
    waf_output = models.CharField(max_length=10,choices=Guard_choices)
    def __str__(self):
        return self.node_guard + '防护情况'

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user_role = models.CharField(max_length=40,default='admin',verbose_name='角色')
    def __str__(self):
        return self.username




