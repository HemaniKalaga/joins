from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)#on_delete=False,why we given as "self"
    hiredate=models.DateField()#auto_now=False,auto_now_add=False
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(max_digits=10,decimal_places=2)
    highsal=models.DecimalField(max_digits=10,decimal_places=2)
