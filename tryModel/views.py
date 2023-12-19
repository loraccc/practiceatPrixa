from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


import csv
from django.shortcuts import render
from .forms import UploadFileForm
from .models import people

# @csrf_exempt
# def index(request):
#     print('index Called', request.POST)
#     return JsonResponse ({'messaghe':'Carol replied GOODJOB'})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            # Process the uploaded file
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'success.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    for row in reader:
        print(row)  # Add this line to print each row
        people.objects.create(
            id=row['ID'],
            name=row['NAME'],
            age=row['AGE'],
            city=row['CITY']
        )
