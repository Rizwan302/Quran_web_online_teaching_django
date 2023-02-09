from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import AdmissionFrom

# Create your views here.

def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        country = request.POST['country']
        city = request.POST['city']
        gender = request.POST['gender']
        if len(fname)<3 and len(lname)<3 and len(dob)<10 and len(country)<4 and len(city)<3 and len(gender)<4 and len(phone)<6 and len(email)<7:
            print('Form Fill Succesfully')
        
        # -------------Start It if statment admin ko email send ka code ha-------------
        if fname and lname and email:
            subject = 'QuranPak Website Send Mail'
            mg = (f"<p>New Student Name <h2>{fname} {lname}</h2> E-mail id for Student <h2>{email}</h2> Admission Form Fill</P>")
            from_email = 'yousafumair460@gmail.com'
            to = "yousafumair460@gmail.com"
            mg = EmailMultiAlternatives(subject,mg,from_email,[to])
            mg.content_subtype='html'
            mg.send()
        # -------------End It if statment admin ko email send ka code ha-------------

        
        funadd = AdmissionFrom(fname=fname, mname=mname, lname=lname, dob=dob, phone=phone, email=email, country=country, city=city, gender=gender)
        funadd.save()
    return render(request, 'home/admission.html')