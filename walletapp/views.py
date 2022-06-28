from django.shortcuts import render
from .form import ExpForm
from .models import balance,update_balance,expences
# Create your views here.

def home(request):
    return render(request,'common.html')
def add_money(req):
    try:
        if req.method == "POST":
                          
            amounts=req.POST['money']
            
            amt=update_balance.objects.get(id=1)
            total=float(str(amt)) + float(amounts)
            
            amt.new_balance =total  # change field
            amt.save()
            bal=balance(amount=amounts)
            bal.save()
            
            
            return render(req,'add_money.html',{'msg':"money added successfully"})
        else:
            return render(req,'add_money.html')
    except Exception as ex:
        print(ex)
        return render(req,'add_money.html',{'msg':"money cannot be added"})



def add_expence(req):
    try:
        if req.method == "POST":
            
            form = ExpForm(req.POST)
            if form.is_valid():
                
                amounts=form['pay'].value()
                amt=update_balance.objects.get(id=1)
                total=float(str(amt)) - float(amounts)
                
                amt.new_balance =total
                amt.save()
                form.save()
                return render(req,'expence.html',{'msg':"Expense added"})
        else:
            forms=ExpForm()
            f_dict={'form':forms}                
            return render(req,'expence.html',f_dict)
    except Exception as e:
        print(e)
        return render(req,'expence.html',{'msg':"Expense cannot be added"})

def view_balance(req):
    money=update_balance.objects.get(id=1)
    return render(req,'balance.html',{'msg': money})

def view_expence(request):
    exp=expences.objects.all()
    return render(request,'view_expences.html',{'msg':exp})