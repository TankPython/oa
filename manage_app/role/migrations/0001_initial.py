# Generated by Django 3.1.7 on 2021-02-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OAPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('method', models.CharField(max_length=20, verbose_name='请求方法')),
                ('pid', models.IntegerField(verbose_name='上级id')),
                ('level', models.IntegerField(verbose_name='等级')),
                ('path', models.CharField(max_length=200, verbose_name='请求路径')),
            ],
            options={
                'verbose_name': '权限表',
                'db_table': 'oa_permission',
            },
        ),
        migrations.CreateModel(
            name='OARole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='名字')),
                ('desc', models.CharField(blank=True, max_length=20, verbose_name='描述')),
                ('ps_ids', models.CharField(blank=True, max_length=300, verbose_name='拥有的权限id')),
            ],
            options={
                'verbose_name': '角色表',
                'db_table': 'oa_role',
            },
        ),
        migrations.CreateModel(
            name='OAUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.IntegerField(default=0)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='邮箱')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='电话')),
                ('role_id', models.IntegerField(blank=True, null=True, verbose_name='角色id')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'oa_user',
            },
        ),
    ]
