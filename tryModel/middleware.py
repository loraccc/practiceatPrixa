from django.http import JsonResponse

def set_request_data(get_response):
    print('Set request data Middleware')

    def wrapper(request):
        print(f"Post data={request.POST}")
        data=request.POST.get('number')
        request.POST={'data':data}
        print('Start of setrequest data')
        # print(data)
        response=get_response(request)
        print('end of this data')
        return response
        
    return wrapper

print('####################')

def check_even(get_response):
    ('Print Even Middleware')
    def wrapper(request):
        print('start of check even')
        number=request.POST.get('number')
        if number and int(number) %2:
            return JsonResponse({'status':'fail','message':'Number is not even'}, status=400)
        # else:
        #     return JsonResponse({'status':'failed'})
        response=get_response(request)
        print('end of check even')
        return response
    return wrapper
     
