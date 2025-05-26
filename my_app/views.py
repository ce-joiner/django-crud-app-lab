from django.shortcuts import render, redirect
from .models import Tea, Teaware
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BrewingForm
from django.views.generic import ListView, DetailView
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
    brewing_form = BrewingForm()  # Create an instance of the BrewingForm
    return render(request, 'teas/details.html', {'tea': tea, 'brewing_form': brewing_form})

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
   
def add_brewing(request, tea_id):
    form = BrewingForm(request.POST)  # Create a form instance with the submitted data
    if form.is_valid():  # Check if the form is valid
        new_brewing = form.save(commit=False)  # Create a Brewing instance without saving to the database yet
        new_brewing.tea_id = tea_id  # Associate the brewing with the specific tea
        new_brewing.save()  # Save the brewing instance to the database
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page

class TeawareCreate(CreateView):
    model = Teaware
    fields = '__all__'  # Use all fields from the Teaware model
    success_url = '/teaware/'  # Redirects to teaware list
    
class TeawareDetail(DetailView):
    model = Teaware
   
class TeawareList(ListView):
    model = Teaware
   