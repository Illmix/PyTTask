from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from csv import DictReader


def sort_file(file_name, column):
    with open(f'./media/{file_name}', 'r', encoding='utf-8') as f:
        csv_reader = DictReader(f)
        line_count = 0
        persons = {}
        for row in csv_reader:
            if not line_count:
                column_names = list(row.keys())
                line_count += 1
                for name in column_names:
                    persons[name] = []
            for name in column_names:
                persons[name].append(row[name])
    try:
        persons[column].sort()
        return persons[column]
    except KeyError:
        return ['Something has gone wrong. The file cannot be sorted, or you entered the wrong column name']


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        column_name = request.POST['text']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['sorted'] = sort_file(uploaded_file.name, column_name)
    return render(request, 'upload.html', context)

