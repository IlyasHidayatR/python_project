from PIL import Image, ImageOps
import math
import random

def ImgNegative(img_input,coldepth):
 #solusi 1
 #img_output=ImageOps.invert(img_input)
 #solusi 2
 if coldepth!=24:
    img_input = img_input.convert('RGB')

 img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
 pixels = img_output.load()
 for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
        r, g, b = img_input.getpixel((i, j))
        pixels[i,j] = (255-r, 255-g, 255-b)

 if coldepth==1:
    img_output = img_output.convert("1")
 elif coldepth==8:
    img_output = img_output.convert("L")
 else:
    img_output = img_output.convert("RGB")

 return img_output

def ImgRotate(img_input,coldepth,deg,direction):
 #solusi 1
 #img_output=img_input.rotate(deg)

 #solusi 2
 if coldepth!=24:
    img_input = img_input.convert('RGB')

 img_output = Image.new('RGB',(img_input.size[1],img_input.size[0]))
 pixels = img_output.load()
 for i in range(img_output.size[0]):
    for j in range(img_output.size[1]):
        if direction=="C":
            r, g, b = img_input.getpixel((j,img_output.size[0]-i-1))
        else:
            r, g, b = img_input.getpixel((img_input.size[1]-j-1,i))
        pixels[i,j] = (r, g, b)

 if coldepth==1:
    img_output = img_output.convert("1")
 elif coldepth==8:
    img_output = img_output.convert("L")
 else:
    img_output = img_output.convert("RGB")

 return img_output

#fungsi mengatur kecerahan gambar
def ImgBrightness(img_input,coldepth,brightness):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         pixels[i,j] = (r+brightness, g+brightness, b+brightness)
   
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")
   
   return img_output

#fungsi mengatur power law transform
def ImgPowerLaw(img_input,coldepth,gamma):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         pixels[i,j] = (int(255*(r/255)**gamma), int(255*(g/255)**gamma), int(255*(b/255)**gamma))
   
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")
   
   return img_output

#fungsi mengatur logaritma transform
def ImgLogTransform(img_input,coldepth,c):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         pixels[i,j] = (int(c*math.log(1+r)), int(c*math.log(1+g)), int(c*math.log(1+b)))
   
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")
   
   return img_output

#fungsi mengatur blending gambar
def ImgBlend(img_input,img_input2,coldepth):
   
   if coldepth!=24:
      img_input = img_input.convert('RGB')
      img_input2 = img_input2.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         r2, g2, b2 = img_input2.getpixel((i, j))
         pixels[i,j] = (int((r+r2)/2), int((g+g2)/2), int((b+b2)/2))
   
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")
   
   return img_output

#fungsi transhold gambar
def ImgThreshold(img_input,coldepth,threshold):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if (r+g+b)/3>threshold:
            pixels[i,j] = (255, 255, 255)
         else:
            pixels[i,j] = (0, 0, 0)
   
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")
   
   return img_output

#fungsi operator translation gambar
def ImgTranslation(img_input,coldepth,x,y):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         if i+x<img_input.size[0] and j+y<img_input.size[1]:
            r, g, b = img_input.getpixel((i+x, j+y))
            pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi operator Flipping gambar
def ImgFlipping(img_input,coldepth,flip):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         if flip=='O':
            r, g, b = img_input.getpixel((i, j))
         elif flip=='H':
            r, g, b = img_input.getpixel((img_input.size[0]-i-1, j))
         elif flip=='V':
            r, g, b = img_input.getpixel((i, img_input.size[1]-j-1))
         elif flip=='HV':
            r, g, b = img_input.getpixel((img_input.size[0]-i-1, img_input.size[1]-j-1))
         pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi zoom out gambar subsampling
def ImgZoomOut(img_input,coldepth,step):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0]//step,img_input.size[1]//step))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i*step, j*step))
         pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi zoom in gambar
def ImgZoomIn(img_input,coldepth,step):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((int(i/step), int(j/step)))
         pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi mengatur setengah gambar menjadi grayscale
