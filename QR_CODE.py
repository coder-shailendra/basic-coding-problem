import qrcode

url = input("Enter your URL: ")

qr = qrcode.make(url)
qr.save("website_qr.png")

print("QR Code generated successfully!")