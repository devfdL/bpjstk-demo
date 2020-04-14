from django.shortcuts import render
from .forms import payForm,payVer
from .models import paymentData
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from userData.models import DataUser,walletData
import base64
import random
import datetime,pytz
from twilio.rest import Client
from PIL import Image
import cv2,os
import numpy as np
import time
import csv
import sys
from io import BytesIO
from os import path


# Create your views here.
def index(request):

    if path.exists(request.user.username+'.png'):
      os.remove(request.user.username+'.png')

    form = payForm()
    formver = payVer()

    udata = DataUser.objects.all()
    global notelp
    for data in udata:
      if data.user_name == request.user.username:
        nik = data.nik
        notelp = data.hp_number

    context ={
      'judul':'.demo',
      'content':'Wellcome to my web.',
      'webname': 'demo',
      'form': form,
    }

    global target
    global amount
    global base64_message
    global ver_kode
    global base64_face
    global face_sign

    if request.method == 'POST':
      target = request.POST['target']
      amount = request.POST['amount']
      paymentchoice = request.POST['paymentchoice']

      if paymentchoice == 'Pay with Whatsapp Verification':
        transaction_sign = nik + '=' + notelp +  '=' + target +  '=' + amount
        #encryp transaction_sign
        message_bytes = transaction_sign.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii') #encrypted transaction_sign

        dtobj1=datetime.datetime.utcnow()
        dtobj3=dtobj1.replace(tzinfo=pytz.UTC)

        time = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%H:%M:%S') 
        date = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%d-%m-%Y') 
        
        kode = random.randint(100000, 999999)
        ver_kode = str(kode)
        msg = 'Anda melakukan transaksi dengan ' + target + ' dengan nominal pembelian Rp.' + amount + ' pada ' + time + ' ' + date + '.\nSilahkan masukan kode verifikasi jika setuju.\nKode: ' + ver_kode
        account_sid = 'ACfd8d4d3d7403fc578db5b8766c8432d6'
        auth_token = 'c60dddb5049c6bd7fb1be5424358a9b8'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body=msg,
        from_='whatsapp:+14155238886',
        to='whatsapp:'+notelp
        )
        return redirect("paymentver")

      if paymentchoice == 'Pay with face Verification':
        transaction_sign = nik + '=' + notelp +  '=' + target +  '=' + amount
        face_sign = nik + '=' + notelp 

        #encryp transaction_sign
        message_bytes = transaction_sign.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii') #encrypted transaction_sign

        #encryp face_sign
        message_bytes = face_sign.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_face = base64_bytes.decode('ascii') #encrypted transaction_sign 

        return redirect("paymentface")

      
    return render(request,'payment/index.html', context)

def ver(request):
    formver = payVer()

    udata = DataUser.objects.all()
    for data in udata:
      if data.user_name == request.user.username:
        nik = data.nik
        notelp = data.hp_number

    context ={
      'judul':'.demo',
      'content':'Wellcome to my web.',
      'webname': 'demo',
      'form': formver,
    }

    dtobj1=datetime.datetime.utcnow()
    dtobj3=dtobj1.replace(tzinfo=pytz.UTC)

    time = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%H:%M:%S') 
    date = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%d-%m-%Y') 

    if request.method == 'POST':
      payver = request.POST['payver']
      if payver == ver_kode:
        paymentData.objects.create(
          costumer_id = nik,
          source = request.user.username,
          target = target,
          date = date,
          time = time,
          amount = amount,
          transaction_sign = base64_message,
        )
        a = walletData.objects.filter().order_by('-id')[:1]
        for n in a:
          if n.user_name == request.user.username:
            data = int(n.wallet) - int(amount)
            point = n.point
            print(data)
            walletData.objects.create(
              user_name = request.user.username,
              wallet = str(data),
              point = point,
              last_transaction = date + ' ' + time
            )
        
        dtobj1=datetime.datetime.utcnow()
        dtobj3=dtobj1.replace(tzinfo=pytz.UTC)

        time = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%H:%M:%S') 
        date = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%d-%m-%Y') 
        
        msg = 'Anda sukses melakukan transaksi dengan ' + target + '. Nominal pembelian Rp.' + amount + ' pada ' + time + ' ' + date + '.'
        account_sid = 'ACfd8d4d3d7403fc578db5b8766c8432d6'
        auth_token = 'c60dddb5049c6bd7fb1be5424358a9b8'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body=msg,
        from_='whatsapp:+14155238886',
        to='whatsapp:'+notelp
        )

        return redirect("home")
 
    return render(request,'payment/ver.html', context)

