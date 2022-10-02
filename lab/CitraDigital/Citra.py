import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

#nama image file temporary setiap kali processing output
filename_out = "out.png"

# Kolom Area No 1: Area open folder and select image
file_list_column = [
 [
 sg.Text("Open Image Folder :"),
 ],
 [
 sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
 sg.FolderBrowse(),
 ],
 [
 sg.Text("Choose an image from list :"),
 ],
 [
 sg.Listbox(
 values=[], enable_events=True, size=(18, 10), key="ImgList"
 )
 ],
 [
 sg.Text("Open Image Folder 2:"),
 ],
 [
 sg.In(size=(20, 1), enable_events=True, key="ImgFolder1"),
 sg.FolderBrowse(),
 ],
 [
 sg.Text("Choose an image from list :"),
 ],
 [
 sg.Listbox(
 values=[], enable_events=True, size=(18, 10), key="ImgList1"
 )
 ],
]
# Kolom Area No 2: Area viewer image input
image_viewer_column = [
 [sg.Text("Image Input :")],
 [sg.Text(size=(40, 1), key="FilepathImgInput")],
 [sg.Image(key="ImgInputViewer")],
 ]
# Kolom Area No 3: Area viewer image input 2
# image_viewer_column2 = [
#  [sg.Text("Image Input 2 :")],
#  [sg.Text(size=(40, 1), key="FilepathImgInput2")],
#  [sg.Image(key="ImgInputViewer2")],
# ]
# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
 [
 sg.Text("Image Information:"),
 ],
 [
 sg.Text(size=(20, 1), key="ImgSize"),
 ],
 [
 sg.Text(size=(20, 1), key="ImgColorDepth"),
 ],
 [
 sg.Text("List of Processing:"),
 ],
 [
 sg.Button("Image Negative", size=(20, 1), key="ImgNegative"),
 ],
 [
 sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"),
 ],
 [
 #mengatur kecerahan
 sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness"),
 ],
 [
 #mengatur blend
 sg.Button("Image Blend", size=(20, 1), key="ImgBlend"),
 ],
 [
 #mengatur power law
 sg.Button("Image Power Law", size=(20, 1), key="ImgPowerLaw"),
 ],
 [
 #mengatur logaritma
 sg.Button("Image Logaritma", size=(20, 1), key="ImgLogaritma"),
 ],
 [
 #mengatur transhold
    sg.Button("Image Transhold", size=(20, 1), key="ImgTranshold"),
 ]
]
# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
 [sg.Text("Image Processing Output:")],
 [sg.Text(size=(40, 1), key="ImgProcessingType")],
 [sg.Image(key="ImgOutputViewer")],
]
# Gabung Full layout
layout = [
 [
 sg.Column(file_list_column),
 sg.VSeperator(),
 sg.Column(image_viewer_column),
 sg.VSeperator(),
 sg.Column(list_processing),
 sg.VSeperator(),
 sg.Column(image_viewer_column2),
 ]
]
window = sg.Window("Mini Image Editor", layout)
# Run the Event Loop
while True:
 event, values = window.read()
 if event == "Exit" or event == sg.WIN_CLOSED:
    break
 # Folder name was filled in, make a list of files in the folder
 if event == "ImgFolder":
    folder = values["ImgFolder"]
    try:
    # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []
    fnames = [
    f
    for f in file_list
    if os.path.isfile(os.path.join(folder, f))
    and f.lower().endswith((".png", ".gif", ".jpg"))
    ]
    window["ImgList"].update(fnames)
 
 elif event == "ImgFolder1":
    folder = values["ImgFolder1"]
    try:
    # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []
    fnames = [
    f
    for f in file_list
    if os.path.isfile(os.path.join(folder, f))
    and f.lower().endswith((".png", ".gif", ".jpg"))
    ]
    window["ImgList1"].update(fnames) 
 elif event == "ImgList": # A file was chosen from the listbox
    try:
        filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
        window["FilepathImgInput"].update(filename)
        window["ImgInputViewer"].update(filename=filename)
        window["ImgProcessingType"].update(filename)
        window["ImgOutputViewer"].update(filename=filename)
        img_input = Image.open(filename)
        #img_input.show()

        #Size
        img_width, img_height = img_input.size
        window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height))

        #Color depth
        mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB":
        24, "HSV": 24, "I": 32, "F": 32}
        coldepth = mode_to_coldepth[img_input.mode]
        window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
    except:
        pass
 elif event == "ImgList1": # A file was chosen from the listbox
    try:
        filename = os.path.join(values["ImgFolder1"], values["ImgList1"][0])
        img_input1 = Image.open(filename)
        #img_input.show()
    except:
        pass
 elif event == "ImgNegative":

    try:
        window["ImgProcessingType"].update("Image Negative")
        img_output=ImgNegative(img_input,coldepth)
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass
 elif event == "ImgRotate":

    try:
        window["ImgProcessingType"].update("Image Rotate")
        img_output=ImgRotate(img_input,coldepth,90,"C")
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ImgBrightness":

     try:
         window["ImgProcessingType"].update("Image Brightness")
         img_output=ImgBrightness(img_input,coldepth,50)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 
 elif event == "ImgBlend":
    
     #event blending 2 gambar
     try:
         window["ImgProcessingType"].update("Image Blend")
         #ambil gambar input 2
         img_output=ImgBlend(img_input,img_input1,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgPowerLaw":
        
     try:
         window["ImgProcessingType"].update("Image Power Law")
         img_output=ImgPowerLaw(img_input,coldepth,2)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgLogaritma":
            
     try:
         window["ImgProcessingType"].update("Image Logaritma")
         img_output=ImgLogTransform(img_input,coldepth,50)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 
 elif event == "ImgTranshold":
                
     try:
         window["ImgProcessingType"].update("Image Transhold")
         img_output=ImgThreshold(img_input,coldepth,50)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

window.close()  