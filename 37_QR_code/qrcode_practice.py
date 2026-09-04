import qrcode
data = "Hello Shravya"
img = qrcode.make(data)
img.save("my_qrcode.png")
print("QR code created succesfully!")