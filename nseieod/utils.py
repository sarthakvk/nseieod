import nsetools

nse = nsetools.Nse()

# fuction to get get_quote data from
# nse website
def get_quote(code):
    quote = nse.get_quote(code)
    return quote


# function to get company stock_codes
# from nse website
def get_company_codes():
    company_codes = nse.get_stock_codes()
    # delete 'SYMBOL' from dict
    del company_codes["SYMBOL"]
    return company_codes


# function to convert stock_code to sutaible postgresql table name
def get_table_name(code):
    table_name = code.lower()
    table_name = table_name.translate(
        {ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-= +"}
    )
    return table_name
