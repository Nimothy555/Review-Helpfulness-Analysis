import qrcode

qr = qrcode.make("https://rent-wise.live/")
qr.save("rentwise_qr.png")
print("Saved rentwise_qr.png")
