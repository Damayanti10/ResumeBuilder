from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        address=request.POST.get("address","")
        dob=request.POST.get("dob","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        college=request.POST.get("college","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        experience=request.POST.get("experience","")
        skill=request.POST.get("skill","")
        about_youself=request.POST.get("about_youself","")

        profile=Profile(name=name,address=address,dob=dob,phone=phone,email=email,college=college,degree=degree,university=university,experience=experience,skill=skill,about_youself=about_youself)
        profile.save()

    return render(request,"accept.html")



def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({'user_profile': user_profile})
    option ={
        'page-size' : 'Letter',
        'encoding' : "UTF-8"
    }
    pdf = pdfkit.from_string(html,False,option)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,'list.html',{'profile': profile})


