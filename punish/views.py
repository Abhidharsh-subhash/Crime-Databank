from dataclasses import dataclass
from datetime import date
from time import time
from unicodedata import category, name
from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import login as log,user as usr,district as dist,location as loca,police as pol,complaint as com,feedback as fb,category as cat,reply as repl,polcom as poco

# Create your views here.
def index(request):
    return render(request,"index.html")

def admin(request):
    if request.POST:
        username=request.POST["username"]
        password=request.POST["password"]
        datac=log.objects.filter(username=username,password=password,role="admin").count()
        if datac==1:
            data=log.objects.get(username=username,password=password,role="admin")
            request.session['username']=data.username
            request.session['role']=data.role
            request.session['id']=data.logid
            response=redirect("/adhome")
            return response
        else:
            return render (request,"adlogin.html")
    else:
        return render(request,"adlogin.html")

def logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

def userhome(request):
    return render(request,"userhome.html")

def userreg(request):
    if request.POST:
        name=request.POST["a1"]
        phoneno=request.POST["a2"]
        address=request.POST["a3"]
        password=request.POST["a4"]
        aadharno=request.POST["a6"]
        email=request.POST["a7"]
        gender=request.POST["a8"]
        district=request.POST["a9"]
        location=request.POST["a10"]
        a11=request.FILES["a11"]
        datadist=dist.objects.get(districtid=district)
        dataloca=loca.objects.get(locationid=location)
        log.objects.create(username=name,password=password,role="user")
        datal=log.objects.last()
        usr.objects.create(login=datal,name=name,phoneno=phoneno,address=address,aadharno=aadharno,email=email,gender=gender,district=datadist,location=dataloca,photo=a11,status="approved")
        
        response = redirect("/userlogin",{"msg":"registration succesfull"})
        return response
    else :
        datadist=dist.objects.all()
        return render(request,"userreg.html",{"datadist":datadist})

