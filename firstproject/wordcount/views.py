from django.shortcuts import render

# Create your views here.
def wordcount(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split(" ")

    word_dict = dict()
    
    for words in word_list:

        if words in word_dict:
    
            word_dict[words] += 1
        else:
            word_dict[words] = 1

    return render(request, 'count.html', {'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dict.items()})