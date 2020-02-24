from django.db import models


# Create your models here.


class Cpu(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    execution = models.IntegerField(verbose_name="执行时间")
    util = models.IntegerField(verbose_name="磁盘使用率")  # 创建一个varchar(20)类型的不能为空的字段
    iowait = models.IntegerField(verbose_name="等待磁盘IO响应使用率")

    def __str__(self):
        return "<{}-{}>".format(self.id, self.execution, self.util, self.iowait)

    class Meta:
        db_table = "cpu"
