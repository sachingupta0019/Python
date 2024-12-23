import qrcode
img = qrcode.make("Name = Sachin Gupta ")
type(img)
img.save("sachin.png")