import time

from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse

from performa.models import Cpu

from utils.tools import time_to_string  # 时间转换函数


def get_cpu_data(request):
    """获取CPU利用率,IO磁盘等待响应"""
    result = {
        "code": 0,  # 0 表示成功 1 表示加载异常
        "msg": ""  # 异常提示信息
    }
    cpu_queryset = Cpu.objects.all().values('execution', 'util', 'iowait')[:20]
    # 将时间转换为时间戳
    string_time = [time_to_string(data['execution']) for data in cpu_queryset[:20]]
    # 获取cpu利用率
    util = [data['util'] for data in cpu_queryset]
    # 获取iowait
    iowait = [data['iowait'] for data in cpu_queryset]
    # 返回结果
    result['execution'] = string_time
    result['util'] = util
    result['iowait'] = iowait

    return JsonResponse(result)
