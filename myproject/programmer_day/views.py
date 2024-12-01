from django.shortcuts import render
from .forms import YearForm

def calculate_programmer_day(year):
    if year < 1918:
        # До 1918 года в России использовался юлианский календарь
        return f"26 сентября {year} (понедельник)" if year % 4 == 0 else f"27 сентября {year} (понедельник)"
    elif year == 1918:
        # В 1918 году был переход на григорианский календарь
        return "26 сентября 1918 (понедельник)"
    else:
        # После 1918 года используется григорианский календарь
        return f"12 сентября {year} (понедельник)" if year % 4 == 0 else f"13 сентября {year} (понедельник)"

def index(request):
    result = ''
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            result = calculate_programmer_day(year)
    else:
        form = YearForm()

    return render(request, 'programmer_day/index.html', {'form': form, 'result': result})