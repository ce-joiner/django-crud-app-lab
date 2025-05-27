from django.shortcuts import render, redirect
from .models import Tea, Teaware
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BrewingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

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
    teaware = tea.teaware.all()  # Get all teaware associated with this tea
    available_teaware = Teaware.objects.exclude(teas=tea)  # Get teaware NOT associated with this tea
    brewing_form = BrewingForm()  # Create an instance of the BrewingForm
    return render(request, 'teas/details.html', {
        'tea': tea, 
        'teaware': teaware, 
        'available_teaware': available_teaware,  # Add this line
        'brewing_form': brewing_form
    })

class TeaCreate(CreateView):
    model = Tea
    fields = [field.name for field in Tea._meta.fields if field.name != 'teaware']  # Exclude 'teaware' field from the form
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
   
class TeawareUpdate(UpdateView):
    model = Teaware
    fields = '__all__'  

class TeawareDelete(DeleteView):
    model = Teaware
    success_url = '/teaware/'  # Redirects to teaware list after deletion

def associate_teaware(request, tea_id, teaware_id):
    # Note that you can pass a toy's id instead of the whole object
    Tea.objects.get(id=tea_id).teaware.add(teaware_id)
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page after association

def remove_teaware(request, tea_id, teaware_id):
    Tea.objects.get(id=tea_id).teaware.remove(teaware_id)  # Remove the association between the tea and teaware
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page after removal


# This class-based view uses Django's built-in LoginView to handle user authentication.
class Home(LoginView):
    template_name = 'home.html'
