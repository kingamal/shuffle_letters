from django.shortcuts import render
from .forms import PeselForm
import datetime

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False, None

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (checksum % 10)) % 10

    if int(pesel[-1]) != control_digit:
        return False, None

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 12:
        month -= 20
        year += 2000
    else:
        year += 1900

    try:
        birth_date = datetime.date(year, month, day)
    except ValueError:
        return False, None

    gender = "mężczyzna" if int(pesel[9]) % 2 == 1 else "kobieta"

    return True, (birth_date, gender)

def pesel_view(request):
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            is_valid, info = validate_pesel(pesel)

            if is_valid:
                birth_date, gender = info
                return render(request, 'pesel_result.html', {
                    'is_valid': True,
                    'birth_date': birth_date,
                    'gender': gender,
                })
            else:
                return render(request, 'pesel_result.html', {'is_valid': False})

    else:
        form = PeselForm()

    return render(request, 'pesel_form.html', {'form': form})
