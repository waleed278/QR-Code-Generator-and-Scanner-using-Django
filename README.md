# 📱 QR Code Generator & Scanner (Django Project)

This is a **Django-based web application** that allows users to **generate** and **scan** QR codes instantly.  
The app uses the **`qrcode`** and **`pyzbar`** libraries for QR processing and integrates file upload, validation, and live decoding — all handled efficiently in memory using `BytesIO`.

---

## 🚀 Features

✅ **QR Code Generator**  
- Users can generate a QR code on the basis of their phone number and total bill amount 
- The QR code is generated dynamically and can be downloaded as an image.  

✅ **QR Code Scanner**  
- Users can upload any QR code image.  
- The app instantly scans and decodes the embedded text or URL.  

✅ **In-Memory Processing**  
- The uploaded QR image is temporarily stored in RAM using `BytesIO` before saving to disk, improving performance and reducing I/O load.

✅ **Error Handling**  
- Proper validation for empty uploads or invalid QR images.  
- User-friendly messages for incorrect files.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django |
| **Language** | Python |
| **Frontend** | HTML, CSS (Bootstrap) |
| **QR Libraries** | `qrcode`, `OpenCV`, `Pillow` |
| **In-memory File Handling** | `io.BytesIO` |

---



### 1️⃣ Clone the Repository
```bash
git clone https://github.com/waleed278/QR-Code-Generator-and-Scanner-using-Django.git
