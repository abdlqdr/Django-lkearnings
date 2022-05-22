def my_middleware(get_response):
    print("One time initialization")
    def my_func(request):
        print("code before view")
        response = get_response(request)
        print("code after view")
        return response
    return my_func