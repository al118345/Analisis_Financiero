from yahoo_fin import stock_info as si
from datetime import datetime, timedelta, date
import pandas as pd

def tabla_div():
    df = pd.read_csv('tickers.csv', header=None, encoding='utf-8')
    tickers = df[0].to_list()
    df = pd.DataFrame()
    cont= 0
    for ticker in tickers:
        try:
            one_day = timedelta(days=600)
            first_day_of_the_month = date.today().replace(day=1)
            fecha_de_inidicio = first_day_of_the_month - one_day
            aux_div = si.get_dividends(ticker, start_date=fecha_de_inidicio)

            df2 = pd.DataFrame(index=aux_div.index.astype(str).to_list(), data=aux_div['dividend'].tolist(),
                              columns=[ticker])
            df= pd.concat([df2,df],axis=0)
            df = df.sort_index(ascending=False)
            cont = cont +1

        except Exception as error:
            print(str(error))
            print(ticker)
            continue
    df.to_csv('resultados_dividendos.csv', index = True)

if __name__ == '__main__':
    tabla_div()