def payface(request):

    udata = DataUser.objects.all()
    for data in udata:
      if data.user_name == request.user.username:
        nik = data.nik
        notelp = data.hp_number

    context ={
      'judul':'.demo',
      'content':'Wellcome to my web.',
      'webname': 'demo',
    }

    dtobj1=datetime.datetime.utcnow()
    dtobj3=dtobj1.replace(tzinfo=pytz.UTC)

    time = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%H:%M:%S') 
    date = dtobj3.astimezone(pytz.timezone("Asia/Jakarta")).strftime('%d-%m-%Y') 

    if request.method == 'POST':
      facesign = request.POST['facesign']
      
      data_face = facesign.replace('data:image/png;base64,', '')

      im = Image.open(BytesIO(base64.b64decode(str(data_face))))
      im.save(request.user.username+'.png', 'PNG')

      path = os.path.dirname(os.path.abspath(__file__))
      recognizer = cv2.face.LBPHFaceRecognizer_create()
      recognizer.read('../face/trainer/trainer.yml')
      cascadePath = "../face/Classifiers/face.xml"
      faceCascade = cv2.CascadeClassifier(cascadePath);

      cam = cv2.imread(request.user.username+'.png')
      font = cv2.FONT_HERSHEY_SIMPLEX

      gray=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
      faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
      for(x,y,w,h) in faces:
          nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
          cv2.rectangle(cam,(x-50,y-50),(x+w+50,y+h+50),(10,255,255), 2)

          with open('../face/data-face.csv') as csvfile:
              database = csv.DictReader(csvfile)
              for row in database:
                  face_id = row['id']
                  face_username = row['username']
                  f_sign = row['face_sign']
                  if str(nbr_predicted) == face_id:
                      #print('Detected: ' + face_username)
                      if conf < 65:
                          cv2.putText(cam,face_username+"--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                          print(face_username+"--"+str(conf)+ '--' +f_sign)
                          if face_username == request.user.username:
                            if f_sign == base64_face:
                              print('pembayaran sukses')
                              paymentData.objects.create(
                                costumer_id = nik,
                                source = request.user.username,
                                target = target,
                                date = date,
                                time = time,
                                amount = amount,
                                transaction_sign = base64_message,
                              )
                              a = walletData.objects.filter().order_by('-id')[:1]
                              for n in a:
                                if n.user_name == request.user.username:
                                  data = int(n.wallet) - int(amount)
                                  point = n.point
                                  print(data)
                                  walletData.objects.create(
                                    user_name = request.user.username,
                                    wallet = str(data),
                                    point = point,
                                    last_transaction = date + ' ' + time
                                  )

                              msg = 'Anda sukses melakukan transaksi dengan ' + target + '. Nominal pembelian Rp.' + amount + ' pada ' + time + ' ' + date + ', menggunakan metode face recognition.'
                              account_sid = 'ACfd8d4d3d7403fc578db5b8766c8432d6'
                              auth_token = 'c60dddb5049c6bd7fb1be5424358a9b8'
                              client = Client(account_sid, auth_token)

                              message = client.messages.create(
                              body=msg,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+notelp
                              )
                              return redirect("home")
                      else:
                          cv2.putText(cam,"unknown--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                          print("unknown--"+str(conf))
                          return redirect("paymentver") 
                  else:
                      cv2.putText(cam,"unknown--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                      print("unknown--") 
                      return redirect("paymentver")


          cv2.imshow('Recognition',cam)

      cv2.destroyAllWindows()

    return render(request,'payment/facever.html', context)