from django.shortcuts import render, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Funcs
from django.urls import reverse
import numpy as np
# Create your views here.


def index(request):
    error = ''
    if request.method == 'POST':
        func1 = request.POST['func1']
        func2 = request.POST['func2']
        func3 = request.POST['func3']
        lv = request.POST['lv']
        gv = request.POST['gv']
        p = request.POST['p']
        if int(gv) > int(lv):
            Funcs.objects.update_or_create(id=1, defaults={'func': float(func1)})
            Funcs.objects.update_or_create(id=2, defaults={'func': float(func2)})
            Funcs.objects.update_or_create(id=3, defaults={'func': float(func3)})
            Funcs.objects.update_or_create(id=4, defaults={'func': float(lv)})
            Funcs.objects.update_or_create(id=5, defaults={'func': float(gv)})
            Funcs.objects.update_or_create(id=6, defaults={'func': float(p)})
        else:
            error = 'Неверные данные'
        return HttpResponseRedirect(reverse('main:index'))
    context = {'error': error}
    return render(request, 'main/index.html', context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = []
        chart_data = []
        error = False
        func1 = Funcs.objects.get(id=1).func
        func2 = Funcs.objects.get(id=2).func
        func3 = Funcs.objects.get(id=3).func
        lv = Funcs.objects.get(id=4).func
        gv = Funcs.objects.get(id=5).func
        p = Funcs.objects.get(id=6).func

        def func(x, n):
            match n:
                case 1:
                    return np.sqrt(x)
                case 2:
                    return 1/x
                case 3:
                    return np.exp(x)
        if int(gv) > int(lv):
            try:
                labels = np.arange(lv, gv, p)
                f3 = map(func, labels, [func3 for i in range(len(labels))])
                f2 = map(func, f3, [func2 for i in range(len(labels))])
                chart_data = map(func, f2, [func1 for i in range(len(labels))])
            except Exception:
                error = True
            else:
                labels = np.arange(lv, gv, p)
                f3 = map(func, labels, [func3 for i in range(len(labels))])
                f2 = map(func, f3, [func2 for i in range(len(labels))])
                chart_data = map(func, f2, [func1 for i in range(len(labels))])
        data = {
            "labels": labels,
            "chart_data": chart_data,
            'error': error,
        }
        return Response(data=data)

