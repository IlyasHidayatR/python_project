import qrcode
import PySimpleGUI as sg

# Create a QR Code
def createQRCode(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QR Code/" + filename + ".png")

# Create a GUI
layout = [
    [sg.Text("QR Code Generator")],
    [sg.Text("Data"), sg.InputText()],
    [sg.Text("Filename"), sg.InputText()],
    [sg.Button("Generate")]
]

window = sg.Window("QR Code Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Generate":
        createQRCode(values[0], values[1])
        sg.popup("QR Code generated")
window.close()