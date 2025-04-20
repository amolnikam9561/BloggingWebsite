from django.shortcuts import render
from onlinequiz.models import *
from django.utils import timezone


# Create your views here.
def question_management(request):
    return render(request,'secondapp/question_management.html')

def addQuestion(request):

    Questions.objects.create(qno=request.GET['qno'],qtext=request.GET['qtext'],answer=request.GET['answer'],op1=request.GET['op1'],op2=request.GET['op2'],op3=request.GET['op3'],op4=request.GET['op4'],subject=request.GET['subject'])
    
    return render(request,'secondapp/question_management.html',{'message':"Question Added successfully!!"})

def viewQuestion(request):
    question = Questions.objects.get(qno=request.GET['qno'],subject=request.GET['subject'])
    return render(request,'secondapp/question_management.html',{'question': question})

def deleteQuestion(request):
    question = Questions.objects.filter(qno=request.GET['qno'],subject=request.GET['subject']).delete()
    return render(request,'secondapp/question_management.html',{'question':question})

def updateQuestion(request):
    qnofrombrowser = request.GET['qno']
    subjectfrombrowser = request.GET['subject']

    try:
        # Fetch the question to be updated
        question = Questions.objects.get(qno=qnofrombrowser, subject=subjectfrombrowser)

        # Update the question fields with the values from the form
        question.qtext = request.GET.get('qtext', question.qtext)
        question.answer = request.GET.get('answer', question.answer)
        question.op1 = request.GET.get('op1', question.op1)
        question.op2 = request.GET.get('op2', question.op2)
        question.op3 = request.GET.get('op3', question.op3)
        question.op4 = request.GET.get('op4', question.op4)

        # Save the updated question
        question.save()

        message = "Question updated successfully!"
    except Questions.DoesNotExist:
        message = "Question not found for the given number and subject."

    return render(request, 'secondapp/question_management.html', {'message': message, 'question': question if 'question' in locals() else None})

def givemeuserregister(request):

    return render(request,'secondapp/user_register.html')

def userregister(request):

    usernamefrombrowser = request.GET['username']
    emailfrombrowser = request.GET['email']
    passwordfrombrowser = request.GET['password']

    UserDatabase.objects.create(username=usernamefrombrowser,email=emailfrombrowser,password=passwordfrombrowser)
    return render(request,'secondapp/user_login.html',{'message':'Registration successful!! Please login now !'})

def givemeuserlogin(request):

    return render(request,'secondapp/user_login.html')

def userlogin(request):
    # Get username and password from the browser
    username_from_browser = request.GET.get("username", "").strip()
    password_from_browser = request.GET.get("password", "").strip()

    request.session['username']=username_from_browser
    
    try:
        # Try to fetch user details from the database
        user_from_db = UserDatabase.objects.get(username=username_from_browser)

    except UserDatabase.DoesNotExist:
        # Invalid username
        return render(request, "secondapp/user_login.html", {"error": "username"})
    
    # Validate the password
    if user_from_db.password == password_from_browser:

        request.session['answers'] = {}
        request.session['score'] = 0
        request.session['qno'] = -1
    

        # queryset =Question.objects.filter(subject='python').values()
        # listofquestions=list(queryset)
        # request.session['listofquestions'] = listofquestions

        return render(request, "secondapp/subject.html")
    else:
        # Invalid password
        return render(request, "secondapp/user_login.html", {"error": "password"})
    
def givemeadminregister(request):

    return render(request,'secondapp/admin_register.html')

def adminregister(request):

    usernamefrombrowser = request.GET['username']
    emailfrombrowser = request.GET['email']
    passwordfrombrowser = request.GET['password']

    AdminDatabase.objects.create(username=usernamefrombrowser,email=emailfrombrowser,password=passwordfrombrowser)
    return render(request,'secondapp/admin_login.html',{'message':'New Admin Registration successful!! Please login now !'})

def givemeadminlogin(request):

    return render(request,'secondapp/admin_login.html')

