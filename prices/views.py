import requests
from django.http import JsonResponse

def get_usdt_price(request):
    try:
        url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
        payload = {
            "asset": "USDT",
            "fiat": "BOB",
            "merchantCheck": False,
            "page": 1,
            "rows": 20,  # Obtener las primeras 20 ofertas
            "payTypes": [],
            "tradeType": "BUY"
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # Extraer precios
        prices = [
            float(offer['adv']['price'])
            for offer in data['data']
        ]

        # Calcular la media
        average_price = round(sum(prices) / len(prices), 4) if prices else None

        return JsonResponse({
            'usdt_price_bs_average': average_price,
            'offers_considered': len(prices)
        })

    except Exception as e:
        print(f"Error obteniendo precio promedio P2P: {e}")
        return JsonResponse({'error': 'No se pudo obtener el precio'}, status=500)
