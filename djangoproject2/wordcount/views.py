from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] #받아오는 원문 글 전체
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dict
            word_dictionary[word] = 1


    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()}) #dict 활용 풀이라 쓰고 텍스트로 읽는다.
    #items()를 사용해서 쌍을 나타낸다.