def ImgGrayHalf(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i<img_input.size[0]//2:
            pixels[i,j] = (r, g, b)
         else:
            pixels[i,j] = (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi mengatur setengah diagonal gambar menjadi grayscale
def ImgGrayDiagonal(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i+j<img_input.size[0]:
            pixels[i,j] = (r, g, b)
         else:
            pixels[i,j] = (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi zoom out gambar subsampling
def ImgZoomOut(img_input,coldepth,step):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0]//step,img_input.size[1]//step)) #// untuk pembulatan ke bawah
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i*step, j*step))
         pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi zoom in gambar
def ImgZoomIn(img_input,coldepth,step):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((int(i/step), int(j/step)))
         pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi mengatur setengah gambar menjadi grayscale
def ImgGrayHalf(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i<img_input.size[0]//2:
            pixels[i,j] = (r, g, b)
         else:
            pixels[i,j] = (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi mengatur setengah diagonal gambar menjadi grayscale
def ImgGrayDiagonal(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i+j<img_input.size[0]:
            pixels[i,j] = (r, g, b)
         else:
            pixels[i,j] = (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi mengatur gambar di tengah berbentuk lingkaran menjadi negatif
def ImgNegativeCircle(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if (i-img_input.size[0]//2)**2+(j-img_input.size[1]//2)**2<img_input.size[0]**2//4:
            pixels[i,j] = (255-r, 255-g, 255-b)
         else:
            pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

#fungsi mengatur gambar di tengah berbentuk belah ketupat menjadi negatif
def ImgNegativeDiamond(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i+j<img_input.size[0]//2 or i+j>img_input.size[0]+img_input.size[1]//2 or i-j>img_input.size[0]//2 or j-i>img_input.size[1]//2:
            pixels[i,j] = (r, g, b)
         else:
            pixels[i,j] = (255-r, 255-g, 255-b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi menampilkan semua flipping gambar Original, Horizontal, Vertical, dan Horizontal+Vertical dalam 1 gambar
def ImgFlipAll(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB',(img_input.size[0]*2,img_input.size[1]*2))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         if i<img_input.size[0] and j<img_input.size[1]:
            r, g, b = img_input.getpixel((i, j))
            pixels[i,j] = (r, g, b)
         elif i>=img_input.size[0] and j<img_input.size[1]:
            r, g, b = img_input.getpixel((img_input.size[0]-i-1, j))
            pixels[i,j] = (r, g, b)
         elif i<img_input.size[0] and j>=img_input.size[1]:
            r, g, b = img_input.getpixel((i, img_input.size[1]-j-1))
            pixels[i,j] = (r, g, b)
         else:
            r, g, b = img_input.getpixel((img_input.size[0]-i-1, img_input.size[1]-j-1))
            pixels[i,j] = (r, g, b)

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")


   return img_output

#fungsi blending gambar dengan gambar ke-2 di zoom out subsampling 4 step berada posisi di pojok kiri atas
def ImgBlendQuarter(img_input,img_input2,coldepth,brigtness):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
      img_input2 = img_input2.convert('RGB')
   

   #lakukan blending gambar ke-1 dengan gambar ke-2
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   #lakukan zoom out subsampling 4 step pada gambar ke-2
   img_input2 = img_input2.resize((img_input2.size[0]//2,img_input2.size[1]//2))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i, j))
         if i<img_input2.size[0] and j<img_input2.size[1]:
            r2, g2, b2 = img_input2.getpixel((i, j))
            # lakukan blending dengan rumus (r1+r2)/2 dan (g1+g2)/2 dan (b1+b2)/2 dan brightness
            pixels[i,j] = ((int((r+r2)/2)+brigtness), int(((g+g2)/2)+brigtness), int(((b+b2)/2)+brigtness))
         else:
            pixels[i,j] = (r+brigtness, g+brigtness, b+brigtness)
   

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output


#fungsi menampilkan semua flipping gambar Original, Horizontal, rotasi 90 derajat dan rotasi 270 derajat dalam 1 gambar
def ImgRotateAll(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth != 24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (int(img_input.size[1]/2), int(img_input.size[0]/2)))
   pixels = img_output.load()

   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((i*2, j*2))
         pixels[i, j] = (r, g, b)

   canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
   canvas_pixels = canvas.load()

   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_output.getpixel((i, j))
         canvas_pixels[i, j] = (r, g, b)
         canvas_pixels[img_output.size[0]*2-1-i, j] = (r, g, b)
         canvas_pixels[i, img_output.size[1]*2-1-j] = (r, g, b)
         #rotating image 90 degree clockwise
         r, g, b = img_output.getpixel((j, img_output.size[0]-i-1))
         canvas_pixels[i+img_output.size[0], j+img_output.size[1]] = (r, g, b)

   if coldepth == 1:
      img_output = img_output.convert("1")
   elif coldepth == 8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return canvas


def ImgBlendQuarter1(img_input,img_input2,coldepth,brigtness):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
      img_input2 = img_input2.convert('RGB')
   

   #lakukan blending gambar ke-1 dengan gambar ke-2
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   #lakukan zoom out subsampling 2 step pada gambar ke-2
   img_input2 = img_input2.resize((img_input2.size[0]//2,img_input2.size[1]//2))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((img_input.size[0]-i-1, j))
         if i<img_input2.size[0] and j<img_input2.size[1]:
            # lakukan rotasi 90 derajat pada gambar ke-2 berlawanan arah jarum jam
            r2, g2, b2 = img_input2.getpixel((img_input2.size[0]-j-1, i))
            # lakukan blending dengan rumus (r1+r2)/2 dan (g1+g2)/2 dan (b1+b2)/2 dan brightness
            pixels[i,j] = ((int((r+r2)/2)+brigtness), int(((g+g2)/2)+brigtness), int(((b+b2)/2)+brigtness))
         else:
            pixels[i,j] = (r+brigtness, g+brigtness, b+brigtness)
   

   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

def ImgBlendQuarter2(img_input,img_input2,coldepth,brigtness):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
      img_input2 = img_input2.convert('RGB')
   

   #lakukan blending gambar ke-1 dengan gambar ke-2
   img_output = Image.new('RGB',(img_input.size[0],img_input.size[1]))
   #lakukan zoom out subsampling 2 step pada gambar ke-2
   img_input2 = img_input2.resize((img_input2.size[0]//2,img_input2.size[1]//2))
   pixels = img_output.load()
   for i in range(img_output.size[0]):
      for j in range(img_output.size[1]):
         r, g, b = img_input.getpixel((img_input.size[0]-i-1, img_input.size[1]-j-1))
         # letakan gambar ke-2 di bagian kanan bawah
         if i<img_input2.size[0] and j>=img_input2.size[1]:
            # lakukan flipping horizontal pada gambar ke-2
            r2, g2, b2 = img_input2.getpixel((i, img_input2.size[1]-j-1))
            # lakukan blending dengan rumus (r1+r2)/2 dan (g1+g2)/2 dan (b1+b2)/2 dan brightness
            pixels[i,j] = ((int((r+r2)/2)+brigtness), int(((g+g2)/2)+brigtness), int(((b+b2)/2)+brigtness))
         else:
            pixels[i,j] = (r+brigtness, g+brigtness, b+brigtness)
         
   if coldepth==1:
      img_output = img_output.convert("1")
   elif coldepth==8:
      img_output = img_output.convert("L")
   else:
      img_output = img_output.convert("RGB")

   return img_output

# fungsi gambar negatif berbentuk setengah belah ketupat pada bagian kanan gambar
def ImgNegatifTriangle(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i < img_output.size[0]/2 and j < img_output.size[1]/2:
               if i <= j:
                   pixels[i, j] = (255-r, 255-g, 255-b)
               else:
                   pixels[i, j] = (r, g, b)
           if i >= img_output.size[0]/2 and j < img_output.size[1]/2:
               if i-img_output.size[0]/2+j < img_output.size[1]/2:
                   pixels[i, j] = (r, g, b)
               else:
                   pixels[i, j] = (255-r, 255-g, 255-b)
           if i < img_output.size[0]/2 and j >= img_output.size[1]/2:
               if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
                   pixels[i, j] = (255-r, 255-g, 255-b)
               else:
                   pixels[i, j] = (r, g, b)
           if i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
               if i >= j:
                   pixels[i, j] = (255-r, 255-g, 255-b)
               else:
                   pixels[i, j] = (r, g, b)

   if coldepth == 1:
       img_output = img_output.convert("1")
   elif coldepth == 8:
       img_output = img_output.convert("L")
   else:
       img_output = img_output.convert("RGB")

   return img_output


#fungsi mengatur gambar di tengah berbentuk lingkaran menjadi negatif dan belah ketupat menjadi gambar asli
def ImgNegativeCircleDiamond(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if abs(i-img_output.size[0]/2)+abs(j-img_output.size[1]/2) < img_output.size[0]/2:
               pixels[i, j] = (r, g, b)
           elif (i-img_input.size[0]//2)**2+(j-img_input.size[1]//2)**2<img_input.size[0]**2//4:
               pixels[i,j] = (255-r, 255-g, 255-b)
           else:
               pixels[i,j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#bonus
def ImgNegativeCircleDiamondTriangle(img_input,coldepth):
   #solusi 1
   #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)
   #solusi 2
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           #fungsi membuat triangle negatif dan jika terkena lingkaran maka akan menjadi gambar asli dan jika terkena diamond maka akan menjadi negatif dan jika lingkaran terkena diamond maka akan menjadi gambar asli dan jika diamond terkena triangle maka akan menjadi negatif
           if abs(i-img_output.size[0]/2)+abs(j-img_output.size[1]/2) < img_output.size[0]/2:
            #fungsi membuat diamond negatif 
               if i < img_output.size[0]/2 and j < img_output.size[1]/2:
                   if i <= j:
                       pixels[i, j] = (255-r, 255-g, 255-b)
                   else:
                       pixels[i, j] = (r, g, b)
               if i >= img_output.size[0]/2 and j < img_output.size[1]/2:
                   if i-img_output.size[0]/2+j < img_output.size[1]/2:
                       pixels[i, j] = (r, g, b)
                   else:
                       pixels[i, j] = (255-r, 255-g, 255-b)
               if i < img_output.size[0]/2 and j >= img_output.size[1]/2:
                   if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
                       pixels[i, j] = (255-r, 255-g, 255-b)
                   else:
                       pixels[i, j] = (r, g, b)
               if i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
                   if i >= j:
                       pixels[i, j] = (255-r, 255-g, 255-b)
                   else:
                       pixels[i, j] = (r, g, b)
           elif (i-img_input.size[0]//2)**2+(j-img_input.size[1]//2)**2<img_input.size[0]**2//4:
             #fungsi membuat lingkaran negatif dan jika terkena triangle maka akan menjadi gambar asli
               if abs(i-img_output.size[0]/2)+abs(j-img_output.size[1]/2) < img_output.size[0]/2:
                     pixels[i, j] = (r, g, b)

               elif i < img_output.size[0]/2 and j < img_output.size[1]/2:
                     if i <= j:
                        pixels[i, j] = (r, g, b)
                     else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
               elif i >= img_output.size[0]/2 and j < img_output.size[1]/2:
                     if i-img_output.size[0]/2+j < img_output.size[1]/2:
                        pixels[i, j] = (255-r, 255-g, 255-b)
                     else:
                        pixels[i, j] = (r, g, b)
               elif i < img_output.size[0]/2 and j >= img_output.size[1]/2:
                     if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
                        pixels[i, j] = (r, g, b)
                     else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
               elif i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
                     if i >= j:
                        pixels[i, j] = (r, g, b)
                     else:
                        pixels[i, j] = (255-r, 255-g, 255-b)
           else:
             pixels[i,j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#median filter
def ImgMedianFilter(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = sorted([r1, r2, r3, r4, r5, r6, r7, r8, r9])[4]
               g = sorted([g1, g2, g3, g4, g5, g6, g7, g8, g9])[4]
               b = sorted([b1, b2, b3, b4, b5, b6, b7, b8, b9])[4]
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#mean filter
def ImgMeanFilter(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               #urut dan ambil nilai rata-rata
               r_pixel = sorted([r1, r2, r3, r4, r5, r6, r7, r8, r9])
               g_pixel = sorted([g1, g2, g3, g4, g5, g6, g7, g8, g9])
               b_pixel = sorted([b1, b2, b3, b4, b5, b6, b7, b8, b9])
               r = sum(r_pixel)//len(r_pixel)
               g = sum(g_pixel)//len(g_pixel)
               b = sum(b_pixel)//len(b_pixel)
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#min filter
def ImgMinFilter(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = sorted([r1, r2, r3, r4, r5, r6, r7, r8, r9])[0]
               g = sorted([g1, g2, g3, g4, g5, g6, g7, g8, g9])[0]
               b = sorted([b1, b2, b3, b4, b5, b6, b7, b8, b9])[0]
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#max filter
def ImgMaxFilter(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = sorted([r1, r2, r3, r4, r5, r6, r7, r8, r9])[8]
               g = sorted([g1, g2, g3, g4, g5, g6, g7, g8, g9])[8]
               b = sorted([b1, b2, b3, b4, b5, b6, b7, b8, b9])[8]
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#convesional linear filter
def ImgLinearFilter(img_input,coldepth):
   koef1 = 2
   koef2 = 4

   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
                r2, g2, b2 = img_input.getpixel((i-1, j-1))  # kiri atas
                r3, g3, b3 = img_input.getpixel((i-1, j))  # kiri
                r4, g4, b4 = img_input.getpixel((i-1, j+1))  # kiri bawah
                r5, g5, b5 = img_input.getpixel((i, j-1))  # tengah atas
                r6, g6, b6 = img_input.getpixel((i, j+1))  # tengah bawah
                r7, g7, b7 = img_input.getpixel((i+1, j-1))  # kanan atas
                r8, g8, b8 = img_input.getpixel((i+1, j))  # kanan
                r9, g9, b9 = img_input.getpixel((i+1, j+1))  # kanan bawah
                r_list = [r*koef2, r2, r3*koef1, r4, r5*koef1, r6*koef1, r7, r8*koef1, r9]
                g_list = [g*koef2, g2, g3*koef1, g4, g5*koef1, g6*koef1, g7, g8*koef1, g9]
                b_list = [b*koef2, b2, b3*koef1, b4, b5*koef1, b6*koef1, b7, b8*koef1, b9]
                r_mean = sum(r_list)//16
                g_mean = sum(g_list)//16  # karena 16 adalah jumlah koefisien
                b_mean = sum(b_list)//16
                pixels[i, j] = (r_mean, g_mean, b_mean)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


def ImgLinearFilter1(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert("RGB")
      input_pixels = img_input.load()

      output_image = Image.new('RGB', (img_input.size[0], img_input.size[1]))
      output_pixels = output_image.load()

   box_kernel = [
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9]]

   kernel = box_kernel
   offset = len(kernel)//2

   for x in range(offset, img_input.size[0] - offset):
       for y in range(offset, img_input.size[1] - offset):
           acc = [0, 0, 0]
           for a in range(len(kernel)):
               for b in range(len(kernel)):
                   xn = x + a - offset
                   yn = y + b - offset
                   pixel = input_pixels[xn, yn]
                   acc[0] += pixel[0] * kernel[a][b]
                   acc[1] += pixel[1] * kernel[a][b]
                   acc[2] += pixel[2] * kernel[a][b]
           output_pixels[x, y] = (int(acc[0]), int(acc[1]), int(acc[2]))

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#Gradient edge detection
def ImgGradientEdgeDetection(img_input,coldepth):
   mask1 = [-1, 1]

   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
   
   pixels = img_output.load()
   for i in range(img_output.size[0]):
         for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
                  pixels[i, j] = (r, g, b)
            else:
                  r, g, b = img_input.getpixel((i, j))
                  r2, g2, b2 = img_input.getpixel((i-1, j))
                  r3, g3, b3 = img_input.getpixel((i+1, j))
                  r_list1 = [r*mask1[0], r2*mask1[1]]
                  g_list1 = [g*mask1[0], g2*mask1[1]]
                  b_list1 = [b*mask1[0], b2*mask1[1]]
                  r_list2 = [r*mask1[1], r3*mask1[0]]
                  g_list2 = [g*mask1[1], g3*mask1[0]]
                  b_list2 = [b*mask1[1], b3*mask1[0]]
                  r_mean1 = sum(r_list1)
                  g_mean1 = sum(g_list1)
                  b_mean1 = sum(b_list1)
                  r_mean2 = sum(r_list2)
                  g_mean2 = sum(g_list2)
                  b_mean2 = sum(b_list2)
                  r_total = abs(r_mean1 + r_mean2)
                  g_total = abs(g_mean1 + g_mean2)
                  b_total = abs(b_mean1 + b_mean2)
                  pixels[i, j] = (r_total, g_total, b_total)
                        
   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output

#Gradient edge detection 2 (dif central)
def ImgGradientEdgeDetection2(img_input,coldepth):
   mask = [-1, 0, 1]

   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
         for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
                  pixels[i, j] = (r, g, b)
            else:
                  r, g, b = img_input.getpixel((i, j))
                  r2, g2, b2 = img_input.getpixel((i-1, j)) #kiri
                  r3, g3, b3 = img_input.getpixel((i+1, j)) #dif central
                  r4, g4, b4 = img_input.getpixel((i, j-1)) #atas
                  r5, g5, b5 = img_input.getpixel((i, j+1)) #bawah
                  r_list1 = [r*mask[0], r2*mask[1], r3*mask[2]]
                  g_list1 = [g*mask[0], g2*mask[1], g3*mask[2]]
                  b_list1 = [b*mask[0], b2*mask[1], b3*mask[2]]
                  r_list2 = [r*mask[0], r4*mask[1], r5*mask[2]]
                  g_list2 = [g*mask[0], g4*mask[1], g5*mask[2]]
                  b_list2 = [b*mask[0], b4*mask[1], b5*mask[2]]
                  r_mean1 = sum(r_list1)
                  g_mean1 = sum(g_list1)
                  b_mean1 = sum(b_list1)
                  r_mean2 = sum(r_list2)
                  g_mean2 = sum(g_list2)
                  b_mean2 = sum(b_list2)
                  r_total = abs(r_mean1 + r_mean2)
                  g_total = abs(g_mean1 + g_mean2)
                  b_total = abs(b_mean1 + b_mean2)
                  pixels[i, j] = (r_total, g_total, b_total)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#sharpening spatial filter with mask 3x3 (laplacian)
def ImgSharpeningFilter(img_input,coldepth):
   mask = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
   
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
         for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
                  pixels[i, j] = (r, g, b)
            else:
                  r2, g2, b2 = img_input.getpixel((i-1, j-1))
                  r3, g3, b3 = img_input.getpixel((i-1, j))
                  r4, g4, b4 = img_input.getpixel((i-1, j+1))
                  r5, g5, b5 = img_input.getpixel((i, j-1))
                  r6, g6, b6 = img_input.getpixel((i, j+1))
                  r7, g7, b7 = img_input.getpixel((i+1, j-1))
                  r8, g8, b8 = img_input.getpixel((i+1, j))
                  r9, g9, b9 = img_input.getpixel((i+1, j+1))
                  r_list = [r*mask[0][0], r2*mask[0][1], r3*mask[0][2], r4*mask[1][0], r5*mask[1][1], r6*mask[1][2], r7*mask[2][0], r8*mask[2][1], r9*mask[2][2]]
                  g_list = [g*mask[0][0], g2*mask[0][1], g3*mask[0][2], g4*mask[1][0], g5*mask[1][1], g6*mask[1][2], g7*mask[2][0], g8*mask[2][1], g9*mask[2][2]]
                  b_list = [b*mask[0][0], b2*mask[0][1], b3*mask[0][2], b4*mask[1][0], b5*mask[1][1], b6*mask[1][2], b7*mask[2][0], b8*mask[2][1], b9*mask[2][2]]
                  r_mean = sum(r_list)
                  g_mean = sum(g_list)
                  b_mean = sum(b_list)
                  
                  #treshold
                  if r_mean < 0:
                        r_mean = 0
                  elif r_mean > 255:
                        r_mean = 255
                  if g_mean < 0:
                        g_mean = 0
                  elif g_mean > 255:
                        g_mean = 255
                  if b_mean < 0:
                        b_mean = 0
                  elif b_mean > 255:
                        b_mean = 255
                  pixels[i, j] = (r_mean, g_mean, b_mean)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#low pass filter
def ImgLowPassFilter(img_input,coldepth):
   mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = ((r1*mask[0][0]) + (r2*mask[0][1]) + (r3*mask[0][2]) + (r4*mask[1][0]) + (r5*mask[1][2]) + (r6*mask[2][0]) + (r7*mask[2][1]) + (r8*mask[2][2]) + (r9*mask[1][1]))//(sum(sum(mask)))
               g = ((g1*mask[0][0]) + (g2*mask[0][1]) + (g3*mask[0][2]) + (g4*mask[1][0]) + (g5*mask[1][2]) + (g6*mask[2][0]) + (g7*mask[2][1]) + (g8*mask[2][2]) + (g9*mask[1][1]))//(sum(sum(mask)))
               b = ((b1*mask[0][0]) + (b2*mask[0][1]) + (b3*mask[0][2]) + (b4*mask[1][0]) + (b5*mask[1][2]) + (b6*mask[2][0]) + (b7*mask[2][1]) + (b8*mask[2][2]) + (b9*mask[1][1]))//(sum(sum(mask)))
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#high pass filter
def ImgHighPassFilter(img_input,coldepth):
   mask = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = ((r1*mask[0][0]) + (r2*mask[0][1]) + (r3*mask[0][2]) + (r4*mask[1][0]) + (r5*mask[1][2]) + (r6*mask[2][0]) + (r7*mask[2][1]) + (r8*mask[2][2]) + (r9*mask[1][1]))//(sum(sum(mask)))
               g = ((g1*mask[0][0]) + (g2*mask[0][1]) + (g3*mask[0][2]) + (g4*mask[1][0]) + (g5*mask[1][2]) + (g6*mask[2][0]) + (g7*mask[2][1]) + (g8*mask[2][2]) + (g9*mask[1][1]))//(sum(sum(mask)))
               b = ((b1*mask[0][0]) + (b2*mask[0][1]) + (b3*mask[0][2]) + (b4*mask[1][0]) + (b5*mask[1][2]) + (b6*mask[2][0]) + (b7*mask[2][1]) + (b8*mask[2][2]) + (b9*mask[1][1]))//(sum(sum(mask)))
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#edge detection
def ImgEdgeDetection(img_input,coldepth):
   mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   for i in range(img_output.size[0]):
       for j in range(img_output.size[1]):
           r, g, b = img_input.getpixel((i, j))
           if i == 0 or i == img_output.size[0]-1 or j == 0 or j == img_output.size[1]-1:
               pixels[i, j] = (r, g, b)
           else:
               r1, g1, b1 = img_input.getpixel((i-1, j-1))
               r2, g2, b2 = img_input.getpixel((i, j-1))
               r3, g3, b3 = img_input.getpixel((i+1, j-1))
               r4, g4, b4 = img_input.getpixel((i-1, j))
               r5, g5, b5 = img_input.getpixel((i+1, j))
               r6, g6, b6 = img_input.getpixel((i-1, j+1))
               r7, g7, b7 = img_input.getpixel((i, j+1))
               r8, g8, b8 = img_input.getpixel((i+1, j+1))
               r9, g9, b9 = img_input.getpixel((i, j))
               r = ((r1*mask[0][0]) + (r2*mask[0][1]) + (r3*mask[0][2]) + (r4*mask[1][0]) + (r5*mask[1][2]) + (r6*mask[2][0]) + (r7*mask[2][1]) + (r8*mask[2][2]) + (r9*mask[1][1]))//(sum(sum(mask)))
               g = ((g1*mask[0][0]) + (g2*mask[0][1]) + (g3*mask[0][2]) + (g4*mask[1][0]) + (g5*mask[1][2]) + (g6*mask[2][0]) + (g7*mask[2][1]) + (g8*mask[2][2]) + (g9*mask[1][1]))//(sum(sum(mask)))
               b = ((b1*mask[0][0]) + (b2*mask[0][1]) + (b3*mask[0][2]) + (b4*mask[1][0]) + (b5*mask[1][2]) + (b6*mask[2][0]) + (b7*mask[2][1]) + (b8*mask[2][2]) + (b9*mask[1][1]))//(sum(sum(mask)))
               
               if r<0:
                  r=0
               if g<0:
                  g=0
               if b<0:
                  b=0
               if r>255:
                  r=255
               if g>255:
                  g=255
               if b>255:
                  b=255
               pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#roberts cross
def ImgRobertsEdgeDetection(img_input,coldepth):
   mask = [[1, 0], [0, -1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   pixels_x = img_output.load()
   pixels_y = img_output.load()

   mask = [1, -1]
   # mask2 = [-1, 1]

   for i in range(img_input.size[0]-1):
       for j in range(img_input.size[1]-1):
           r, g, b = img_input.getpixel((i, j))
           r2, g2, b2 = img_input.getpixel((i+1, j))  # kanan
           r3, g3, b3 = img_input.getpixel((i, j+1))  # bawah
           r4, g4, b4 = img_input.getpixel((i+1, j+1))  # kanan bawah

           # print(r2)

           r_sum_x = (r*mask[0])+(r4*mask[1])
           g_sum_x = (g*mask[0])+(g4*mask[1])
           b_sum_x = (b*mask[0])+(b4*mask[1])
           pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

           r_sum_y = (r2*mask[0])+(r3*mask[1])
           g_sum_y = (g2*mask[0])+(g3*mask[1])
           b_sum_y = (b2*mask[0])+(b3*mask[1])
           pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

           r_sum_xy = (abs(r_sum_x))+(abs(r_sum_y))
           g_sum_xy = (abs(g_sum_x))+(abs(g_sum_y))
           b_sum_xy = (abs(b_sum_x))+(abs(b_sum_y))
           pixels[i, j] = (r_sum_xy, g_sum_xy, b_sum_xy)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#prewitt edge detection
def ImgPrewittEdgeDetection(img_input,coldepth):
   mask = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
   mask1 = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB') 

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
   
   pixels = img_output.load()
   pixels_x = img_output.load()
   pixels_y = img_output.load()

   for i in range(1, img_input.size[0]-1):
         for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r1, g1, b1 = img_input.getpixel((i-1, j-1))
            r2, g2, b2 = img_input.getpixel((i, j-1))
            r3, g3, b3 = img_input.getpixel((i+1, j-1))
            r4, g4, b4 = img_input.getpixel((i-1, j))
            r5, g5, b5 = img_input.getpixel((i+1, j))
            r6, g6, b6 = img_input.getpixel((i-1, j+1))
            r7, g7, b7 = img_input.getpixel((i, j+1))
            r8, g8, b8 = img_input.getpixel((i+1, j+1))
            r9, g9, b9 = img_input.getpixel((i, j))
   
            r_sum_x = (r1*mask[0][0]) + (r2*mask[0][1]) + (r3*mask[0][2]) + (r4*mask[1][0]) + (r5*mask[1][2]) + (r6*mask[2][0]) + (r7*mask[2][1]) + (r8*mask[2][2]) + (r9*mask[1][1])
            g_sum_x = (g1*mask[0][0]) + (g2*mask[0][1]) + (g3*mask[0][2]) + (g4*mask[1][0]) + (g5*mask[1][2]) + (g6*mask[2][0]) + (g7*mask[2][1]) + (g8*mask[2][2]) + (g9*mask[1][1])
            b_sum_x = (b1*mask[0][0]) + (b2*mask[0][1]) + (b3*mask[0][2]) + (b4*mask[1][0]) + (b5*mask[1][2]) + (b6*mask[2][0]) + (b7*mask[2][1]) + (b8*mask[2][2]) + (b9*mask[1][1])
            pixels_x[i, j] = (r_sum_x, g_sum_x, b_sum_x)

            r_sum_y = (r1*mask1[0][0]) + (r2*mask1[0][1]) + (r3*mask1[0][2]) + (r4*mask1[1][0]) + (r5*mask1[1][2]) + (r6*mask1[2][0]) + (r7*mask1[2][1]) + (r8*mask1[2][2]) + (r9*mask1[1][1])
            g_sum_y = (g1*mask1[0][0]) + (g2*mask1[0][1]) + (g3*mask1[0][2]) + (g4*mask1[1][0]) + (g5*mask1[1][2]) + (g6*mask1[2][0]) + (g7*mask1[2][1]) + (g8*mask1[2][2]) + (g9*mask1[1][1])
            b_sum_y = (b1*mask1[0][0]) + (b2*mask1[0][1]) + (b3*mask1[0][2]) + (b4*mask1[1][0]) + (b5*mask1[1][2]) + (b6*mask1[2][0]) + (b7*mask1[2][1]) + (b8*mask1[2][2]) + (b9*mask1[1][1])
            pixels_y[i, j] = (r_sum_y, g_sum_y, b_sum_y)

            r_mean_xy = ((abs(r_sum_x))+(abs(r_sum_y)))//2
            g_mean_xy = ((abs(g_sum_x))+(abs(g_sum_y)))//2
            b_mean_xy = ((abs(b_sum_x))+(abs(b_sum_y)))//2
            pixels[i, j] = (r_mean_xy, g_mean_xy, b_mean_xy)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#sobel edge detection
def ImgSobelEdgeDetection(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   pixels_x = img_output.load()
   pixels_y = img_output.load()

   mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
   mask2 = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

   for i in range(img_input.size[0]-2):
         for j in range(img_input.size[1]-2):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i+1, j))
            r3, g3, b3 = img_input.getpixel((i+2, j))
            r4, g4, b4 = img_input.getpixel((i, j+1))
            r5, g5, b5 = img_input.getpixel((i+1, j+1))
            r6, g6, b6 = img_input.getpixel((i+2, j+1))
            r7, g7, b7 = img_input.getpixel((i, j+2))
            r8, g8, b8 = img_input.getpixel((i+1, j+2))
            r9, g9, b9 = img_input.getpixel((i+2, j+2))

            r_sum_x = (r*mask[0][0])+(r2*mask[0][1])+(r3*mask[0][2])+(r4*mask[1][0])+(r5*mask[1][1])+(r6*mask[1][2])+(r7*mask[2][0])+(r8*mask[2][1])+(r9*mask[2][2])
            g_sum_x = (g*mask[0][0])+(g2*mask[0][1])+(g3*mask[0][2])+(g4*mask[1][0])+(g5*mask[1][1])+(g6*mask[1][2])+(g7*mask[2][0])+(g8*mask[2][1])+(g9*mask[2][2])
            b_sum_x = (b*mask[0][0])+(b2*mask[0][1])+(b3*mask[0][2])+(b4*mask[1][0])+(b5*mask[1][1])+(b6*mask[1][2])+(b7*mask[2][0])+(b8*mask[2][1])+(b9*mask[2][2])
            
            r_sum_y = (r*mask2[0][0])+(r2*mask2[0][1])+(r3*mask2[0][2])+(r4*mask2[1][0])+(r5*mask2[1][1])+(r6*mask2[1][2])+(r7*mask2[2][0])+(r8*mask2[2][1])+(r9*mask2[2][2])
            g_sum_y = (g*mask2[0][0])+(g2*mask2[0][1])+(g3*mask2[0][2])+(g4*mask2[1][0])+(g5*mask2[1][1])+(g6*mask2[1][2])+(g7*mask2[2][0])+(g8*mask2[2][1])+(g9*mask2[2][2])
            b_sum_y = (b*mask2[0][0])+(b2*mask2[0][1])+(b3*mask2[0][2])+(b4*mask2[1][0])+(b5*mask2[1][1])+(b6*mask2[1][2])+(b7*mask2[2][0])+(b8*mask2[2][1])+(b9*mask2[2][2])

            r_mean = ((abs(r_sum_x))+(abs(r_sum_y)))//2
            g_mean = ((abs(g_sum_x))+(abs(g_sum_y)))//2
            b_mean = ((abs(b_sum_x))+(abs(b_sum_y)))//2

            pixels_x[i+1, j+1] = (r_mean, g_mean, b_mean)
   

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#laplacian edge detection
def ImgLaplacianEdgeDetection(img_input,coldepth):
   mask = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
         pixels[i,j] = (0,0,0)

   for i in range(1,img_input.size[0]-1):
      for j in range(1,img_input.size[1]-1):
         r_sum = 0
         g_sum = 0
         b_sum = 0
         for a in range(3):
            for b in range(3):
               xn = i + a - 1
               yn = j + b - 1
               pixel = input_pixels[xn, yn]
               r_sum += pixel[0] * mask[a][b]
               g_sum += pixel[1] * mask[a][b]
               b_sum += pixel[2] * mask[a][b]

         pixels[i,j] = (r_sum,g_sum,b_sum)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#compass edge detection (north-west)
def ImgCompassEdgeDetection(img_input,coldepth):
   mask = [[-1, -1, 1], [-1, -2, 1], [1, 1, 1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
         pixels[i,j] = (0,0,0)

   for i in range(1,img_input.size[0]-1):
      for j in range(1,img_input.size[1]-1):
         r_sum = 0
         g_sum = 0
         b_sum = 0
         for a in range(3):
            for b in range(3):
               xn = i + a - 1
               yn = j + b - 1
               pixel = input_pixels[xn, yn]
               r_sum += pixel[0] * mask[a][b]
               g_sum += pixel[1] * mask[a][b]
               b_sum += pixel[2] * mask[a][b]

         pixels[i,j] = (r_sum,g_sum,b_sum)
   

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#canny edge detection
def ImgCannyEdgeDetection(img_input,coldepth):
   mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')
   
   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
         pixels[i,j] = (0,0,0)

   for i in range(1,img_input.size[0]-1):
      for j in range(1,img_input.size[1]-1):
         r_sum = 0
         g_sum = 0
         b_sum = 0
         for a in range(3):
            for b in range(3):
               xn = i + a - 1
               yn = j + b - 1
               pixel = input_pixels[xn, yn]
               r_sum += pixel[0] * mask[a][b]
               g_sum += pixel[1] * mask[a][b]
               b_sum += pixel[2] * mask[a][b]

         if r_sum<0:
            r_sum=0
         if g_sum<0:
            g_sum=0
         if b_sum<0:
            b_sum=0
         if r_sum>255:
            r_sum=255
         if g_sum>255:
            g_sum=255
         if b_sum>255:
            b_sum=255

         pixels[i,j] = (r_sum,g_sum,b_sum)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#noise gaussian filter
def ImgNoiseGaussianFilter(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   #make a noise with gaussian distribution
   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
        r, g, b = input_pixels[i, j]
        r, g, b = int(r), int(g), int(b)
        r = r + int(random.gauss(0, 50))
        g = g + int(random.gauss(0, 50))
        b = b + int(random.gauss(0, 50))
        if r < 0:
         r = 0
        if g < 0:
         g = 0
        if b < 0:
         b = 0
        if r > 255:
         r = 255
        if g > 255:
         g = 255
        if b > 255:
         b = 255
        pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#salt noise
def ImgSaltNoise(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   #make a salt noise
   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
        r, g, b = input_pixels[i, j]
        r, g, b = int(r), int(g), int(b)
        if random.randint(0, 100) < 10:
         r = 255
         g = 255
         b = 255
        pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#paper noise
def ImgPaperNoise(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   #make a paper noise
   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
        r, g, b = input_pixels[i, j]
        r, g, b = int(r), int(g), int(b)
        if random.randint(0, 100) < 10:
         r = 0
         g = 0
         b = 0
        pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output


#salt and paper noise
def ImgSaltPaperNoise(img_input,coldepth):
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   #make a salt and paper noise
   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
        r, g, b = input_pixels[i, j]
        r, g, b = int(r), int(g), int(b)
        if random.randint(0, 100) < 10:
         r = 255
         g = 255
         b = 255
        if random.randint(0, 100) < 10:
         r = 0
         g = 0
         b = 0
        pixels[i, j] = (r, g, b)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output

#gaussian filter
def ImgGaussianFilter(img_input,coldepth):
   mask = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
   if coldepth!=24:
      img_input = img_input.convert('RGB')

   img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

   pixels = img_output.load()
   input_pixels = img_input.load()

   for i in range(img_input.size[0]):
      for j in range(img_input.size[1]):
         pixels[i,j] = (0,0,0)

   for i in range(1,img_input.size[0]-1):
      for j in range(1,img_input.size[1]-1):
         r_sum = 0
         g_sum = 0
         b_sum = 0
         for a in range(3):
            for b in range(3):
               xn = i + a - 1
               yn = j + b - 1
               pixel = input_pixels[xn, yn]
               r_sum += pixel[0] * mask[a][b]
               g_sum += pixel[1] * mask[a][b]
               b_sum += pixel[2] * mask[a][b]

         r_sum = int(r_sum//16)
         g_sum = int(g_sum//16)
         b_sum = int(b_sum//16)

         pixels[i,j] = (r_sum,g_sum,b_sum)

   if coldepth == 1:
         img_output = img_output.convert("1")
   elif coldepth == 8:
         img_output = img_output.convert("L")
   else:
         img_output = img_output.convert("RGB")

   return img_output