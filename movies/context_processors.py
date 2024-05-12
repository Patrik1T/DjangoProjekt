from .models import predmet

def genres(request):
    return {'predmet': predmet.objects.all()}