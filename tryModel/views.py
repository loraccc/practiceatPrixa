from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from xhtml2pdf import pisa  # Import required for PDF generation
import csv
from .forms import UploadFileForm
from .models import people
import csv
from django.shortcuts import render
from .forms import UploadFileForm
from .models import people
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration.html', {'error': 'Passwords do not match'})
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Log in the user
        # authenticated_user = authenticate(request, username=username, password=password)
        login(request, user)
        
        # Redirect to a success page or home page
        return redirect('success')

    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Manually authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #Send mail after Registration of new user 
            subject = 'User Created Successfully'
            message = 'Congratulations! YOUR have logged in.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['carolacharya1@gmail.com']

            send_mail(subject, message, from_email, recipient_list)
            # Redirect to a success page or home page
            return redirect('upload')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')




@login_required(login_url='login/')
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

@login_required
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
# @login_required
def generate_pdf(request):
    template_path = 'pdf_template.html'
    people_data = people.objects.all()

    context = {'people_data': people_data}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="people_data.pdf"'

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


# @csrf_exempt
# def index(request):
#     print('index Called', request.POST)
#     return JsonResponse ({'messaghe':'Carol replied GOODJOB'})

