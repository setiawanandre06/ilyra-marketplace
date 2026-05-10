from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def calculator_view(request):
    context = {
        'title': 'Kalkulator Harga & Keuntungan',
        # Keep the standard admin context if extending admin/base_site.html
    }
    return render(request, 'marketplaces/calculator.html', context)
