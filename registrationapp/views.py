import email
from email import message
from re import U
from unicodedata import name
from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import admin_users, issued_table
from .models import book_table
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def registeradmin(request):
    if request.method == 'POST':
        Uname = request.POST.get("urname")
        Uemail = request.POST.get("uremail")
        Upass = request.POST.get("urpassword")
        USuser = False 
        if admin_users.objects.filter(email=Uemail).exists():
            messages.info(request,'Email Exist')
            return redirect('register')

        else:
            user = admin_users.objects.create(name=Uname,email=Uemail,password=Upass,superuser=USuser)
            user.save()
            messages.info(request,'Registration Sucessfull Please Login!!')
            return redirect('register')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        Lemail = request.POST.get("ulemail")
        Lpass = request.POST.get("ulpassword")
        if admin_users.objects.filter(email=Lemail).exists() and admin_users.objects.filter(password=Lpass).exists():
            adetails = admin_users.objects.get(email = Lemail)
            return render(request,'adminpannel.html', {'adetails':adetails})
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect('login')


    else:
        return render(request,'login.html')

def logout(request):
    return redirect('login')

@csrf_exempt
def addbook(request):
    if request.method == 'POST':
        return render(request,'addbook.html')

    else:
        return redirect('login')

@csrf_exempt
def addbookval(request):
    if request.method == 'POST':
        bookid = request.POST.get("bookid")
        bookname = request.POST.get("bookname")
        bookimg = request.FILES["upimg"]
        bookTotal = request.POST.get("Tbooks")
        bookAvail = bookTotal
        bookissue = 0
        
        
        print("addvalue",bookimg)
        if book_table.objects.filter(bookid=bookid).exists():
            messages.info(request,"Bookid Exist")
            return render(request,'addbook.html')
        elif book_table.objects.filter(bookname=bookname).exists():
            messages.info(request,"Bookname Exist")
            return render(request,'addbook.html')
        else:
            
            Badd = book_table.objects.create(bookid=bookid,bookname=bookname,bookimg=bookimg,totalbooks=bookTotal,
            Available=bookAvail,issued = bookissue)
            Badd.save()  
            messages.info(request,'Book Added Sucessfully!!')
            return render(request,'addbook.html')

    else:
        return redirect('addbook')


Bid = ""

def update_val(request):
    if request.method == 'POST':
        updBname = request.POST.get("Ubookname")
        if book_table.objects.filter(bookname=updBname).exists():
            updvalues = book_table.objects.get(bookname=updBname)
            global Bid 
            Bid = updvalues.bookid
            print(Bid)
            return render(request,"updatebook.html",{'updvalues': updvalues})
        else:
            messages.info(request,"Book doesn't Exist")
            return render(request,'updsearch.html')


    else:
        return redirect('login')



@csrf_exempt
def updatesearch(request):
    if request.method == "POST":
        return render(request,'updsearch.html')
    else:
        return redirect('login')

@csrf_exempt
def update_submit(request):
    from .models import book_table
    if request.method == "POST":
        #Udbookid = request.POST.get("utbookid")
        Udbookname = request.POST.get("utbookname")
        Udbookimg = str("img/")+str(request.FILES["utupimg"])
        UdbookT = request.POST.get("utTbooks")
        UdbookA = request.POST.get("utAvailable")
        UdbookI = request.POST.get("utissued")
        
        
        #,bookimg=Udbookimg
        if book_table.objects.filter(bookid=Bid).exists():
            if len(Udbookimg) > 0 or Udbookimg == "":
                b_up = book_table.objects.filter(bookid=Bid).update(bookname=Udbookname,bookimg=Udbookimg,totalbooks=UdbookT,
                Available=UdbookA,issued=UdbookI)
                
                 
                messages.info(request,"Book Updated Sucessfully!!")
                return render(request,"updatebook.html")
            else:
                b_up = book_table.objects.filter(bookid=Bid).update(bookname=Udbookname,totalbooks=UdbookT,
                Available=UdbookA,issued=UdbookI)
            
                messages.info(request,"Book Updated Sucessfully!!")
                return render(request,"updatebook.html")

        
    else:
        return redirect('login')


            


