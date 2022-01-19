from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Основное меню')

def group_posts(request):
    return HttpResponse('Группы постов')

def group_posts_1(request, pk):
    return HttpResponse(f'Группа постов номер {pk}')