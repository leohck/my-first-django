from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'site_teste/post_list.html', {})
