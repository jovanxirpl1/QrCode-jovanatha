import qrcode
import image
qr =qrcode.QRCode(
    version = 15,#versi qr code
    box_size = 10, #untuk ukuran qrcode
    border = 5#ukuran putih putih qrcode
)

data = "https://youtu.be/CwGbMYLjIpQ?si=xLN_chdwc8c_rfMH"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white") #seting warna qrcode
img.save("image.jpg")