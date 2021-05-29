from django.shortcuts import redirect

def LoginCheckMiddleware(get_response):

	def middleware(request):
		# This is for getting the path of current url
		returnUlr = request.META['PATH_INFO']
		if not request.session.get('username'):
			# this is for redirecting that page
			return redirect(f'login?return_url={returnUlr}')

		return get_response(request)

	return middleware


def LogoutCheckMiddleware(get_response):

	def middleware(request):
		if request.session.get('username'):
			return redirect('home')

		return get_response(request)

	return middleware