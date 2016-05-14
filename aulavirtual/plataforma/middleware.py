from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import HttpResponse
from social import exceptions as social_exceptions

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def process_exception(self, request, exception):		
		if hasattr(social_exceptions, 'AuthCanceled'):
			return HttpResponse("<h2>Cancelaste las solicitud de login, <a href='/'>Volver</a></h2>")
		else:
			raise exception