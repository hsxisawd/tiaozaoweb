from django.db import models
from datetime import datetime
# Create your models here.
class Tiaozao(models.Model):
    user_name=models.CharField(max_length=255) #联系人姓名
    booth_num=models.CharField(max_length=50)         #摊位号
    photo=models.IntegerField()             #联系人电话
    weixin=models.CharField(max_length=100) #联系人微信
    category_id = models.CharField(max_length=30)    #商品分类
    cover_pic = models.CharField(max_length=50,null=True)    #商品图片
    name = models.CharField(max_length=255)  #商品名称
    price = models.FloatField()             #商品单价
    status = models.IntegerField(default=1)        #状态:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间
    shoptext=models.TextField(default='')
    def toDict(self):
        return {'booth_num':self.booth_num,'id':self.id,"user_name":self.user_name,"photo":self.photo,'weixin':self.weixin,'shoptext':self.shoptext,'category_id':self.category_id,'cover_pic':self.cover_pic,'name':self.name,'price':self.price,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "tiaozao"  # 更改表名


class Fenlei(models.Model):
    leibei=models.CharField(max_length=50)

    class Meta:
        db_table = "fenlei"
class AorB(models.Model):
    AorB=models.CharField(max_length=50)#A区还是B区
    user_name=models.CharField(max_length=255) #联系人姓名
    photo=models.IntegerField()             #联系人电话
    weixin=models.CharField(max_length=100) #联系人微信
    status = models.CharField(max_length=50) #0代表已交 1代表未交
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间
    booth_num = models.IntegerField() #摊位号
    B_leixin=models.CharField(max_length=50)#B区类型
    class Meta:
        db_table = "tiaozaoAorB"

class Rootadmin(models.Model):
    name=models.CharField(max_length=50) #学生会管理人员