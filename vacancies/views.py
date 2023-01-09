from datetime import datetime

from django.shortcuts import render

from vacancies.hh_api_worker import HhApiWorker


def vacancies(request):
    vac_list = HhApiWorker().get_vacancies(datetime(2022, 12, 11), "NAME:(java NOT qa)", swap_to_workday=True, count=10)
    return render(request, 'vacancies/vacancies.html', {'vacancies': vac_list})
