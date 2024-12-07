from django.shortcuts import render,get_object_or_404
from searchapp.models import Item
from django.db.models import Q

# Create your views here.
def search_view(request):
    query = request.GET.get('q') or ''
    results = Item.objects.all() 
    if query:
        results = results.filter(Q(name__icontains = query)| Q(description__icontains = query))
    no_results = False
    if not results:
        no_results = True
    return render(request,'index.html',{'results':results,'query':query,'no_results': no_results})

def item_detailed_view(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    return render(request,'item_detail.html',{'item':item})