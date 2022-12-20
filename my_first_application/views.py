from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView

from my_first_application.models import OverFirst


class ClassEndpointView(TemplateView):
    template_name = 'first.html'
    http_method_names = [
        "get",
    ]

    def get(self, request, *args, **kwargs):
        return HttpResponse('page 1')


def first(request):
    return render(request, 'first.html')


def one(request):  # request = HTTP packet
    raise Exception
    return HttpResponse('page 1')


def two(request):
    return HttpResponse('page 2')


def three(request):
    return HttpResponse('page 3')


def get_obj_by_id(request, obj_id):
    objs = OverFirst.objects.filter(id=obj_id)
    if objs:
        obj = objs[0]
        return HttpResponse(f'<h1>OBJ:</h1> {obj.__dict__}')
    return HttpResponse('Not found', status=404)