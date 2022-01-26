sp500_1_300_list.csv: top 300 company stock symbol in sp500 based on mkt cap (299 because GOOG and GOOGL are both in it), as of 04/18/2021

sp500_1_300_history_raw.csv: quarterly price, earning, book value, pe and pb of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from macrotrend. Most start from 2006. 

sp500_1_300_history_filterd.csv: quarterly price, earning, book value, pe and pb of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from macrotrend. Most start from 2006. The following stocks are removed: 1) with less than 29 quarters filtered out, or 2) with over 20 quarters with negative equity. Also some inf value imputed to 0

sp500_1_300_history_price_raw.csv: daily price data of the top 300 companies from sp500_1_300_list.csv, downloaded using akshare from finance.sina.com.cn/stock/usstock/sector.shtml

For all rows, if the eps is null or negative, the pe is 0; if the book value is null, the pb is 0
The last row for each stock is the value when data were pulled. The eps and book value are null. The pe and pb ratio for that rwo was computed with current price, and eps and book value from previous quarter. 