from django.http import HttpResponse
from .wordgenerator import RandomWordGenerator
from django.views.decorators.cache import never_cache

# create objecto of dict_holder class
generator = RandomWordGenerator()

# this decorator makes sure you don't get same words for new requests
@never_cache
def randomword(request):
    return HttpResponse(generator.get_word())

def home(request):
	return HttpResponse("Home Sweet Home")