import random
from django.shortcuts import render, redirect
from .forms import UploadFileForm


def shuffle_word(word):
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def process_text(text):
    result = []
    for line in text.splitlines():
        new_line = ' '.join(shuffle_word(word) for word in line.split())
        result.append(new_line)
    return '\n'.join(result)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            text = file.read().decode('utf-8')
            modified_text = process_text(text)
            return render(request, 'result.html', {'modified_text': modified_text})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})