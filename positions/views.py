from django.shortcuts import render

from .models import Position
import requests


def home_view(request):
    """View that gets data from the API and shows it on template"""
    data = Position.objects.all()

    context = {"data": data}
    return render(request, "positions/main.html", context)
def get_usd_to_vnd():
    """Get the latest USD to VND exchange rate"""
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    if 'rates' in data and 'VND' in data['rates']:
        return data['rates']['VND']
    else:
        return 1  
def home_view(request):
    """View that gets data from the API and shows it on template"""
    data = Position.objects.all()
    
    # Lấy tỷ giá USD/VND
    usd_to_vnd = get_usd_to_vnd()

    # Chuyển đổi giá USD sang VND cho từng Position
    for position in data:
        position.price_vnd = float(position.price) * usd_to_vnd  # Thêm giá trị VND vào đối tượng Position

    context = {"data": data, "usd_to_vnd": usd_to_vnd}
    return render(request, "positions/main.html", context)