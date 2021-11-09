from .models import *


def categories_info(request):
    all_categories = Categories.objects.all()
    return locals()