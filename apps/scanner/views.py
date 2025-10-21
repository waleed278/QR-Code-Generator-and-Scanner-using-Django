from django.shortcuts import render
from .models import QRCode
import qrcode
from .forms.form_generate import GenerateForm
from .forms.form_scanner import ScannerForm
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import uuid
from django.conf import settings
import cv2
import os
from io import BytesIO
from pathlib import Path

def home(request):
    return render(request, "scanner/home.html")

def Generate(request):
    qr_image_url = None
    if request.method == "POST":
        form = GenerateForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']

            unique_id = uuid.uuid4().hex[:6]
            filename = f"{amount}_{phone}_{unique_id}.png"
            qr_content = f"{phone}|{amount}"
            qr = qrcode.make(qr_content)
            qr_image_io = BytesIO()
            qr.save(qr_image_io,format="PNG")
            qr_image_io.seek(0)

            qr_storage_path = settings.MEDIA_ROOT / 'qr_code'
            fs = FileSystemStorage(location=qr_storage_path , base_url='/media/qr_code/')
            qr_image_content = ContentFile(qr_image_io.read(),name=filename)
            filepath = fs.save(filename,qr_image_content)
            qr_image_url = fs.url(filename)
            QRCode.objects.create(data=amount, mobile_number=phone, qr_filename=filename)
        else:
            print(form.errors)
    else:
        form = GenerateForm()
    return render(request, "scanner/generate.html", {'form': form, 'qr_image_url': qr_image_url})


def Scanner(request):
    result = None
    if request.method =="POST":
        form = ScannerForm(request.POST,request.FILES)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            image =  form.cleaned_data['image']

            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            image_path = Path(fs.location)/filename

            try:
                img = cv2.imread(str(image_path))
                detector = cv2.QRCodeDetector()
                qr_content,points,_ = detector.detectAndDecode(img)

                if qr_content:
                    qr_content = qr_content.strip()
                    qr_mobile , qr_data = qr_content.split('|')

                    qr_entry = QRCode.objects.filter(data=qr_data,mobile_number=qr_mobile).first()
                    if qr_entry:
                        result = "Scan Success: Valid QR code for the provided mobile number"
                        filename_to_delete = qr_entry.qr_filename
                        qr_entry.delete()
                        qr_image_path = os.path.join(settings.MEDIA_ROOT, 'qr_code',filename_to_delete)
                        if os.path.exists(qr_image_path):
                            os.remove(qr_image_path)

                        
                    else:
                        result = "Invalid QR code does not match the mobile number"
                
                else:
                    result = "No QR code is detected in the image"
                
            except Exception as e:
                result = f"Error processing in this images:{str(e)}"
          
            
        else:
            print(form.errors)
    

    else:
        form = ScannerForm()
    return render(request, "scanner/scanner.html", {'form': form, 'result': result})