def studview(request):  
    bookDetails = book_table.objects.all()
    return render(request,"studentview.html",{"bkds":bookDetails})


@csrf_exempt
def bookview(request,bkid):
    print(bkid)
    bkviews = book_table.objects.get(bookid=bkid)
    return render(request,"bookview.html",{"bkviews":bkviews})

@csrf_exempt
def delsrch(request):
    if request.method == "POST":
        return render(request,"delsrch.html")

    else:
        return redirect('login')

def delval(request):
    if request.method == "POST":
        delbkid = request.POST.get("Dbookid")
        print(delbkid)
        if len(book_table.objects.filter(bookid=delbkid)) > 0:
            book_table.objects.filter(bookid=delbkid).delete()
            messages.info(request,"Book Deleted Sucessfully!!")
            return render(request,"delsrch.html")
        else:
            messages.info(request,"Book doesn't Exist")
            return render(request,"delsrch.html")

    else:
        return redirect('login')

    



@csrf_exempt
def issuebook(request):
    if request.method == 'POST':
        return render(request,'issuebook.html')

    else:
        return redirect('login')

@csrf_exempt
def issueval(request):
    if request.method == "POST":
        Ibkname = request.POST.get("Ibookname")
        Isrno = request.POST.get("Srno")
        Isname = request.POST.get("Stname")
        Idate = request.POST.get("Idate")
        Rdate = request.POST.get("Rdate")
        print(Idate)
        if book_table.objects.filter(bookname = Ibkname).exists():
            Issvalues = book_table.objects.get(bookname=Ibkname)
            tempbknm = Issvalues.bookname
            valtotal = Issvalues.totalbooks
            valissued = Issvalues.issued
            if tempbknm == Ibkname:
                if  valissued < valtotal:
                    onebkval = issued_table.objects.filter(book_name=Ibkname)
                    if onebkval.count() < 1:
                        ireg = issued_table.objects.create(stud_rollno=Isrno,stud_name=Isname,issue_date=Idate,return_date=Rdate,
                        book_name=Ibkname)
                        ireg.save()

                        updI = issued_table.objects.filter(book_name=Ibkname)
                        updICount = updI.count()
                        temptotal = Issvalues.totalbooks
                        tempissued = updICount
                        tempavail = int(temptotal) - int(tempissued)
                        book_table.objects.filter(bookname=Ibkname).update(Available=tempavail,issued=tempissued)

                        messages.info(request,'Issue Registered Sucessfully!!')
                        return render(request,'issuebook.html')
                    else:
                        messages.info(request,'Book is been Already issued!!')
                        return render(request,'issuebook.html')


                else:
                    messages.info(request,'Book Not Available!!')
                    return render(request,'issuebook.html')

                
            else:
                messages.info(request,"Invalid bookname")
                return render(request,'issuebook.html')

        else:
            messages.info(request,"Invalid bookName")
            return render(request,'issuebook.html')

    else:
        return redirect('login')



@csrf_exempt
def returnsrch(request):
    if request.method == "POST":
        return render(request,"returnsearch.html")

    else:
        return redirect('login')

@csrf_exempt
def returnview(request):
    if request.method=="POST":
        Rsrno = request.POST.get("Strno")
        Robjs = issued_table.objects.filter(stud_rollno=Rsrno)
        for Robj in Robjs:
            tempN = Robj.stud_name
        
        if Robjs.count() > 0:
            return render(request,"returnbook.html",{"Robjs":Robjs,"tempN":tempN})

        else:
            messages.info(request,"No Data Available!")
            return render(request,"returnsearch.html")

    else:
        return redirect('login')

@csrf_exempt
def returnval(request):
    if request.method == "POST":
        Rdel = request.POST.get("tableF")
        
        issued_table.objects.filter(bookid_id=Rdel).delete()
        messages.info(request,"Book Returned!!")
        return render(request,"returnbook.html")
    else:
        return redirect('login')


        