def user(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        datac=log.objects.filter(username=username,password=password,role="user").count()
        if datac==1:
            data=log.objects.get(username=username,password=password,role="user")
            request.session['username']=data.username
            request.session['role']=data.role
            request.session['id']=data.logid
            response=redirect("/userhome")
            return response
        else:
            return render(request,"userlogin.html")
    else:
        return render(request,"userlogin.html")

def police(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        datac=log.objects.filter(username=username,password=password,role="policehead").count()
        if datac==1:
            data=log.objects.get(username=username,password=password,role="policehead")
            datas=pol.objects.get(login=data)
            request.session['username']=data.username
            request.session['district']=datas.district.districtid
            request.session['role']=data.role
            request.session['id']=data.logid
            response=redirect("/polhome")
            return response
        else:
            response=redirect("pollogin")
            return response
    else:
        response=redirect("pollogin")
        return response

def userlogin(request):
    return render(request,"userlogin.html")

def pollogin(request):
    datadist=dist.objects.all()
    return render(request,"pollogin.html",{"datadist":datadist})

def adhome(request):
    return render(request,"adhome.html")

def adlogin(request):
    return render(request,"adlogin.html")

def dislist(request):
    datadist = dist.objects.all()
    return render(request,"dislist.html",{"datadist":datadist})

def complaints(request):
    dataco = com.objects.all()
    return render(request,"complaints.html",{"dataco":dataco})

def complaintlist(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    dataus=usr.objects.get(login=datal)
    data=com.objects.filter(userid=dataus).all()
    return render(request,"complaintlist.html",{"data":data})

def loclist(request):
    dataloca = loca.objects.all()
    return render(request,"loclist.html",{"dataloca":dataloca})

def usrfeedback(request):
    if request.POST:
        username=request.POST["username"]
        subject=request.POST["subject"]
        feedback=request.POST["feedback"]
        fb.objects.create(username=username,subject=subject,feedback=feedback,status="waiting")
        response = redirect("userhome")
        return response
    else:
        return render(request,"usrfeedback.html")

def adm(request):
    return render(request,"adm.html")

def repcomp(request):
    if request.POST:
        name=request.POST["name"]
        phone=request.POST["phone"]
        category=request.POST["category"]
        complaint=request.POST["complaint"]
        district=request.POST["district"]
        location=request.POST["location"]
        time=request.POST["time"]
        spot=request.POST["spot"]
        evidence=request.FILES["evidence"]
        date=request.POST["date"]
        datacat=cat.objects.get(categoryid=category)
        datadt=dist.objects.get(districtid=district)
        datalt=loca.objects.get(locationid=location)
        id=request.session['id']
        datal=log.objects.get(logid=id)
        datau=usr.objects.get(login=datal)
        com.objects.create(userid=datau,name=name,phoneno=phone,category=datacat,complaint=complaint,time=time,spot=spot,district=datadt,location=datalt,
        evidence=evidence,date=date,status="waiting")
        
        response = redirect("/userhome")
        return response
    else :
        datacat=cat.objects.all()
        datadist=dist.objects.all()
        return render(request,"repcomp.html",{"datadist":datadist,"datacat":datacat})

def feedback(request):
    datafd = fb.objects.all()
    return render(request,"feedback.html",{"datafd":datafd})

def userlist(request):
    datausr = usr.objects.all()
    return render(request,"userlist.html",{"datausr":datausr})

def userchange(request):
    if request.POST:
        old=request.POST["old"]
        password=request.POST["password"]
        id=request.session['id']
        role=request.session['role']

        datac=log.objects.filter(password=old).count()
        if datac==1:
            log.objects.filter(logid=id,role=role).update(password=password)
            response=redirect("userlogin")
            return response
        else:
            return render(request,"userchange.html",{"msg":"failed to change password"})
    else:
        return render(request,"userchange.html",{"msg":"password change failed"})

def pollist(request):
    datapol=pol.objects.all()
    return render(request,"pollist.html",{"datapol":datapol})

def polreg(request):
    if request.POST:
        name=request.POST["name"]
        mobileno=request.POST["mobileno"]
        aadharno=request.POST["aadharno"]
        address=request.POST["address"]
        qualification=request.POST["qualification"]
        rewards=request.POST["rewards"]
        designation=request.POST["designation"]
        dep=request.POST["dep"]
        district=request.POST["district"]
        location=request.POST["location"]
        password=request.POST["password"]
        date=request.POST["date"]
        gender=request.POST["gender"]
        photo=request.FILES["photo"]
        datadt=dist.objects.get(districtid=district)
        datalt=loca.objects.get(locationid=location)
        log.objects.create(username=name,password=password,role="policehead")
        datal=log.objects.last()
        pol.objects.create(login=datal,name=name,mobileno=mobileno,aadharno=aadharno,address=address,qualification=qualification,
        rewards=rewards,designation=designation,dapartment=dep,date=date,gender=gender,photo=photo,district=datadt,location=datalt,status="approved")

        response = redirect("/pollogin?msg=registration successfull",{"datadt":datadt})
        return response

    else:
        datadist=dist.objects.all()
        return render(request,"polreg.html",{"datadist":datadist})

def polrep(request):
    return render(request,"polrep.html")

def polhome(request):
    return render(request,"polhome.html")

def dis(request):
    if request.POST:
        district=request.POST["district"]
        dist.objects.create(district=district)
    return render(request,"dis.html",{"msg":"inserted successfully"})

def loc(request):
    data=dist.objects.all()
    if request.POST:
        district=request.POST["district"]
        location=request.POST["location"]
        datadt=dist.objects.get(districtid=district)
        loca.objects.create(district=datadt,location=location)
    return render(request,"loc.html",{"msg":"inserted successfully","data":data})

def adchange(request):
    if request.POST:
        old=request.POST["old"]
        password=request.POST["password"]
        id=request.session['id']
        role=request.session['admin']

        datac=log.objects.filter(password=old,role=role).count()
        if datac==1:
            log.objects.filter(logid=id).update(password=password)
            response=redirect("adlogin")
            return response
        else:
            return render(request,"adchange.html",{"msg":"failed to change password"})
    else:
        return render(request,"adchange.html",{"msg":"password change failed"})

def polchange(request):
   if request.POST:
        old=request.POST["old"]
        password=request.POST["password"]
        id=request.session['id']
        role=request.session['role']

        datac=log.objects.filter(password=old).count()
        if datac==1:
            log.objects.filter(logid=id,role=role).update(password=password)
            response=redirect("pollogin")
            return response
        else:
            return render(request,"adchange.html",{"msg":"failed to change password"})
   else:
        return render(request,"adchange.html",{"msg":"password change failed"})
def getloca(request):
    a10=request.GET["a10"]
    dtdata=dist.objects.get(districtid=a10)

    data=loca.objects.filter(district=dtdata).all()
    ret="<option value=''>--Location--</option>"
    for d in data:
        ret+="<option value='"+str(d.locationid)+"'>"+d.location+"</option>"
    return HttpResponse(ret)

def getloc(request):
    location=request.GET["location"]
    dtdata=dist.objects.get(districtid=location)

    data=loca.objects.filter(district=dtdata).all()
    ret="<option value=''>--Location--</option>"
    for d in data:
        ret+="<option value='"+str(d.locationid)+"'>"+d.location+"</option>"
    return HttpResponse(ret)

def crimecat(request):
    if request.POST:
        category=request.POST["category"]
        cat.objects.create(category=category)
    return render(request,"crimecat.html",{"msg":"inserted successfully"})

def catlist(request):
    datacat=cat.objects.all()
    return render(request,"catlist.html",{"datacat":datacat})

def usrprofile(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datapf=usr.objects.filter(login=datal).all()
    return render(request,"usrprofile.html",{"datapf":datapf})

def adreply(request):
    if request.POST:
        rep = request.POST["rep"]
        username = request.POST["username"]
        category = request.POST["category"]
        status = request.POST["status"]
        datacat=cat.objects.get(categoryid=category)
        repl.objects.create(rep=rep,username=username,category=datacat,status=status)
        return render(request,"adhome.html")
    else:
        datacat=cat.objects.all()
        return render(request,"adreply.html",{"datacat":datacat})

def deletepol(request):
    id=request.POST['id']
    log.objects.filter(logid=id).delete()
    response=redirect("/pollist")
    return response

def editpol(request):
    b1=request.GET["c"]
    data=pol.objects.get(policeid=b1)
    return render(request,"editspol.html",{"d":data})

def editspol(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    pol.objects.filter(policeid=c).update(name=t1,qualification=t2,mobileno=t3,address=t4,rewards=t5)
    response = redirect("pollist")
    return response

def deluser(request):
    id=request.POST['id']
    usr.objects.filter(userid=id).delete()
    response=redirect("/userlist")
    return response

def polucomp(request):
    district=request.session['district']
    data=com.objects.filter(district=district,status="viewed").all()
    return render(request,"polucomp.html",{"data":data})

def forward(request):
    f=request.GET["c"]
    data=com.objects.filter(complaintid=f).update(status="viewed")
    return redirect("/complaints",{"data":data})

def polreport(request):
    return render(request,"polreport.html")

def polcom(request):
    return render(request,"polcom.html")

def poc(request):
    if request.POST:
        name=request.POST['name']
        designation=request.POST['designation']
        mobileno=request.POST['mobileno']
        comp=request.POST['comp']
        poco.objects.create(name=name,designation=designation,mobileno=mobileno,polcom=comp)
    return render(request,"polcom.html")

def pcomlist(request):
    datal=poco.objects.all()
    return render(request,"pcomlist.html",{"datal":datal})

def editusr(request):
    b1=request.GET["u"]
    data=usr.objects.get(userid=b1)
    return render(request,"editsusr.html",{"d":data})

def editsusr(request):
    u=request.GET["u"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    pol.objects.filter(userid=u).update(name=t1,address=t2,phoneno=t3,email=t4)
    response = redirect("usrprofile")
    return response

def editscom(request):
    c=request.GET["c"]
    name=request.POST["name"]
    phone=request.POST["phone"]
    complaint=request.POST["complaint"]
    com.objects.filter(complaintid=c).update(name=name,phoneno=phone,complaint=complaint)
    return redirect("complaintlist")

def editcom(request):
    c1=request.GET["c"]
    data=com.objects.get(complaintid=c1)
    return render(request,"editscom.html",{"d":data})

def deletedis(request):
    id=request.POST['id']
    dist.objects.filter(districtid=id).delete()
    response=redirect("/dislist")
    return response

def editdis(request):
    b1=request.GET['i']
    data=dist.objects.get(districtid=b1)
    return render(request,"editsdis.html",{"d":data})

def editsdis(request):
    i=request.GET['i']
    t1=request.POST["t1"]
    dist.objects.filter(districtid=i).update(district=t1)
    response = redirect("dislist")
    return response

def deletelo(request):
    id=request.POST['id']
    loca.objects.filter(locationid=id).delete()
    response=redirect("/loclist")
    return response

def editlo(request):
    b1=request.GET['i']
    data=loca.objects.get(locationid=b1)
    return render(request,"editslo.html",{"d":data})

def editslo(request):
    i=request.GET['i']
    t1=request.POST["t1"]
    loca.objects.filter(locationid=i).update(location=t1)
    response = redirect("loclist")
    return response

def deletect(request):
    id=request.POST['id']
    cat.objects.filter(categoryid=id).delete()
    response=redirect("/catlist")
    return response

def editct(request):
    b1=request.GET['i']
    data=cat.objects.get(categoryid=b1)
    return render(request,"editsct.html",{"d":data})

def editsct(request):
    i=request.GET['i']
    t1=request.POST["t1"]
    cat.objects.filter(categoryid=i).update(category=t1)
    response = redirect("catlist")
    return response

    


