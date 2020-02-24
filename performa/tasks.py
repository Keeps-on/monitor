from __future__ import absolute_import, unicode_literals
import time
import os
from django.conf import settings
from django.core.mail import send_mail


from celery.task.schedules import crontab
from celery.decorators import periodic_task

from worker import celery_app
from performa.models import Cpu


# @celery_app.task
# def consume_task(s):
#     print('this is a consume task'.center(30, '-'))
#     time.sleep(s)
#     print('this is a consume task'.center(30, '-'))
#     return "this is task result"
#
#
# @celery_app.task
# def check_email():
#     msg = '服务器运行良好ssssssssss'
#     send_mail(
#         subject='请注意这是Django邮件测试',
#         message=msg,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=["1299793997@qq.com"]  # 这里注意替换成自己的目的邮箱，不然就发到我的邮箱来了：）
#     )
#     # return HttpResponse('测试邮件已发出请注意查收')
#     return True


@periodic_task(run_every=crontab())
def read_cpu_data():
    """
    定时执行脚本获取CPU利用率IO磁盘响应等待
    :return:
    """
    # 执行脚本返回列表
    output = os.popen('bash /home/workspace/monitor/scripts/cpu.sh').readline()
    # 对执行结果进行处理,返回的是map可循环遍历的对象
    result = list(map(int, output.split(',')))
    # 执行时间
    execution = int(time.time())
    # util
    util = result[0]
    # iowait
    iowait = result[1]
    Cpu.objects.create(execution=execution, util=util, iowait=iowait)
    return True
