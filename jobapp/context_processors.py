def user_type_processor(request):
    user_type = None
    if request.user.is_authenticated:
        user_type = request.user.account
    return {'user_type': user_type}