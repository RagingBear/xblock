from django.http import JsonResponse, QueryDict
from django.views import View

from xb_log.models import AccessLog


# Create your views here.

class Access(View):
    def get(self, request, *args, **kwargs):
        """
        get AccessLog data, optional arguments:
        - offset:int
        - limit:int
        :param request:
        :return:
        json response
        (200):
            - offset:int
            - limit:int
            - total:int
            - rows:list()
        (400):
            message about error
        """
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 10))
        count = AccessLog.objects.count()
        if offset >= count:
            return JsonResponse(data={'status': 'error', 'message': 'offset too large'}, status=400)

        rows = list()
        data = AccessLog.objects.all().order_by('-time')[offset:offset + limit if offset + limit <= count else count]
        for item in data.iterator():
            rows.append({
                'id': item.id,
                'ip': item.ip,
                'path': item.path,
                'referer': item.referer,
                'time': item.time,
            })
        return JsonResponse({
            'offset': offset,
            'limit': limit,
            'total': count,
            'rows': rows,
        })

    def delete(self, request, *args, **kwargs):
        """
        delete access log depends on id
        - id:int
        :param request:
        :return:
        (200):
            message about ok
        (400):
            message about id error
        """
        req_data = QueryDict(request.body)
        id = req_data.get('id', None)
        if id is None:
            return JsonResponse(data={'status': 'error', 'message': 'no id argument'}, status=400)
        data = AccessLog.objects.filter(id=id)
        if data.count() == 0:
            return JsonResponse(data={'status': 'error', 'message': 'id not existed'}, status=400)
        data.delete()
        return JsonResponse({
            'status': 'ok',
        })
