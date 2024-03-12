from django.shortcuts import render


def home(request):
   
    restored_card = request.GET.get('restoredCard')
    card_id = request.GET.get('cardId')

   
    context = {
        'restored_card': restored_card,
        'card_id': card_id,
    }
    return render(request, 'land_page.html', context)

def archive(request):
    return render(request,'archive.html')
def dash(request):
    return render(request,'dash.html')
