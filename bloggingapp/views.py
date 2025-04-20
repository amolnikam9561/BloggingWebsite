from django.shortcuts import render

from bloggingapp.models import UserData

# Create your views here.
def Home(request):
    return render(request,'bloggingapp/home.html')

def givemelogin(request):
    return render(request,'bloggingapp/login.html')

def givemeregister(request):
    return render(request,'bloggingapp/register.html')

def welcome(request):
    return render(request,'bloggingapp/welcomepage.html')

def errorpage(request):
    return render(request,'bloggingapp/errorpage.html')

def blogpage(request):
    return render(request,'bloggingapp/blog.html')

def register(request):

    usernamefrombrowser = request.GET["username"]
    emailid = request.GET["email"]
    mobilenumber = request.GET["mobile"]
    passfrombrowser = request.GET["password"]

    UserData.objects.create(username=usernamefrombrowser,password=passfrombrowser,email=emailid,mobile_number=mobilenumber)

    #create() will create new row in database table
    #print(connection.queries)
    return render(request,'bloggingapp/login.html',{'message':'Registration Successfull!! Please login now'})

def login(request):
    # Get username and password from the browser
    username_from_browser = request.GET.get("username", "").strip()
    password_from_browser = request.GET.get("password", "").strip()

    request.session['username']=username_from_browser
    
    try:
        # Try to fetch user details from the database
        user_from_db = UserData.objects.get(username=username_from_browser)

        # Validate the password
        if user_from_db.password == password_from_browser:
            return render(request, "bloggingapp/welcomepage.html")
        else:
            # Invalid password
            return render(request, "bloggingapp/errorpage.html", {"error": "password"})
    except UserData.DoesNotExist:
        # Invalid username
        return render(request, "bloggingapp/errorpage.html", {"error": "username"})

