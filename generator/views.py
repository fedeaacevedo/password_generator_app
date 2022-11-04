from django.shortcuts import render
from django.http import HttpResponse
import random 


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html') 

def password(request):
    
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_paswword = ''
    
    #Traemos el largo que el usuario quiere para su password y lo pasamos al for 
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑPQRSTUVWXYZ'))
        
    if request.GET.get('special'):
        characters.extend(list('!"#$%&/()=?¡¿+{][¨¨.,.-+~'))
    
    if request.GET.get('number'):
            characters.extend(list('1234567890'))    
    
    #recorremos nuestra lista y vamos usando los caracteres
    for char in range(length):
        generated_paswword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': generated_paswword})