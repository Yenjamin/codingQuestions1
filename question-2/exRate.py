import traceback
from luno_python.client import Client
import datetime, time, traceback

"""getting and formatting the information from api"""
def exRate(c):
    res = c.get_ticker(pair='XBTZAR')
    time = datetime.datetime.fromtimestamp(res['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S')
    bid = "{:.2f}".format(float(res['bid']))
    ask = "{:.2f}".format(float(res['ask']))
    avg = "{:.2f}".format(float(res['last_trade']))
    print(f"{time}  Bid: R{bid:>10}  Ask: R{ask:>10}  Avg: R{avg:>10}")

"""repeating the exRate function every 10 second"""
def repeater(c):
    nt = time.time() + 10
    while True:
        try:
            exRate(c)
        except Exception:
            traceback.print_exc()
        time.sleep(max(0, nt - time.time()))
        nt += 10

if __name__ == '__main__':
    c = Client(api_key_id='<enter key id here or environment variable of it>',
               api_key_secret='<enter key secret here or environment variable of it>')

    repeater(c)

