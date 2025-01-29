from django.http import HttpResponse,JsonResponse
def http_test(request):
    return HttpResponse('<h1>salam</h1>')
def jason_test(request):
    return JsonResponse({'name':'omid'})