import time
from datetime import datetime
from django.shortcuts import redirect
from  django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from tiaozaoapp.models import Tiaozao,Fenlei,AorB,Rootadmin
# Create your views here.de

def index(request):
    db=Tiaozao.objects.all()
    shopfl = Fenlei.objects.all()
    fllist=[]
    for i in shopfl:
        fllist.append(i.leibei)
    categorylist = dict()
    productlist = dict()
    request.session['shoplist'] = fllist
    # 遍历菜品类别信息
    for vo in shopfl:
        c = {"id": vo.id, "name": vo.leibei, "pids": []}
        plist = Tiaozao.objects.filter(category_id=vo.leibei)
        # 遍历当前类别下的所有菜品信息
        for p in plist:
            c['pids'].append(p.toDict())
        categorylist[vo.id] = c
        # 将上面的结果存入session中
        request.session['categorylist'] = categorylist
    context = {"shoplist": request.session.get("categorylist", {}).items(),"shopfl":shopfl}

    return render(request,'index.html',context)

def add(request):
    shopfl=Fenlei.objects.all()
    context={'shoplist':shopfl}

    return render(request,'add.html',context)


def insert(request):#执行添加
        try:
            ob=Tiaozao()
            ob.category_id=request.POST.get("fenlei")
            ob.name=request.POST.get('shopname')
            ob.price=request.POST.get('price')
            ob.photo=request.POST.get('photo')
            ob.weixin=request.POST.get('weixinnum')
            ob.user_name=request.POST.get('username')
            ob.shoptext = request.POST.get('shoptext')
            ob.booth_num = request.POST.get('booth_num')
            myfile = request.FILES.get("cover_pic", None)
            if not myfile:
                return HttpResponse("没有店铺封面上传文件信息")
            cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
            ob.cover_pic=cover_pic#存入数据库
            destination = open("./static/img/" + cover_pic, "wb+")
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            ob.status=1
            ob.create_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ob.update_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ob.save()
        except Exception as err:
            print(err)
        return redirect(reverse('indexshop'))

def addB(request):
    shopfl=Fenlei.objects.all()
    context={'shoplist':shopfl}

    return render(request,'addB.html',context)


def insertB(request):#执行添加
        try:
            ob=Tiaozao()
            ob.category_id=request.POST.get("fenlei")
            ob.name=request.POST.get('shopname')
            ob.price=request.POST.get('price')
            ob.photo=request.POST.get('photo')
            ob.weixin=request.POST.get('weixinnum')
            ob.user_name=request.POST.get('username')
            ob.shoptext = request.POST.get('shoptext')
            ob.booth_num = "义卖"
            myfile = request.FILES.get("cover_pic", None)
            if not myfile:
                return HttpResponse("没有店铺封面上传文件信息")
            cover_pic = str(time.time()) + "." + myfile.name.split('.').pop()
            ob.cover_pic=cover_pic#存入数据库
            destination = open("./static/img/" + cover_pic, "wb+")
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            ob.status=1
            ob.create_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ob.update_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ob.save()
        except Exception as err:
            print(err)
        return redirect(reverse('indexshop'))



def login(request):
    return render(request,'login.html')

def dologin(request):
    try:
        Rootadmin.objects.get(name=request.POST.get("username"))
        return render(request, 'aORb.html')
    except:
        return HttpResponse("没有这个成员！")
def aorb(request):
    if request.method=="GET":
        if request.GET['aob']=='1':
            return render(request,'addroot.html')
        else:
            return render(request,'addrootB.html')
def A(request):
    try:
        ob=AorB()
        ob.photo = request.POST.get('photo')
        ob.weixin = request.POST.get('weixinnum')
        ob.AorB=A
        ob.user_name = request.POST.get('username')
        if request.POST.get('status',0)==0:
            ob.status = "未交"
        elif request.POST.get('status')==1:
            ob.status='已交'
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.booth_num=request.POST.get('booth_num')
        ob.save()
        return HttpResponse('登记成功！')
    except Exception as e:
        print(e)
        return HttpResponse('登记失败！')

def B(request):
    try:
        ob=AorB()
        ob.photo = request.POST.get('photo')
        ob.weixin = request.POST.get('weixinnum')
        ob.AorB=B
        ob.user_name = request.POST.get('username')
        ob.B_leixin=request.POST.get('fenlei')
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        return HttpResponse('登记成功！')
    except Exception as e:
        print(e)
        return HttpResponse('登记失败！')

def v_login(request):
    return render(request, 'vlogin.html')

def dovlogin(request):
    try:
        AorB.objects.get(photo=request.POST['phone'])
        request.session['dolg']=1
        return redirect(reverse('indexshop'))
    except:
        return HttpResponse("没有登记！不能发布物品！")
