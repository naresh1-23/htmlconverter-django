from django.shortcuts import render


def Convert(request):
    if request.method == 'POST':
        text= request.POST['sentence']
        tags = request.POST['tags']
        contents = "<"+tags+">"+text+"</"+tags+">"
        return render(request,'converter/convert.html', {'contents':contents })
    else:
        return render(request, 'converter/convert.html')
# Create your views here.
