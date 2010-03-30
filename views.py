from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

from translate import process_csp
def map_color (request):
	return render_to_response('map_color.html',{})

def solve(request):
	if request.POST:
		matrix = request.POST.get('matrix')
		count = request.POST.get('count')
	color_solution = process_csp(matrix,count)
	color = unicode(color_solution[0])
	data = {"matrix": color}
	return HttpResponse(simplejson.dumps(data), mimetype= 'application/json')
