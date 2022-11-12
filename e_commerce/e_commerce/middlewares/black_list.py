
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class BlackListMiddleware(MiddlewareMixin):
    BLACK_IP_LIST = [
        '127.0.0.1'
    ]
    
    
    
    def process_request(self,request):
        if request.META.get("REMOTE_ADDR") in self.BLACK_IP_LIST:
            raise PermissionDenied