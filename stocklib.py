""" Library for stocks """
#!/usr/bin/env python3

import pandas as pd


def _parse_quarter(s):
    x = s.dayofyear
    if x <= 90:
        q = "Q1"
    elif x <= 181:
        q = "Q2"
    elif x <= 273:
        q = "Q3"
    else:
        q = "Q4"
    return str(s.year) + q


def get_quarter(df, date_column="date"):
    """Get quaters from stock df"""
    df["DATE"] = pd.to_datetime(df[date_column])
    df["dayofyear"] = df["DATE"].dt.dayofyear
    df.loc[df["DATE"].dt.is_leap_year, "dayofyear"] -= 1
    df["year"] = df["DATE"].dt.year
    df["quarter"] = df.apply(_parse_quarter, axis=1)
    df = df.set_index("quarter")
    df = df.sort_index()
    return df


def pick_stocks(df, cash_to_invest, n_stocks, mmt_var, top_by_mmt):
    """Pick stocks based on momentum and pb, used in the magic formula
    - Look for the top_by_mmt fraction of companies that have the largest mmt_var
    - Sort these companies by price-to-book value in ascending order
        and take the top n_stocks stocks
    Returns
        A df with all the stocks chosen and their mmt_var and PB
    Note:
        mmt_var is a momentum variable like 6 month price momentum
    """

    cash_for_each_stock = cash_to_invest / n_stocks
    top_by_mmt = (
        df[(~df["book_value_per_share"].isnull()) & (df["price_to_book_ratio"] > 0)]
        .sort_values(mmt_var, ascending=False)
        .iloc[: round(len(df) * top_by_mmt), :]
    )
    stocks_by_mmt_pb = (
        top_by_mmt.sort_values("price_to_book_ratio").head(n_stocks).copy()
    )
    stocks_by_mmt_pb["shares"] = cash_for_each_stock / stocks_by_mmt_pb["stock_price"]
    stocks_by_mmt_pb_simple = stocks_by_mmt_pb[
        [
            "stock",
            "shares",
            "stock_price",
            mmt_var,
            "price_to_book_ratio",
            "book_value_per_share",
        ]
    ]
    # Change momentum to percentage
    stocks_by_mmt_pb_simple[mmt_var + "_pct"] = (
        stocks_by_mmt_pb_simple[mmt_var] * 100
    ).round()
    stocks_by_mmt_pb_simple = stocks_by_mmt_pb_simple.drop(mmt_var, axis=1)
    #     stocks_by_mmt_pb_simple = stocks_by_mmt_pb_simple.rename({
    #         'stock_price': 'stock_price_bought',
    #         mmt_var: mmt_var + '_bought',
    #         'price_to_book_ratio': 'price_to_book_ratio_bought',
    #         'book_value_per_share': 'book_value_per_share_bought',
    #     }, axis=1)
    return stocks_by_mmt_pb_simple
