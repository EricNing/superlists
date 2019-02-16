# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from lists.models import Item, List
from django.db import connection
from django.core.exceptions import ValidationError
# Create your views here.
from lists.forms import ItemForm


def get_data_from_ora():
    import cx_Oracle
    conn = cx_Oracle.connect('zabbix', 'zabbix', "10.1.23.187:1521/orcl")
    cursor = conn.cursor()
    sql = "select clock*1000 clock, round(value*100,2) value from history where itemid=24496 order by clock fetch first 50 rows only"
    cursor.execute(sql)
    res = dictfetchall(cursor)
    cursor.close()
    conn.close()
    return res

# def get_data():
#     import pymysql
#     conn = pymysql.connect(host='10.1.23.167',
#                                  user='book',
#                                  passwd='book',
#                                  db='book', charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("select * from lists_list")
#     res = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return res

def get_lists():
    with connection.cursor() as cursor:
        cursor.execute("select * from lists_list")
        row = dictfetchall(cursor)
    return row

def dictfetchall(cursor):
    """
    :param cursor:
    :return: Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def echars(request):
    # rows = get_data_from_ora
    return render(request, 'lists/echarts.html')
                  # , {'row': rows})

def base(request):
    # 默认去所有APP下的templates目录下查找模板
    return render(request, 'lists/base.html')

def home_page(request):
    # 默认去所有APP下的templates目录下查找模板
    return render(request, 'lists/home.html', {'form': ItemForm()})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list = list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {"form": form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list = list_)
            return redirect(list_)
    return render(request, "lists/list.html", {'list': list_, 'form': form})