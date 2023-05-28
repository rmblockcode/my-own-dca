import ccxt
import pandas as pd

# okx = ccxt.okx(
#     {
#         'apiKey': 'EXCHANGE_API_KEY',
        # 'secret': 'EXCHANGE_SECRET',
        # 'password': 'EXCHANGE_PASSWORD'
#     }
# )

exchange_list = [
    {
        'exchange': 'okx',
        'apiKey': 'EXCHANGE_API_KEY', # Ver el video en YT para saber como obtenes estas credenciales
        'secret': 'EXCHANGE_SECRET',
        'password': 'EXCHANGE_PASSWORD'
    },
    # ...
]

for exchange in exchange_list:
    print('--------------------')
    print('Exchange: ', exchange.get('exchange'))
    ex = getattr(ccxt, exchange.get('exchange'))({
        'apiKey': exchange.get('apiKey'),
        'secret': exchange.get('secret'),
        'password': exchange.get('password')
    })
    # print(ex.fetch_balance())
    data = ex.fetchOHLCV('BTC/USDT', limit=60)
    df = pd.DataFrame(data)
    df.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']
    print(df)