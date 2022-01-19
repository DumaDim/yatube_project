from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Основное меню')

def group_posts(request, slug):
    return HttpResponse(f'Группа постов {slug}')