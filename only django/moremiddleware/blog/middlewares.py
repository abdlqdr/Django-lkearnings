from django.http import HttpResponse

class BortherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Brother One time Initialization")
    
    def __call__(self, request):
        print("Brother before view")
        response = self.get_response(request)
        print("Brother after view")
        return response
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Father One time Initialization")
    
    def __call__(self, request):
        print("Father before view")
        response = self.get_response(request)
        # response = HttpResponse("resopnse from father")
        print("Father after view")
        return response
        
class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Mother One time Initialization")
    
    def __call__(self, request):
        print("Mother before view")
        response = self.get_response(request)
        print("Mother after view")
        return response