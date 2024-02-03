
class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user_type = request.user.account
        else:
            request.user_type = None
            
        response = self.get_response(request)
        return response
