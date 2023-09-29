from django.shortcuts import render

# Create your views here.
def halaman(request):
    nama = "Yashiru"
    return render(request, 'halaman.html', {'nama': nama})