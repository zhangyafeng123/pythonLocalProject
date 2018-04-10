from django.db import models

# Create your models here.
#每一个用户可能拥有多个角色，那么就可能会有相同的权限，
#在最后查询处理的时候要进行去重。
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '用户表'
    def __str__(self):
        return self.username
class Role(models.Model):
    caption = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = '角色表'
    def __str__(self):
        return self.caption
class User2Role(models.Model):
    u = models.ForeignKey(User,on_delete=models.CASCADE,)
    r = models.ForeignKey(Role,on_delete=models.CASCADE,)
    class Meta:
        verbose_name_plural = '用户分配角色'
    def __str__(self):
        return "%s-%s" %(self.u.username,self.r.caption)
class Action(models.Model):
    # get 获取用户信息 1
    # post 创建用户 2
    # delete 删除用户 3
    # put 修改用户 4
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '操作表'

    def __str__(self):
        return self.caption
class Menu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self',related_name='p',null=True,blank=True,on_delete=models.CASCADE,)
    def __str__(self):
        return "%s" %(self.caption,)
class Permission(models.Model):
    # http://127.0.0.1:8000/user.html 用户管理 1
    # http://127.0.0.1:8000/order.html 订单管理 1
    caption = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    menu = models.ForeignKey(Menu,null=True,blank=True,on_delete=models.CASCADE,)
    class Meta:
        verbose_name_plural = 'URL表'
    def __str__(self):
        return "%s-%s" %(self.caption,self.url,)

class Permission2Action(models.Model):

    p = models.ForeignKey(Permission,on_delete=models.CASCADE,)
    a = models.ForeignKey(Action,on_delete=models.CASCADE,)
    class Meta:
        verbose_name_plural = '权限表'
    def __str__(self):
        return "%s-%s:-%s?t=%s" %(self.p.caption,self.a.caption,self.p.url,self.a.code)
class Permission2Action2Role(models.Model):
    p2a = models.ForeignKey(Permission2Action,on_delete=models.CASCADE,)
    r = models.ForeignKey(Role,on_delete=models.CASCADE,)
    class Meta:
        verbose_name_plural = '角色分配权限'
    def __str__(self):
        return "%s==>%s" %(self.r.caption,self.p2a)
