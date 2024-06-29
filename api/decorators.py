from django.http import JsonResponse

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Login required'}, status=403)
    return wrapper