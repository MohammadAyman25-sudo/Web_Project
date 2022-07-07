from .models import Employee, Student
from django.shortcuts import render,redirect

## the following functions are meant to load html pages only

nav_context = {
    'userName':'',
    'lname':'login'
    }

temp=dict()
ID = None
st = None

def login(request):
    context={
        'ok':True,
    }
    return render(request,'login_screen.html',context)

def who_pressed_login(request):
    global ID
    ID=request.POST['uname']
    return redirect('loginScreen')

def new_account(request):
    context={
        'ok':True
    }
    return render(request, 'CreateEmployeeAccount.html', context)

    
def homepage(request):
    global nav_context
    return render(request, 'Home.html', nav_context)

def active_inactive(request):
    st=Student.objects.all()
    global nav_context
    context={
        'ss':st,
        'lname':nav_context['lname'],
        'userName':nav_context['userName']
    }
    return render(request,'active-inactive.html',context)

def search(request):
    global nav_context
    return render(request, 'search.html', nav_context)

def addStudentPage(request):
    global nav_context
    return render(request, 'add_student.html', nav_context)

def log_out(request):
    alEmp = Employee.objects.get(Username=request.POST['uname'])
    alEmp.logedin = False
    alEmp.save()
    nav_context['lname'] = 'login'
    nav_context['userName'] = ''
    return render(request, 'Home.html', nav_context)

def editPage(request):
    global nav_context
    return render(request, 'edit.html', nav_context)

def department_assignment(request):
    context={
        'students': request.POST.get('students'),
        'lname':nav_context['lname'],
        'userName':nav_context['userName']
    }
    return render(request, 'department_assignment.html', context)

## end of "html loading" functions

def validate(request):
    if request.method == 'POST':
        context = {
            'ok': True,
            'lname':nav_context['lname'],
            'userName':nav_context['userName']
            }
        allStudents=Employee.objects.all()
        for a in allStudents:
            if a.mail==request.POST.get('email'):
                if a.password==request.POST.get('password'):
                    a.logedin = True
                    a.save()
                    if a.logedin:
                        context['lname'] = 'logout'
                        context['userName']=a.Username
                        context['ok'] = True
                        nav_context['lname'] = 'logout'
                        nav_context['userName'] = a.Username
                        
                    if ID == 'add':
                        return redirect('addStudentPage')
                    elif ID == 'search':
                        return redirect('search')
                    elif ID == 'active_inactive':
                        return redirect('active-inactive')                    
                    return render(request, 'Home.html', context)
        context['ok'] = False
        return render(request,'login_screen.html',context)

def check_new_Account(request):
    if request.method == 'POST':
        temp=dict(request.POST.dict())
        Accounts = Employee.objects.all()
        for acc in Accounts:
            if acc.mail == request.POST.get('email'):
                temp['exists']=True
                return render(request, 'CreateEmployeeAccount.html', temp)
            if acc.Username == request.POST.get('User_name'):
                temp['uniqueUser']=False
                return render(request, 'CreateEmployeeAccount.html', temp)

        if request.POST.get('password') != request.POST.get('Confirmpassword'):
            temp['correctPass']=False
            return render(request, 'CreateEmployeeAccount.html', temp)
        if request.POST.get('User_name')[0] in ['_', '-','.'] or ' ' in request.POST.get('User_name'):
            temp['correctUser'] = False
            return render(request, 'CreateEmployeeAccount.html', temp)
        x = []
        y = []
        z = []
        c = 'A'
        while c <= 'Z':
            x.append(c)
            c = chr(ord(c) + 1)
        c = '0'
        while c <= '9':
            y.append(c)
            c = chr(ord(c) + 1)
        c = 'a'
        while c <= 'z':
            z.append(c)
            c = chr(ord(c) + 1)
        char = False
        dig = False
        for i in x:
            if request.POST.get('User_name').find(i) != -1:
                char = True
                break;
        for i in y:
            if request.POST.get('User_name').find(i) != -1:
                dig = True
                break
        
        if char and dig:
            name = request.POST.get('User_name')
            mail = request.POST.get('email')
            password = request.POST.get('password')
            data = Employee(Username=name, mail=mail, password=password)
            data.save()
            return render(request, 'login_screen.html', {'account':True})
        else:
            temp['correctUser']=False
            return render(request, 'CreateEmployeeAccount.html', temp)
    
