import datetime
from django.utils.timezone import utc
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreationForm
from userData.models import walletData,DataUser
from payment.models import paymentData

def index(request):

    uwallet = walletData.objects.filter().order_by('-id')[:1]
    udata = DataUser.objects.all()
    pay = paymentData.objects.filter().order_by('-id')[:1]

    context ={
      'judul':'.demo',
      'content':'Wellcome to my web.',
      'webname': 'demo',
      'uwallet': uwallet,
      'udata':udata,
      'pay': pay,
    }

    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("userdata")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm

    context={
        'form': form,
    }

    
    return render(request, "main/register.html", context)