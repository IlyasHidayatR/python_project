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
