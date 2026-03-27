import qrcode

data = "http://192.168.21.1/Site-hebergement/"
qr = qrcode.make(data)
qr.save("mon_premier_site.png")
