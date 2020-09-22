

# Create your views here.
from django.http import HttpResponse
from django.views import View


class RegisterView(View):

     def get(self, request):

         return HttpResponse(
             "注册"
         )