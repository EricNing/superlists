# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from lists.models import Item, List
from django.db import connection
from django.core.exceptions import ValidationError
# Create your views here.


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
    return render(request, 'lists/home.html')

def new_list(request):
    list_ = List.objects.create()
    # Item.objects.create(text=request.POST['item_text'], list=list_)
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
        # url = '/lists/' + bytes(list_.id) + '/'
        # return redirect(url)
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'lists/home.html', {'error': error})
    # return redirect(f'/lists/{list_.id}/')
    # return redirect('view_list', list_.id)
    return redirect(list_)

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    # items = Item.objects.filter(list=list_)
    if request.method == 'POST':
        # Item.objects.create(text=request.POST['item_text'], list=list_)
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            # return redirect(f'/lists/{list_.id}/')
            # return redirect('view_list', list_.id)
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, "lists/list.html", {'list': list_, 'error': error})

# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     # url = '/lists/' + bytes(list_.id) + '/'
#     return redirect(f'/lists/{list_.id}/')
    # return redirect(url)