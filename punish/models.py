from django.db import models

# Create your models here.
class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=50)
    password = models.CharField("password",max_length=25)
    role = models.CharField("role",max_length=25)

class district(models.Model):
    districtid = models.AutoField(primary_key=True)
    district = models.CharField("district",max_length=100)

class location(models.Model):
    locationid = models.AutoField(primary_key=True)
    location = models.CharField("location",max_length=100)
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True)

class user(models.Model):
    userid = models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name = models.CharField("name",max_length=25)
    phoneno = models.CharField("phoneno",max_length=10)
    address = models.CharField("address",max_length=100)
    aadharno = models.CharField("aadharno",max_length=20)
    email = models.CharField("email",max_length=30)
    gender = models.CharField("gender",max_length=20)
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True)
    photo = models.FileField("photo",max_length=100,upload_to="img/")
    status=models.CharField("status:",max_length=100)

class police(models.Model):
    policeid = models.AutoField(primary_key=True)
    login = models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name = models.CharField("name",max_length=50)
    mobileno = models.CharField("mobileno",max_length=20)
    aadharno = models.CharField("aadharno",max_length=20)
    address = models.CharField("address",max_length=50)
    qualification = models.CharField("qualification",max_length=30)
    rewards = models.CharField("rewards",max_length=50)
    dapartment = models.CharField("department", max_length=30)
    designation = models.CharField("designation",max_length=30)
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True)
    gender = models.CharField("gender",max_length=20)
    date = models.CharField("date",max_length=30)
    photo = models.FileField("photo",max_length=100,upload_to="img/")
    status=models.CharField("status:",max_length=100)

class category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    category = models.CharField("category",max_length=35)

class complaint(models.Model):
    complaintid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    name = models.CharField("name",max_length=20)
    phoneno = models.CharField("mobileno",max_length=20)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    complaint = models.CharField("complaint",max_length=300)
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE, null=True)
    time = models.CharField("time",max_length=50)
    spot = models.CharField("spot",max_length=50)
    evidence = models.FileField("evidence",max_length=100,upload_to="img/")
    date = models.DateField("date",max_length=30)
    status=models.CharField("status:",max_length=100)

class feedback(models.Model):
    feedbackid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=50)
    subject = models.CharField("subject",max_length=50)
    feedback = models.CharField("feedback",max_length=250)
    status=models.CharField("status:",max_length=100)

class reply(models.Model):
    repid = models.AutoField(primary_key=True)
    rep = models.CharField("reply",max_length=200)
    username = models.CharField("username",max_length=200)
    category = models.CharField("category",max_length=100)
    status = models.CharField("status",max_length=30)

class polcom(models.Model):
    polcomid = models.AutoField(primary_key=True)
    polcom = models.CharField("polcom",max_length=300)
    name = models.CharField("name",max_length=50)
    designation = models.CharField("designation",max_length=50)
    mobileno = models.CharField("mobileno",max_length=50)

