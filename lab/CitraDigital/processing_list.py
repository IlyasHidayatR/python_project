from PIL import Image, ImageOps
import math

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
            r, g, b = img_input.getpixel((j,img_output.size[0]-i-1)) #clockwise rotation (kiri ke kanan)
        else:
            r, g, b = img_input.getpixel((img_input.size[1]-j-1,i)) #counter clockwise rotation (kanan ke kiri)
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