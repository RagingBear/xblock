from xb_log.models import AccessLog


class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        AccessLog.objects.create(
            ip=x_forwarded_for if x_forwarded_for else request.META.get('REMOTE_ADDR'),
            path=request.path,
            referer=request.headers.get('feferer', ''),
        )

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