def adminlogin(request):
    # Get username and password from the browser
    username_from_browser = request.GET.get("username", "").strip()
    password_from_browser = request.GET.get("password", "").strip()

    #request.session['username']=username_from_browser
    
    try:
        # Try to fetch user details from the database
        user_from_db = AdminDatabase.objects.get(username=username_from_browser)

        # Validate the password
        if user_from_db.password == password_from_browser:
            return render(request, "secondapp/admin_dashboard.html")
        else:
            # Invalid password
            return render(request, "secondapp/admin_login.html", {"error": "password"})
    except AdminDatabase.DoesNotExist:
        # Invalid username
        return render(request, "secondapp/admin_login.html", {"error": "username"})
    
def student_dashboard(request):
    return render(request,'secondapp/student_dashboard.html')


def question_navigation(request):
    return render(request,'secondapp/question_navigation.html')

def nextQuestion(request):

    if 'op' in request.GET:
        allanswers = request.session['answers']

        allanswers[request.GET['qno']] = [request.GET['qno'], request.GET['qtext'], request.GET['answer'],request.GET['op']]

        print(allanswers)
    
    allquestions=request.session["listofquestions"]

    questionindex=request.session['qno']
    
    if questionindex<len(allquestions) -1:

        request.session["qno"]=request.session["qno"] + 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'secondapp/question_navigation.html',{'message':"!!This is Last Question!!",'question':allquestions[len(allquestions)-1]})

    return render(request,'secondapp/question_navigation.html',{'question':question})

def previousQuestion(request):
    # Retrieve the list of all questions from the session

    if 'op' in request.GET:
        allanswers = request.session['answers']

        allanswers[request.GET['qno']]  = [request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        print(allanswers)
    allquestions = request.session["listofquestions"]

    # Get the current question index from the session
    questionindex = request.session['qno']

    # Check if there are previous questions available
    if questionindex > 0:
        # Decrement the question index to move to the previous question
        request.session["qno"] = request.session["qno"] - 1

        print(f"qno is {request.session['qno']}")

        # Get the previous question
        question = allquestions[request.session["qno"]]
    else:
        # If no previous question exists, show a message
        return render(request, 'secondapp/question_navigation.html', {
            'message': "You are already at the first question.",
            'question': allquestions[0]  # Display the first question
        })

    # Render the page with the previous question
    return render(request, 'secondapp/question_navigation.html', {'question': question})

def endexam(request):
    if 'op' in request.GET:

        #Retrieve all answers from the session
        allanswers = request.session['answers']
        allanswers[request.GET['qno']] = request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']

        print(allanswers)

    
    responses = request.session["answers"]
    allanswers2 = responses.values() 
        
    for ans in allanswers2:

        print(f"correct answer {ans[2]} and submitted answer {ans[3]}")

        if ans[2] == ans[3]:
            request.session['score'] = request.session['score'] + 1

    finalscore = request.session['score']
    print(f"Your score is {finalscore}")

    usernamefrombrowser = request.session['username']
    subjectfrombrowser = request.GET['subject']
    scorefrombrowser = finalscore
    datetimefrombrowser = timezone.now()

    Results.objects.create(username=usernamefrombrowser,subject=subjectfrombrowser,score=scorefrombrowser,date_time = datetimefrombrowser)



    return render(request,'secondapp/score.html',{'score':finalscore,'responses':allanswers2})

def startTest(request):

    subjectname = request.GET['subject']
    request.session['subject'] = subjectname

    queryset = Questions.objects.filter(subject=subjectname).values()
    listofquestions=list(queryset)
    request.session['listofquestions'] = listofquestions

    return render(request,'secondapp/question_navigation.html',{'question':listofquestions[0]})

def admin_dashboard(request):
    # Check if the admin username is stored in the session
    admin_from_browser = request.session.get('username', None)

    if admin_from_browser:
        # Fetch all records from the Results model
        data = Results.objects.all()
        
        # Render the data to the HTML page
        return render(request, 'secondapp/results_of_user.html', {'data': data})
    else:
        # If the admin is not logged in, redirect them to the login page or show an error
        return render(request, 'secondapp/givemeadminlogin.html')
    
def question_management(request):

    return render(request,'secondapp/question_management.html')

def student_results(request):

    data = Results.objects.all()

    return render(request,'secondapp/student_results.html', {'data': data})




