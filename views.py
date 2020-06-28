
from django.shortcuts import render, redirect, HttpResponse
import json
import time
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse
from django.urls import path
import request
from functools import wraps
from django.template import loader ,Context
import xlrd
from django.shortcuts import render, redirect
import importlib
import sys
import pymysql
conn = pymysql.connect(host='localhost',user='root',password='123',charset='utf8')
cursor = conn.cursor()
sql_one = 'use duhaiping_str;'
cursor.execute(sql_one)
conn.commit()
importlib.reload(sys)
@csrf_exempt
def login(request):
    if request.method=='GET':
        return render(request,'hello.html')
def hello(request):
    if request.method=='GET':
        return render(request,'login.html')
def dzx_ad(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_ad_position(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_admin(request):
    if request.method=='GET':
        sql_dzx_admin = 'select * from dzx_admin;'
        cursor.execute(sql_dzx_admin)
        conn.commit()

        return render(request,'hello.html')
def dzx_admin_log(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_article_classify(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_auth_group(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_auth_group_access(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_auth_rule(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_auth_rule111(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_content_article(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_guestbook(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_model(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_page(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_region(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_system(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_systerm(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_user(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_user_message(request):
    if request.method=='GET':
        return render(request,'hello.html')
def dzx_user_role(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_ad_classify(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_ad_info(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_admin(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_admin_log(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_article_classify(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_attr(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_attr_list(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_auth_group(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_auth_group_access(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_auth_rule(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_article(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_copy1(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_courseware(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_demeanour(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_education(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_education20181218(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_education20812181(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_expert(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_expert_copy(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_fkd_reserve_zone(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_hdjc(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_kfd_reserve(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_kfd_reserve_collect(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_kfd_reserve_route(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_kfdjs(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_knowledge(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_school(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_school20181218(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_senews(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_video(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_content_video_copy(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_guestbook(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_knowledge(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_knowledgezan(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_member(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_member_info(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_member_person(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_member_schedule(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_member_schedule_copy(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_model(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_page(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_parking(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_photo_album(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_region(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_school_score(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_systerm(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_tags(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_test_question(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_user(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_user_admin(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_user_message(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_user_reserve(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_user_role(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wp_validate_record(request):
    if request.method=='GET':
        return render(request,'hello.html')
def wx_user(request):
    if request.method=='GET':
        return render(request,'hello.html')




'''
个人中心
'''