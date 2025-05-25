from django.shortcuts import render
from .models import Tea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  

# class Tea:
#     def __init__(self, name, description, type, origin, image):
#         self.name = name
#         self.description = description
#         self.type = type
#         self.origin = origin
#         self.image = image
        
# teas = [
#     Tea('2024 Nightlife', 'Heavy, creamy mouthfeel with an airy sweetness and aroma', 'Moonlight white', 'Yunnan, China', 'images/2024Nightlife.png' ),
#     Tea('2016 Poundcake', 'A blend of raw Puer material that has strength, medium light bitterness, and sweetness', 'Raw Puer', 'Yunnan, China', 'images/poundcake.png'),
#     Tea('Duckshit on the Breeze', 'Elegant and wisy take on the classic Duckshit tea', 'Dancong Oolong', 'Guangdong Province, China', 'images/duckshit.png'),
#     Tea('Fruit Bomb Lapsang', 'Heavy, intense fruit fragrances over a full bodied, smoky black tea', 'Lapsang Souchong', 'Fujian Province, China', 'images/FruitBombLapsang.png'),
# ]

def tea_index(request):
    teas = Tea.objects.all()  # Fetch all tea objects from the database
    return render(request, 'teas/index.html', {'teas': teas})

def tea_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)  # Fetch the specific tea object by its ID
    return render(request, 'teas/details.html', {'tea': tea})

class TeaCreate(CreateView):
    model = Tea
    fields = '__all__'  # Use all fields from the Tea model
    # success_url = '/teas/'  # Redirect to the tea index page after creation
   
class TeaUpdate(UpdateView):
    model = Tea
    fields = '__all__'  # Use all fields from the Tea model

class TeaDelete(DeleteView):
    model = Tea
    success_url = '/teas/'  
   