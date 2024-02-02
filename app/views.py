from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def equi_joins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    #EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    #EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    #EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    #EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)#It is showing None Not empty block
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equi_joins.html',d)

def self_joins(request):
    empmgrobjects=Emp.objects.select_related('empno').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='king')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=1000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__sal__gte=1000)
    #empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=5000)
    #empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2000,sal__lte=3000)
    empmgrobjects=Emp.objects.select_related('mgr').all().order_by(Length('ename'))
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname="Research")



    d={'empmgrobjects':empmgrobjects}
    return render(request,'self_joins.html',d)

def emp_mgr_dept(request):
    emdo=Emp.objects.select_related('deptno','mgr').all()
    emdo=Emp.objects.select_related('deptno','mgr').filter(mgr__ename="Blake")
    #emdo=Emp.objects.select_related('deptno','mgr').filter(ename="Martin")
    #emdo=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname="Research") | Q(mgr__ename="Johns"))
    emdo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname="Accounting")
    d={'emdo':emdo}
    return render(request,'emp_mgr_dept.html',d)

