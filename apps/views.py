from django.shortcuts import render
from .forms import MyMessage

from .models import Service,Past_Paper,Register_Book,Book_Category,Testimonial,Teacher
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

import requests
from django.http import HttpResponse




from .forms import MyMessage

def contact(request):
    ujumbe = ""

    if request.method == 'POST':
        form = MyMessage(request.POST)
        if form.is_valid():
            form.save()
            ujumbe = "Hongera! Ujumbe wako umetumwa kikamilifu."
            return redirect('contact')  # Kuzuia double submission
    else:
        form = MyMessage()

    context = {
        'form': form,
        'ujumbe': ujumbe
    }
    return render(request, 'contact.html', context)



# Home Page
def home(request):
    past_papers = Past_Paper.objects.all()[:3]
    teacher = Teacher.objects.all()[:2]
    testimon = Testimonial.objects.all()

    context = {
       'past_papers':past_papers,
       'teacher':teacher,
        'testimon':testimon
    }
 
    return render(request, 'index.html',context)

# Elimu ya Ufahamu
def service(request):
    services = Service.objects.all()
    teacher = Teacher.objects.all()
    
    context = {
        'services':services,
        'teacher':teacher
    }

    return render(request, 'service.html',context)

# Warsha za Kiroho
# def contact(request):
#     return render(request, 'contact.html')

# Ushuhuda wa Wateja
def about(request):
    teacher = Teacher.objects.all()

    context = {
       'teacher':teacher,
    }

    return render(request, 'about.html',context)


def pastpaper(request):
    past_papers = Past_Paper.objects.all()
    return render(request, 'pastpaper.html', {'past_papers': past_papers})

def download_pdf(request, file_id):
    # Construct the Cloudinary URL for the file based on the file_id
    cloudinary_url = f"https://res.cloudinary.com/Ydjzcf2bvp/raw/upload/{file_id}"

    # Fetch the file from Cloudinary
    response = requests.get(cloudinary_url, stream=True)

    if response.status_code == 200:
        # Get the filename from the URL (or use file_id)
        filename = file_id.split("/")[-1]

        # Set the headers to force download
        res = HttpResponse(response.content, content_type='application/pdf')
        res['Content-Disposition'] = f'attachment; filename="{filename}"'

        return res
    else:
        return HttpResponse("File not found", status=404)



def test(request):
    return render(request,'test.html')

def books(request):
    book = Register_Book.objects.all()
    categories = Book_Category.objects.all()
    testimon = Testimonial.objects.all()

    context = {
        'book':book,
        'categories':categories,
        'testimon':testimon
    }
    return render(request,'book.html',context)


from .models import Gallery

def gallery(request):
    # Get all gallery items
    gallery_items = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})