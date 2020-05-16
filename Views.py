#I have created this file=DISHA PUROHIT

from django.http import  HttpResponse
from django.shortcuts import render

# def index(request):
#     return  HttpResponse('''<h1>Disha</h1> <a href="https://cloud.r-project.org/s"> my file1</a>''')
#
# def index(request):
#     return  HttpResponse('''<h1>Disha2</h1> <a href="http://127.0.0.1:8000/analyze?text=plz+remove...%3A%27%3B+punc&removepunc=on">my file2</a>''')
#
# def index(request):
#     return  HttpResponse('''<h1>Disha3</h1> <a href="https://www.google.co.in/"my file3</a>''')
#
# def about(request):
#     return  HttpResponse("About Disha")

def index(request):
    params={'name':'Disha','place':'india'}
    return render(request,'index.html',params)
    # return HttpResponse("HOME")

# def removepunc(request):
#     # get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse("RemovePunc")

def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')

    # check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')



    print(removepunc)
    print(djtext)

    # check which checkbox is on
    if removepunc=="on":
        analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=" "
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punc','analyzed_text':analyzed}
    # analyze the text
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=" "
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        # analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = " "
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'remove NewLines', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = " "
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'remove NewLines', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == "on"):
        analyzed = " "
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'char count', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!= "on" and charcount!= "on"):
        return HttpResponse("Error! Please select any option <br> Try again")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("CapitalizeFirst")
#
# def NewLineRemove(request):
#     return HttpResponse("NewLineRemove")
#
# def SpaceRemove(request):
#     return HttpResponse("SpaceRemove <a href='/'>back</a>")
#
# def CharCount(request):
#     return HttpResponse("CharCount")


