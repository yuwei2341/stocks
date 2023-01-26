sp500_fulllist.csv: full sp500 companies (299 because GOOG and GOOGL are both in it), as of 02/02/2022, from wiki
sp500_fulllist_ranked.csv: copy-pasted with mkt cap from https://www.slickcharts.com/sp500


sp500_history_price_raw.csv: daily price data of sp500 stocks, downloaded using akshare from finance.sina.com.cn/stock/usstock/sector.shtml
sp500_history_raw.csv: fundamental data of sp500 stocks, downloaded using akshare from https://www.macrotrends.net/stocks/charts/AAPL/apple/pe-ratio. The data is quarterly, while the last row is values on the day of data retrieval 
sp500_history_filterd.csv: fundamental data of sp500 stocks, processed from sp500_history_raw.csv including formating and conversion to quarter


sp500_index_history.csv: history of sp500 index from https://datahub.io/core/s-and-p-500#resource-data
fed_funds_rate_historical.csv: history of fed funds rate from macrotrends


backup:
sp500_1_300_list.csv: top 300 company stock symbol in sp500 based on mkt cap (299 because GOOG and GOOGL are both in it), as of 04/18/2021
sp500_1_300_history_raw.csv: quarterly price, earning, book value, pe and pb of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from macrotrend. Most start from 2006. 
sp500_1_300_history_filterd.csv: quarterly price, earning, book value, pe and pb of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from macrotrend. Most start from 2006. The following stocks are removed: 1) with less than 29 quarters filtered out, or 2) with over 20 quarters with negative equity. Also some inf value imputed to 0
sp500_1_300_history_price_raw.csv: daily price data of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from finance.sina.com.cn/stock/usstock/sector.shtml

For all rows, if the eps is null or negative, the pe is 0; if the book value is null, the pb is 0
The last row for each stock is the value when data were pulled. The eps and book value are null. The pe and pb ratio for that rwo was computed with current price, and eps and book value from previous quarter. 