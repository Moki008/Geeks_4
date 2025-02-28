from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

Junior_club = 'Junior'
Middle_club = 'Middle'
Senior_club = 'Senior'


class ExperienceClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if 0 < experience <= 3 :
                request.club = Junior_club
            elif 3 < experience <= 6:
                request.club = Middle_club
            elif 6 < experience < 50:
                request.club = Senior_club
            else:
                return HttpResponseBadRequest('Введи опыт адекватно!')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request,'club',"Клуб не определен")