import qrcode

# Generating the qr static image for link
img = qrcode.make("https://iftiahmed01.github.io/My_Online_Portfolio/")

img.save("qr.png")