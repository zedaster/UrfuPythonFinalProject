from django.shortcuts import render

from vacancies.hh_api_worker import HhApiWorker
from vacancies.models import VacanciesPage


def vacancies(request):
    page = VacanciesPage.objects.first()

    vac_list = None
    captcha_link = None
    try:
        vac_list = HhApiWorker().get_vacancies(page.date, page.search_query,
                                               swap_to_workday=True, count=page.count)
    except HhApiWorker.CaptchaException as ex:
        captcha_link = ex.captcha_url

    return render(request, 'vacancies/vacancies.html', {'vacancies': vac_list, 'captcha_link': captcha_link})
