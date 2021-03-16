from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import Document
from .forms import DocumentForm

'''def index(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'index.html', context)'''


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            return redirect('index')
    else:
        form = DocumentForm
    media = Document.objects.all()
    context = {'media': media, 'form': form}

    return render(request, 'index.html', context)
