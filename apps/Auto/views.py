# # auto/views.py
#
# from django.http import JsonResponse
# from apps.Auto.models import Auto
#
# def filter_autos(request):
#     przebieg_min = request.GET.get('przebieg_min')
#     przebieg_max = request.GET.get('przebieg_max')
#     rok_min = request.GET.get('rok_min')
#     rok_max = request.GET.get('rok_max')
#     fraza = request.GET.get('fraza')
#
#     autos = Auto.objects.all()
#
#     if przebieg_min:
#         autos = autos.filter(przebieg__gte=przebieg_min)
#     if przebieg_max:
#         autos = autos.filter(przebieg__lte=przebieg_max)
#     if rok_min:
#         autos = autos.filter(rok_produkcji__gte=rok_min)
#     if rok_max:
#         autos = autos.filter(rok_produkcji__lte=rok_max)
#     if fraza:
#         autos = autos.filter(fraza__icontains=fraza)
#
#
#     data = [{'przebieg': auto.przebieg, 'rok_produkcji': auto.rok_produkcji, 'fraza': auto.fraza} for auto in autos]
#     return JsonResponse(data, safe=False)