def addStudent(request):
    if request.method == 'POST':
        global nav_context
        temp = dict(request.POST.dict())
        x=Student.objects.filter(ID=request.POST['id'])
        if x:
            temp['lname'] = nav_context['lname']
            temp['ok'] = False
            temp['userName'] = nav_context['userName']
            return render(request,'add_student.html',temp)
        t = request.POST['gender']
        if t == 'male':
            t = True
        else:
            t = False
        a = request.POST['status']
        if a == 'active':
            a = True
        else:
            a = False
        member = Student(
        name=request.POST['name'],
        ID=request.POST['id'],
        birth=request.POST['date'],
        gpa=request.POST['gpa'],
        male=t,
        female=not t,
        level=request.POST['level'],
        active=a,
        inactive=not a,
        dep=request.POST.get('department', 'general'),
        mail=request.POST['email'],
        phone=request.POST['phone'],
        )
        member.save()
        context={'st':True,
                 'ss': Student.objects.all(),
                 'userName':nav_context['userName'],
                 'lname':nav_context['lname']
         }
        return render(request, 'active-inactive.html', context)

def updateStudents(request):
    if request.method == 'POST':
        global st
        x=Student.objects.get(ID=request.POST['id'])
        st=request.POST['id']
        context = {
            'lname':nav_context['lname'],
            'userName':nav_context['userName'],
            'student':x
            }
        return render(request,"edit.html",context)

def updateDone(request):
    if request.method == 'POST':
        if request.POST['id'] != st:
            temp = dict(request.POST.dict())
            temp["lname"] = nav_context['lname']
            temp['userName'] = nav_context['userName']
            temp['ok'] = False
            x=Student.objects.get(ID=st)
            temp['student'] = x
            return render(request, 'edit.html', temp)
        x=Student.objects.get(ID=request.POST['id'])
        x.name = request.POST['name']
        x.birth = request.POST['date']
        x.gpa = request.POST['gpa']
        if request.POST['gender'] == 'male':
            x.male = True
            x.female = False
        else:
            x.female = True
            x.male = False
        if request.POST['status'] == 'active':
            x.inactive = False
            x.active = True
        else:
            x.inactive = True
            x.active = False
        x.level = request.POST['level']
        x.dep = request.POST.get('department', x.dep)
        x.phone = request.POST['phone']
        x.mail = request.POST['email']
        x.save()
        return redirect('active-inactive')

def deleteStudent(request):
    if request.method == 'POST':
        x=Student.objects.get(ID=request.POST['id'])
        x.delete()
        return redirect("active-inactive")

def changeStatus(request):
    if request.method == 'POST':
        x=Student.objects.get(ID=request.POST['id'])
        x.active = not x.active
        x.inactive = not x.inactive
        x.save()
    
        return redirect('active-inactive')

def assign(request,id):
    if request.method == 'POST':
        global nav_context
        choice=request.POST['dep']
        x=Student.objects.get(ID=id)
        context={
                'num':0,
                'lname':nav_context['lname'],
                'userName':nav_context['userName']
            }
        x.dep=choice
        x.save()
        context['num'] = 1
        return render(request, "search.html", context)

def getSt(request):
    if request.method == 'POST':
        if request.POST.get('search') == "":
            context={
                'num':4,
                'lname':nav_context['lname'],
                'userName':nav_context['userName']
                }
            return render(request, 'search.html', context)
        choice=request.POST['select']
        if choice== 'id':
            x=Student.objects.filter(ID__startswith=request.POST['search'],active = True)
            context={
                    'students':x,
                    'lname':nav_context['lname'],
                    'userName':nav_context['userName']
                }
            if x:
                return render(request,'department_assignment.html',context)
            else:
                context={
                        'num':2,
                        'lname':nav_context['lname'],
                        'userName':nav_context['userName']
                    }
                return render(request,"search.html",context)        
        else:
            x=Student.objects.filter(name__startswith=request.POST['search'],active = True)
            context={
                    'students':x,
                    'lname':nav_context['lname'],
                    'userName':nav_context['userName']
                }
            if x:
                return render(request,'department_assignment.html',context)
            else:
                context={
                        'num':2,
                        'lname':nav_context['lname'],
                        'userName':nav_context['userName']
                    }
                return render(request,"search.html",context)
