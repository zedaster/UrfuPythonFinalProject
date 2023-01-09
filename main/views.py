from django.shortcuts import render


# Create your views here.
from main.models import HomePage, HomePageImage, DemandPage, GeographyPage, SkillPage
from main.utils.bb_handler import handle_bb_image_links


def home(request):
    page = HomePage.objects.first()
    images = HomePageImage.objects.all()
    image_links = dict(map(lambda i: (i.name, i.image.url), images))
    content = handle_bb_image_links(image_links, page.content)
    return render(request, 'main/home.html', {'content': content})


def demand(request):
    page = DemandPage.objects.first()
    return render(request, 'main/demand.html', {'page': page})


def geography(request):
    page = GeographyPage.objects.first()
    return render(request, 'main/geography.html', {'page': page})


def skills(request):
    page = SkillPage.objects.first()
    return render(request, 'main/skills.html', {'page': page})
