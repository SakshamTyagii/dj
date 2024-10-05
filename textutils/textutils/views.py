from django.http import HttpResponse
from django.shortcuts  import render


def index2(request):
    return render(request, 'index2.html')

def index(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'",<>.\/?@#$%^&*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'removed punctuations' ,'analyzed_text':analyzed}
        djtext = analyzed
        
    if(capitalize == 'on'):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params={'purpose':'changed to uppercase' ,'analyzed_text':analyzed}
        djtext = analyzed
    
    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params={'purpose':'Removed Newlines' ,'analyzed_text':analyzed}
        djtext = analyzed
    
    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params={'purpose':'Removed extraspaces' ,'analyzed_text':analyzed}
        djtext=analyzed 
    
    if(charcount):
        length =(len(djtext.split()))
        analyzed=djtext+"            \n"+ str(length) +" "+ 'words';   
        params={'purpose':'total number of words:' ,'analyzed_text':analyzed}
    return render(request,'index.html', params)
        