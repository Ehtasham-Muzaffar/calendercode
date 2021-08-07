from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    month=month.capitalize()
    month_name=list(calendar.month_name).index(month)
    month_name=int(month_name)
    cal=HTMLCalendar().formatmonth(
        year,month_name
    )  
    now=datetime.now()
    year=now.year
    times=now.strftime('%I:%M:%S:%p')
    return render(request, 'events/home.html', {
        'name':"shami",
        'year':year,
        'month':month,
        'month_number':month_name,
        'cal':cal,
        'time':times,
        'year':year


    })
    