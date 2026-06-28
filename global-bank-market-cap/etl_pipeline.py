import pandas as pd
import datetime
import requests
from io import StringIO
from bs4 import BeautifulSoup

log_file_path = r"C:\Users\Temitope.Arigbede\loggy.txt"
output = r"C:\Users\Temitope.Arigbede\Largest_banks_data.csv"


def log_sheet(message):
    with open(log_file_path, "a") as log:
        datestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log.write(f"{message} on {datestamp} at {timestamp}\n")


def extract():
    url = "https://en.wikipedia.org/wiki/List_of_largest_banks"

    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, "html.parser")

    table = soup.find_all("table")[0]

    df = pd.read_html(str(table))[0]

    df = df.iloc[:, 1:]
    df.columns = ["Name", "MC_USD_Billion"]

    return df


def transform(df):
    try:
        csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
        rates = pd.read_csv(csv_url)

        # STEP 1: force clean conversion safely
        rates["Rate"] = (
            rates["Rate"]
            .astype(str)
            .str.extract(r"([\d.]+)")[0]
        )

        rates["Rate"] = pd.to_numeric(rates["Rate"], errors="coerce")

        # STEP 2: remove bad rows instead of risking NaN
        rates = rates.dropna(subset=["Rate"])

        rates_dict = dict(zip(rates["Currency"], rates["Rate"]))

        # STEP 3: clean bank data safely
        df["MC_USD_Billion"] = pd.to_numeric(
            df["MC_USD_Billion"].astype(str).str.extract(r"([\d.]+)")[0],
            errors="coerce"
        )

        df = df.dropna(subset=["MC_USD_Billion"])

        # STEP 4: calculations
        df["MC_GBP_Billion"] = df["MC_USD_Billion"] * rates_dict["GBP"]
        df["MC_EUR_Billion"] = df["MC_USD_Billion"] * rates_dict["EUR"]
        df["MC_INR_Billion"] = df["MC_USD_Billion"] * rates_dict["INR"]

        df = df.round(2)

        log_sheet("Transformation completed successfully")
        return df

    except Exception as e:
        log_sheet(f"Transformation failed: {e}")
        raise


def load_to_csv(df, output):
    try:
        df.to_csv(output, index=False)
        log_sheet("CSV file created successfully")

    except Exception as e:
        log_sheet(f"Load failed: {e}")
        raise

def main():
    try:
        log_sheet("Script started")

        df_extracted = extract()
        df_transformed = transform(df_extracted)
        display(df_transformed.head(10))
        load_to_csv(df_transformed, output)

        log_sheet("Script completed successfully")
        print("Script ran successfully. Check log file and output CSV.")

    except Exception as e:
        log_sheet(f"Script failed: {e}")
        print(f"Error occurred: {e}")



if __name__ == "__main__":
    main()