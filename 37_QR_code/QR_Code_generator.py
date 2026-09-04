import qrcode

print("=== QR CODE GENERATOR ===")
text = input("Enter text or URL: ")
image = qrcode.make(text)
name = input("Enter file name: ")
image.save(name)

print(f"\nQR Code created succesfully!\n Saved as {name}")
