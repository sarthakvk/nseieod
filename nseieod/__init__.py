import argparse
from .utils import get_company_codes, get_table_name
from .db import StockDB

# function to setup initialization
def init():
    sd = StockDB()
    sd.create_db()
    print("Created Database!")
    codes = get_company_codes()
    for code in codes.keys():
        sd.create_table(get_table_name(code))
    print("Created Tables")
    print("Done setup!")


# function to parse positional and optional arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="Getting last traded price for stonks listed in NSE"
    )
    parser.add_argument(
        "--init", action="store_true", help="initialize database and create tables"
    )
    parser.add_argument(
        "-g",
        "--get-only",
        type=str,
        nargs="+",
        help="get only the specified stonks from NSE(you can use code or name of stock and it's case insensitive",
    )
    return parser.parse_args()


# funtion for calling functions based on args
def run():
    args = parse_args()
    if args.init:
        init()
    if args.get_only:
        pass
    else:
        pass
