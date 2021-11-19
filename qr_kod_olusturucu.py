import qrcode # Qr kod kütüphanesini yüklemek için terminale pip install qrcode pillow yazınız.

code = qrcode.QRCode(
    version = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100, # Boyutu
    border = 3 # Kenar kalınlığı
)

code.add_data("https://github.com/hypenosoncode") # Buraya istediğiniz linki, metni vs. ekleyin.
code.make(fit = True)

image = code.make_image(fill_color = "black", back_color = "white") # Renk ismi yerine (8, 153, 206) bu şekilde renk uzayı da yazılabilir.
image.save("qr_kodu.png") # Çıkan dosyanın adı bu şekilde olacaktır.

print("QR oluşturma işlemi başarılı")