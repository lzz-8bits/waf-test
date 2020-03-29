# Generated by Django 3.0.2 on 2020-03-23 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('node_guard', models.CharField(default='节点名称', max_length=20, primary_key=True, serialize=False)),
                ('waf_enable', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('white_ip_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('black_ip_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('url_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('user_agent_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('cookie_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('cc_check', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
                ('waf_output', models.CharField(choices=[('N', 'NO'), ('C', 'Close')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_ip', models.CharField(default='127.0.0.1', max_length=100, verbose_name='源IP')),
                ('log_type', models.CharField(default='error', max_length=10, verbose_name='日志类型')),
                ('log_context', models.TextField(max_length=300, null=True, verbose_name='日志内容')),
                ('log_date', models.DateTimeField(verbose_name='报告时间')),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='NodeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(default='节点名称', max_length=20)),
                ('node_ip', models.GenericIPAddressField(verbose_name='节点地址')),
                ('node_active', models.CharField(max_length=10, verbose_name='开启')),
                ('change_time', models.DateTimeField(null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('user_role', models.CharField(default='admin', max_length=40, verbose_name='角色')),
            ],
        ),
    ]
