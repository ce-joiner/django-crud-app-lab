from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello tea lover!</h1>')  

def about(request):
    return render(request, 'about.html')  

class Tea:
    def __init__(self, name, description, type, origin, image):
        self.name = name
        self.description = description
        self.type = type
        self.origin = origin
        self.image = image
        
teas = [
    Tea('2024 Nightlife', 'Heavy, creamy mouthfeel with an airy sweetness and aroma', 'Moonlight white', 'Yunnan, China', ),
    Tea('2016 Poundcake', 'A blend of raw Puer material that has strength, medium light bitterness, and sweetness', 'Raw Puer', 'Yunnan, China'),
    Tea('Duckshit on the Breeze', 'Elegant and wisy take on the classic Duckshit tea', 'Dancong Oolong', 'Guangdong Province, China'),
    Tea('Fruit Bomb Lapsang', 'Heavy, intense fruit fragrances over a full bodied, smoky black tea', 'Lapsang Souchong', 'Fujian Province, China')
]

def tea_index(request):
    # render the tea_index.html template with the teas list
    return render(request, 'teas/index.html', {'teas': teas})