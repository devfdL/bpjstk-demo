from django.shortcuts import render
from .forms import walletForm,userForm
from .models import DataUser,walletData
from django.shortcuts import redirect

# Create your views here.
def index(request):
    uform = userForm()
   
    context ={
      'judul':'.demo',
      'content':'Wellcome to my web.',
      'webname': 'demo',
      'uform': uform,
    }

    if request.method == 'POST':
      nik = request.POST['nik']
      hp_number = request.POST['hp_number']
      alamat = request.POST['alamat']
      ttl = request.POST['ttl']
      pekerjaan = request.POST['pekerjaan']
      user_signature = request.POST['user_signature']

      DataUser.objects.create(
        nik = nik,
        user_name = request.user.username,
        alamat = alamat,
        ttl = ttl,
        pekerjaan = pekerjaan,
        user_signature = user_signature,
        hp_number = hp_number,
      )
      return redirect("home")
      
    return render(request,'userdata/index.html', context)