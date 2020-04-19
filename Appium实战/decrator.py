def authicate(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        from login import checkuser_logged_in
        if checkuser_logged_in(request):
            func(*args, **kwargs)
        else:
            raise Exception('Authentication fail')

    return wrapper
