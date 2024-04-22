from django.db import models

# Create your models here.
class DEPT(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField( max_length=50,unique=True)
    loc=models.CharField(max_length=50)
    def __str__(self):
        return self.deptname
    
class EMP(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(DEPT, on_delete=models.CASCADE)
    def  __str__(self):
        return self.ename
    
class SALGRADE(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.grade)
