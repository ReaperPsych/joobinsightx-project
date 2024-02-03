from django.core.exceptions import PermissionDenied




# ACCOUNT_TYPE = [
#     ('1', 'Employee'),
#     ('2', 'Employer')
# ]


def user_is_employee(view_function):
    def wrap(request, *args, **kwargs):
        if request.user.account == '1':
            return view_function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_is_employer(view_function):
    def wrap(request, *args, **kwargs):
        if request.user.account == '2':
            return view_function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


