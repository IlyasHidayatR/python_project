from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = Image.open('lab/ImageDetection/Image2.jpg') # Ini adalah baris kode yang membuka file gambar yang ditentukan oleh path file tersebut dan menugaskan objek Image yang dihasilkan ke variabel image.

# Image resize to 50% of original size
image = image.resize((int(image.width * 0.5), int(image.height * 0.5))) # Ini adalah baris kode yang mengubah ukuran gambar menjadi 50% dari ukuran aslinya.

# Detect fruits and vegetables in the image with color space and color segmentation and count them
def detect_fruits_and_vegetables(image):
    # Convert the image to RGB color space
    image = image.convert('RGB') # Ini adalah baris kode yang mengubah gambar dari mode warna yang sebelumnya adalah mode warna CMYK menjadi mode warna RGB.

    # Define colors to detect for each fruit and vegetable in RGB color space
    color_fruits_and_vegetables = { # Ini adalah baris kode yang mendefinisikan warna yang akan dideteksi untuk setiap buah dan sayuran dalam ruang warna RGB.
        # Fruits
        'Apple': (255, 0, 0),
        'Blueberry': (0, 0, 255),
        'Orange': (255, 165, 0),
        'Strawberry': (255, 0, 0),
        'Green Apple': (0, 255, 0),
        'Grapes': (255, 0, 0),
        # Vegetables
        'Carrot': (255, 165, 0),
        'Cucumber': (0, 255, 0),
        'Lettuce': (0, 255, 0),
        'Onion': (255, 0, 0),
        'Tomato': (255, 0, 0)
    }

    # Convert the image to NumPy array
    image = np.array(image) # Ini adalah baris kode yang mengubah objek gambar menjadi array NumPy.

    # Count the fruits and vegetables with morfology operation and show the result location in image with rectangle
    fruits_and_vegetables_count = {} # Ini adalah baris kode yang mendefinisikan variabel fruits_and_vegetables_count sebagai dictionary kosong.
    for color_to_detect in color_fruits_and_vegetables: # Ini adalah baris kode yang melakukan iterasi untuk setiap warna yang akan dideteksi dalam dictionary color_fruits_and_vegetables.
        # Define the color boundaries in RGB color space for the color to detect
        lower_color = np.array(color_fruits_and_vegetables[color_to_detect]) - 30 # Ini adalah baris kode yang mendefinisikan batas warna bawah dalam ruang warna RGB untuk warna yang akan dideteksi.
        upper_color = np.array(color_fruits_and_vegetables[color_to_detect]) + 30 # Ini adalah baris kode yang mendefinisikan batas warna atas dalam ruang warna RGB untuk warna yang akan dideteksi.

        # Create a mask for the colors
        mask = cv2.inRange(image, lower_color, upper_color) # ni adalah baris kode yang membuat sebuah masker untuk warna yang akan dideteksi. Masker ini akan menghasilkan nilai 1 di semua pixel yang memiliki nilai warna di antara batas atas dan bawah yang ditentukan.

        # Mask the image to only select the colors to detect
        segmented_image = cv2.bitwise_and(image, image, mask=mask) # Ini adalah baris kode yang menggunakan masker untuk memilih hanya pixel yang memiliki nilai warna yang sesuai dengan masker. Hasilnya adalah sebuah gambar baru yang hanya terdiri dari warna yang akan dideteksi.

        # Apply a threshold to the image (10 for the threshold value and 255 for the maximum value)
        _, segmented_image = cv2.threshold(segmented_image, 10, 255, cv2.THRESH_BINARY) # Ini adalah baris kode yang menerapkan sebuah ambang pada gambar yang telah dipilih dengan masker. Semua pixel dengan nilai lebih dari ambang akan diubah menjadi nilai maksimum (255), sementara pixel dengan nilai dibawah ambang akan diubah menjadi nilai minimum (0).

        # Apply a morphological operation to the image with a 5x5 kernel and Close operation
        kernel = np.ones((5, 5), np.uint8)
        segmented_image = cv2.morphologyEx(segmented_image, cv2.MORPH_CLOSE, kernel) #Ini adalah baris kode yang menerapkan operasi morfologi pada gambar yang telah diberikan ambang. Operasi morfologi ini digunakan untuk menyatukan objek kecil menjadi satu dan menghilangkan objek kecil yang tidak diinginkan.

        # Convert the image to grayscale color space
        segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY) # Ini adalah baris kode yang mengubah gambar dari spasi warna RGB menjadi skala abu-abu. Spasi warna grayscale hanya memiliki satu kanal yang merepresentasikan nilai kecerahan pixel, sementara spasi warna RGB memiliki tiga kanal yang merepresentasikan nilai merah, hijau, dan biru pada pixel.

        # Find the contours of the image with OpenCV
        contours, _ = cv2.findContours(segmented_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Ini adalah baris kode yang mencari batas-batas objek di dalam gambar. Batas-batas objek ini disebut dengan contour. Fungsi findContours() akan mengembalikan list dari contour dan hierarki contour dari objek di dalam gambar.

        # Count the fruits and vegetables
        fruits_and_vegetables_count[color_to_detect] = len(contours) #Ini adalah baris kode yang menghitung jumlah objek yang terdeteksi dengan mengambil panjang list contour. Jumlah objek ini kemudian ditambahkan ke dictionary fruits_and_vegetables_count dengan nama objek sebagai key.

        # Draw the rectangle around the fruits and vegetables
        for contour in contours: # Ini adalah baris kode yang melakukan iterasi untuk setiap contour yang terdeteksi.
            x, y, w, h = cv2.boundingRect(contour) # Ini adalah baris kode yang mendapatkan nilai x, y, w, dan h dari setiap contour. Nilai x dan y adalah titik koordinat kiri atas dari kotak persegi yang mengelilingi objek. Nilai w dan h adalah lebar dan tinggi dari kotak persegi yang mengelilingi objek.
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) # Ini adalah baris kode yang menggambar kotak persegi pada gambar yang mengelilingi objek yang terdeteksi.
            cv2.putText(image, color_to_detect, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # Ini adalah baris kode yang menulis nama objek di dalam kotak persegi yang mengelilingi objek.

        #Ini adalah baris kode yang menggambar sebuah kotak sekitar setiap objek yang terdeteksi. Fungsi boundingRect() akan mengembalikan koordinat titik kiri atas dan lebar dan tinggi dari kotak yang dapat mengelilingi objek. Fungsi rectangle() kemudian digunakan untuk menggambar kotak, sementara fungsi putText() digunakan untuk menuliskan nama objek di atas kotak tersebut.

    # Show the image with the rectangle around the fruits and vegetables 
    plt.title('Fruits and Vegetables Detection') # Ini adalah baris kode yang menampilkan gambar dengan kotak yang telah digambar sekitar objek yang terdeteksi. Fungsi title() digunakan untuk memberikan judul pada plot, fungsi imshow() digunakan untuk menampilkan gambar, dan fungsi show() digunakan untuk menampilkan plot.
    plt.imshow(image)
    plt.show()

    return fruits_and_vegetables_count # Ini adalah baris kode yang mengembalikan dictionary fruits_and_vegetables_count yang berisi nama objek dan jumlah objek yang terdeteksi.
    
# Detect fruits and vegetables in the image
fruits_and_vegetables_count = detect_fruits_and_vegetables(image) # Ini adalah baris kode yang memanggil fungsi detect_fruits_and_vegetables() untuk mendeteksi buah dan sayur di dalam gambar.

# Print the fruits and vegetables count
print(fruits_and_vegetables_count)

# Show the results for the fruits and vegetables count in a bar chart
plt.bar(fruits_and_vegetables_count.keys(), fruits_and_vegetables_count.values()) # Ini adalah baris kode yang menampilkan hasil dari fungsi detect_fruits_and_vegetables() dalam bentuk bar chart. Fungsi bar() digunakan untuk membuat bar chart, fungsi keys() digunakan untuk mendapatkan nama objek dari dictionary fruits_and_vegetables_count, dan fungsi values() digunakan untuk mendapatkan jumlah objek dari dictionary fruits_and_vegetables_count.
plt.xticks(rotation=90) # Ini adalah baris kode yang mengatur rotasi label pada sumbu x.
plt.show() # Ini adalah baris kode yang menampilkan plot.
