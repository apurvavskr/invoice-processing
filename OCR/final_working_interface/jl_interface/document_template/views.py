from django.shortcuts import render, HttpResponse
from .forms import ImageUploadForm
from .image_processing import invoice_to_html

def upload_invoice(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            html_output = invoice_to_html(image_file)
            response = HttpResponse(html_output, content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="processed_invoice.html"'
            return response
        else:
            return render(request, 'upload.html', {'form': form})
    else:
        form = ImageUploadForm()
        return render(request, 'upload.html', {'form': form})
