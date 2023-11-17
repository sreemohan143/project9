from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='inda win the world cup'
    d={'assumssion':data}
    return render(request,'data_render.html',context=d)