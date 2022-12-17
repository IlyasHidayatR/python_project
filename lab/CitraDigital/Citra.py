import PySimpleGUI as sg
import numpy as np
import os.path
from PIL import Image, ImageOps
from processing_list import *

#nama image file temporary setiap kali processing output
filename_out = "lab\CitraDigital\output.png"

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
#  [
#  sg.Button("Image Negative", size=(20, 1), key="ImgNegative"),
#  ],
#  [
#  #inputan derajat rotasi
#  sg.Text("Degree of Rotation:"),
#  sg.InputText(size=(5, 1), key="DegRotation"),
#  ],
#  [
#  sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"),
#  ],
#  [
#  #input kecerahan gambar
#  sg.Text("Brightness Image:"),
#  sg.InputText(size=(5, 1), key="Brightness"),
#  ],
#  [
#  #mengatur kecerahan
#  sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness"),
#  ],
#  [
#  #mengatur blend gambar dengan nilai
#  sg.Text("Blend Image:"),
#  sg.InputText(size=(5, 1), key="Blend"),
#  ],
#  [
#  #mengatur blend
#  sg.Button("Image Blend", size=(20, 1), key="ImgBlend"),
#  ],
#  [
#  #mengatur power law dengan input nilai gamma
#  sg.Text("Gamma Value:"),
#  sg.InputText(size=(5, 1), key="Gamma"),
#  ],
#  [
#  #mengatur power law
#  sg.Button("Image Power Law", size=(20, 1), key="ImgPowerLaw"),
#  ],
#  [
#  #input mengatur kecerahan log transform
#  sg.Text("Log Transform:"),
#  sg.InputText(size=(5, 1), key="BrightnessLog"),
#  ],
#  [
#  #mengatur logaritma
#  sg.Button("Image Logaritma", size=(20, 1), key="ImgLogaritma"),
#  ],
#  [
#  #input mengatur transhold
#  sg.Text("Transhold Value:"),
#  sg.InputText(size=(5, 1), key="Transhold"),
#  ],
#  [
#  #mengatur transhold
#  sg.Button("Image Transhold", size=(20, 1), key="ImgTranshold"),
#  ],
#  [
#  #input x dan y translasi
#  sg.Text("X :"),
#  sg.InputText(size=(5, 1), key="XTranslasi"),
#  sg.Text("Y :"),
#  sg.InputText(size=(5, 1), key="YTranslasi"),
#  ],
#  [
#  #mengatur translasi
#  sg.Button("Image Translasi", size=(20, 1), key="ImgTranslasi"),
#  ],
#  [
#  #input flipping V, H, atau VH
#  sg.Text("Flip Direct (V/H/HV):"),
#  sg.InputText(size=(5, 1), key="FlipDirection"),
#  ],
#  [
#  #mngatur flipping gambar
#  sg.Button("Image Flipping", size=(20, 1), key="ImgFlipping"),
#  ],
#  [
#  #input zoom in dan zoom out
#  sg.Text("Zoom In/Out (value):"),
#  sg.InputText(size=(5, 1), key="ZoomInOut"),
#  ],
#  [
#  #tombol zoom in
#  sg.Button("Image Zoom In", size=(20, 1), key="ImgZoomIn"),
#  ],
#  [
#  #tombol zoom out
#  sg.Button("Image Zoom Out", size=(20, 1), key="ImgZoomOut"),
#  ],
#  [
#  #tombol engatur gambar di tengah berbentuk lingkaran menjadi negatif
#  sg.Button("Image Negative Circle", size=(20, 1), key="ImgNegativeCircle"),
#  ],
#  [
#  #tombol engatur gambar di tengah berbentuk belah ketupat menjadi negatif
#  sg.Button("Image Negative Diamond", size=(20, 1), key="ImgNegativeCenter"),
#  ],
#  [
#  #tombol mengautur filpping gambar menjadi satu
#  sg.Button("Image Flipping All", size=(20, 1), key="ImgFlippingAll"),
#  ],
#  [
#  #tombol blending gambar dengan gambar lain ukuran satu per empat gambar di pojok atas kiri
#  sg.Button("Image Blend 1/4", size=(20, 1), key="ImgBlend1/4"),
#  ],
#  [
#  #tombol fungsi semua rotasi gambar dengan derajat original, 90, 180, 270 menjadi satu
#  sg.Button("Image Rotate All", size=(20, 1), key="ImgRotateAll"),
#  ],
#  [
#  #tombol blending gambar dengan gambar lain ukuran satu per empat gambar di pojok atas kiri
#  sg.Button("Image Blend 1/4 ke-2", size=(20, 1), key="ImgBlend1/4New"),
#  ],
#  [
#  #tombol blending gambar dengan gambar lain ukuran satu per empat gambar di pojok bawah kiri
#  sg.Button("Image Blend 1/4 ke-3", size=(20, 1), key="ImgBlend1/4New1"),
#  ],
#  [
#  #fungsi negatif gambar trianggle
#  sg.Button("Image Negative Triangle", size=(20, 1), key="ImgNegativeTriangle"),
#  ],
#  [
#  #fungsi mengatur gambar di tengah berbentuk lingkaran menjadi negatif dan belah ketupat menjadi gambar asli
#  sg.Button("Image Negative Circle & Diamond", size=(20, 1), key="ImgNegativeCircleDiamond"),
#  ],
#  [
#  #ImgNegativeCircleDiamondTriangle
#  sg.Button("Image Negative Circle & Diamond & Triangle", size=(20, 1), key="ImgNegativeCircleDiamondTriangle"),
#  ],
#  [
#  #image median filter
#  sg.Button("Image Median Filter", size=(20, 1), key="ImgMedianFilter"),
#  ],
#  [
#  #image mean filter
#  sg.Button("Image Mean Filter", size=(20, 1), key="ImgMeanFilter"),
#  ],
#  [
#  #image max filter
#  sg.Button("Image Max Filter", size=(20, 1), key="ImgMaxFilter"),   
#  ],
#  [
#  #image min filter
#  sg.Button("Image Min Filter", size=(20, 1), key="ImgMinFilter"),
#  ],
 [
 #input mask value for linear filter
#  sg.Text("Mask Value:"),
#  sg.InputText(size=(5, 1), key="MaskValue"),
 ],
 [
 #convesinal linear filter
 sg.Button("Weight Average Filter", size=(20, 1), key="ImgConvesinalLinearFilter"),
 ],
 [
 #convesinal linear filter
 sg.Button("Weight Average Filter 2", size=(20, 1), key="ImgConvesinalLinearFilter1"),
 ],
 [
 #gradient filter
 sg.Button("Gradient Filter", size=(20, 1), key="ImgGradientFilter"),
 ],
 [
 #gradient filter 1
 sg.Button("Gradient Filter 1", size=(20, 1), key="ImgGradientFilter1"),
 ],
 [
 #Sharpening Filter
 sg.Button("Sharpening Filter", size=(20, 1), key="ImgSharpenFilter"),
 ],
 [
 #laplacian filter
 sg.Button("Laplacian Filter", size=(20, 1), key="ImgLaplacianFilter"), 
 ],
 [
 #roberts filter
 sg.Button("Roberts Filter", size=(20, 1), key="ImgRobertsFilter"),
 ],
 [
 #sobel filter
 sg.Button("Sobel Filter", size=(20, 1), key="ImgSobelFilter"),
 ],
 [
 #prewitt filter
 sg.Button("Prewitt Filter", size=(20, 1), key="ImgPrewittFilter"),
 ],
 [
 #compass filter
 sg.Button("Compass Filter", size=(20, 1), key="ImgCompassFilter"),
 ],
 [
 #canny filter
 sg.Button("Canny Filter", size=(20, 1), key="ImgCannyFilter"),
 ],
 [
 #noise gaussian filter
 sg.Button("Noise Gaussian Filter", size=(20, 1), key="ImgNoiseGaussianFilter"),
 ],
 [
 #salt noise filter
 sg.Button("Salt Noise Filter", size=(20, 1), key="ImgSaltNoiseFilter"),
 ],
 [
 #pepper noise filter
 sg.Button("Pepper Noise Filter", size=(20, 1), key="ImgPepperNoiseFilter"),
 ],
 [
 #gaussian filter
 sg.Button("Gaussian Filter", size=(20, 1), key="ImgGaussianFilter"),
 ],
 [
 #Erosion Binary Filter
 sg.Button("Erosion Binary Filter", size=(20, 1), key="ImgErosionBinaryFilter"),
 ],
 [
 #Dilation Binary Filter
 sg.Button("Dilation Binary Filter", size=(20, 1), key="ImgDilationBinaryFilter"),
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
        derajat = int(values["DegRotation"])
        img_output=ImgRotate(img_input,coldepth,derajat,"C")
        img_output.save(filename_out)
        window["ImgOutputViewer"].update(filename=filename_out)
    except:
        pass

 elif event == "ImgBrightness":

     try:
         window["ImgProcessingType"].update("Image Brightness")
         brightness = int(values["Brightness"])
         img_output=ImgBrightness(img_input,coldepth,brightness)
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
         gamma = float(values["Gamma"])
         img_output=ImgPowerLaw(img_input,coldepth,gamma)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgLogaritma":
            
     try:
         window["ImgProcessingType"].update("Image Logaritma")
         c = float(values["BrightnessLog"])
         img_output=ImgLogTransform(img_input,coldepth,c)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 
 elif event == "ImgTranshold":
                
     try:
         window["ImgProcessingType"].update("Image Transhold")
         trans_value = int(values["Transhold"])
         img_output=ImgThreshold(img_input,coldepth,trans_value)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgTranslasi":
    
     try:
         window["ImgProcessingType"].update("Image Translasi")
         x = int(values["XTranslasi"])
         y = int(values["YTranslasi"])
         img_output=ImgTranslation(img_input,coldepth,x,y)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgFlipping":
       
     try:
         window["ImgProcessingType"].update("Image Flipping")
         jenis_flip = values["FlipDirection"]
         img_output=ImgFlipping(img_input,coldepth,jenis_flip)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgZoomOut":

     try:
         window["ImgProcessingType"].update("Image Zoom Out")
         step = int(values["ZoomInOut"])
         img_output=ImgZoomOut(img_input,coldepth,step)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgZoomIn":
        
     try:
         window["ImgProcessingType"].update("Image Zoom In")
         step = int(values["ZoomInOut"])
         img_output=ImgZoomIn(img_input,coldepth,step)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgNegativeCircle":

     try:
         window["ImgProcessingType"].update("Image Negative Circle")
         img_output=ImgNegativeCircle(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgNegativeCenter":

     try:
         window["ImgProcessingType"].update("Image Negative Center")
         img_output=ImgNegativeDiamond(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 
 elif event == "ImgFlippingAll":

     try:
         window["ImgProcessingType"].update("Image Flipping All")
         img_output=ImgFlipAll(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgBlend1/4":

     try:
         window["ImgProcessingType"].update("Image Blend 1/4")
         img_output=ImgBlendQuarter(img_input,img_input1,coldepth,40)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgRotateAll":

     try:
         window["ImgProcessingType"].update("Image Rotate All")
         img_output=ImgRotateAll(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgBlend1/4New":

     try:
         window["ImgProcessingType"].update("Image Blend 1/4")
         img_output=ImgBlendQuarter1(img_input,img_input1,coldepth,0)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgBlend1/4New1":

     try:
         window["ImgProcessingType"].update("Image Blend 1/4")
         img_output=ImgBlendQuarter2(img_input,img_input1,coldepth,0)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgNegativeTriangle":

        try:
            window["ImgProcessingType"].update("Image Negative Triangle")
            img_output=ImgNegatifTriangle(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

 elif event == "ImgNegativeCircleDiamond":

     try:
         window["ImgProcessingType"].update("Image Negative Circle Diamond")
         img_output=ImgNegativeCircleDiamond(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgNegativeCircleDiamondTriangle":

     try:
         window["ImgProcessingType"].update("Image Negative Circle Diamond Triangle")
         img_output=ImgNegativeCircleDiamondTriangle(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgMedianFilter":

     try:
         window["ImgProcessingType"].update("Image Median Filter")
         img_output=ImgMedianFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgMeanFilter":

     try:
         window["ImgProcessingType"].update("Image Mean Filter")
         img_output=ImgMeanFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgMinFilter":

     try:
         window["ImgProcessingType"].update("Image Min Filter")
         img_output=ImgMinFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgMaxFilter":

     try:
         window["ImgProcessingType"].update("Image Max Filter")
         img_output=ImgMaxFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgConvesinalLinearFilter":

     try:
         window["ImgProcessingType"].update("Image Convesional Linear Filter")
         img_output=ImgLinearFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 
 elif event == "ImgConvesinalLinearFilter1":

     try:
         window["ImgProcessingType"].update("Image Convesional Linear Filter")
         img_output=ImgLinearFilter1(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass
 elif event == "ImgGradientFilter":

     try:
         window["ImgProcessingType"].update("Image Gradient Filter")
         img_output=ImgGradientEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgGradientFilter1":

     try:
         window["ImgProcessingType"].update("Image Gradient Filter")
         img_output=ImgGradientEdgeDetection2(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgSharpenFilter":

     try:
         window["ImgProcessingType"].update("Image Sharpen Filter")
         img_output=ImgSharpeningFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgLaplacianFilter":

     try:
         window["ImgProcessingType"].update("Image Laplacian Filter")
         img_output=ImgLaplacianEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgRobertsFilter":

     try:
         window["ImgProcessingType"].update("Image Roberts Filter")
         img_output=ImgRobertsEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgSobelFilter":

     try:
         window["ImgProcessingType"].update("Image Sobel Filter")
         img_output=ImgSobelEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgPrewittFilter":

     try:
         window["ImgProcessingType"].update("Image Prewitt Filter")
         img_output=ImgPrewittEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgCompassFilter":

     try:
         window["ImgProcessingType"].update("Image Compass Filter")
         img_output=ImgCompassEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgCannyFilter":

     try:
         window["ImgProcessingType"].update("Image Canny Filter")
         img_output=ImgCannyEdgeDetection(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgNoiseGaussianFilter":

     try:
         window["ImgProcessingType"].update("Image Noise Gaussian Filter")
         img_output=ImgNoiseGaussianFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgSaltNoiseFilter":

     try:
         window["ImgProcessingType"].update("Image Salt Noise Filter")
         img_output=ImgSaltNoise(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgPepperNoiseFilter":

     try:
         window["ImgProcessingType"].update("Image Pepper Noise Filter")
         img_output=ImgPaperNoise(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgGaussianFilter":

     try:
         window["ImgProcessingType"].update("Image Gaussian Filter")
         img_output=ImgGaussianFilter(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgErosionBinaryFilter":

     try:
         window["ImgProcessingType"].update("Image Erosion Binary Filter")
         img_output=ImgErosionBinary(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

 elif event == "ImgDilationBinaryFilter":

     try:
         window["ImgProcessingType"].update("Image Dilation Binary Filter")
         img_output=ImgDilationBinary(img_input,coldepth)
         img_output.save(filename_out)
         window["ImgOutputViewer"].update(filename=filename_out)
     except:
         pass

window.close()  