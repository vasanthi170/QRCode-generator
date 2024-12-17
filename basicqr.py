import qrcode

generate_image = qrcode.make("Linkedin")
generate_image.save('image1.png')