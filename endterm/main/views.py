from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import Achievements
from django.http import HttpResponse, JsonResponse

from django.http import HttpResponse


#def home(request):
 #   return render(request, 'home.html')
@csrf_exempt
def ahievments_list(request):
    if request.method=='GET':
        achievements = Achievements.object.all()
        achievements = [a.to_json() for a in achievements]
        return JsonResponse(achievements, safe=False)
    elif request.method == 'POST':
        data = JsonResponse.loads(request.body)
        achievements = Achievements (id = data['id'])
        achievements = Achievements (Personid = data[ 'Personid'])
        achievements = Achievements (Categoryid = data [ 'Categoryid'])
        achievements = Achievements (Date = data ['Date'])
        achievements = Achievements (Title = data [ 'Title'])
        achievements.save()
        return  JsonResponse(achievements.to_json())




