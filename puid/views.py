from django.shortcuts import render, redirect
from django.core.paginator import InvalidPage, EmptyPage #, Paginator
import collections
from .models import Puid
from datetime import datetime
from django.core.paginator import Paginator
from django.views.generic import View


fromDate = ''
toDate = ''
zoneId = ''
number = 0
totalResult = None


def index(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('new_handler')
    #     else:
    #         messages.success(request, ('Ошибка ввода'))
    #         return redirect('')
    #
    # else:
    return render(request, 'puid/index.html')


def about(request):
    global fromDate, toDate, zoneId, number, totalResult
    if request.method == 'POST':
        fromDate = request.POST['fromDate']

        toDate = request.POST['toDate']

        zoneId = request.POST['vehicle_class']  # TODO получить код зоны

        date_obj = datetime.strptime(fromDate, "%Y-%m-%dT%H:%M")
        fromDate = date_obj.strftime("%Y-%m-%d %H:%M:%S")

        date_obj = datetime.strptime(toDate, "%Y-%m-%dT%H:%M")
        toDate = date_obj.strftime("%Y-%m-%d %H:%M:%S")

        totalResult = Puid.objects.filter(vehicle_class__contains=zoneId,
                                          datetime__gte=fromDate,
                                          datetime__lte=toDate).order_by('vehicle_class')
        number = len(totalResult)
        paginator = Paginator(totalResult, 15)
        page_obj = paginator.get_page(1)
        print(page_obj)

        # page_range = 10
        # margin_pages = 2
        # if paginator.num_pages <= page_range:
        #     return range(1, paginator.num_pages + 1)
        # result = []
        # left_side = page_range /2
        # right_side = page_range - left_side
        # if number > paginator.num_pages - page_range / 2:
        #     right_side = paginator.num_pages - number
        #     left_side = page_range - right_side
        # elif number < page_range / 2:
        #     left_side = number
        #     right_side = page_range - left_side
        # for page in range(1, paginator.num_pages + 1):
        #     if page <= margin_pages:
        #         result.append(page)
        #         continue
        #     if page > paginator.num_pages - margin_pages:
        #         result.append(page)
        #         continue
        #     if (page >= number - left_side) and (page <= number + right_side):
        #         result.append(page)
        #         continue
        #     if result[-1]:
        #         result.append(None)

        data = {'all_info': totalResult, 'resul': number, 'page_obj': page_obj}
    elif request.GET.get('page'):
        page_number = request.GET.get('page')
        print(page_number)
        if page_number is None:
            page_number = '1'
        paginator = Paginator(totalResult, 15)
        print(paginator)
        page_obj = paginator.get_page(page_number)
        print(page_obj)

        nums = "a" * page_obj.paginator.num_pages
        print(nums)
        data = {'all_info': totalResult, 'resul': number, 'page_obj': page_obj, 'nums': nums}
    else:
        data = {'all_info': Puid.objects.none()}

    return render(request, 'puid/about.html', data)





