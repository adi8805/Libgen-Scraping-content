
# 📚 LibGen Series Scraper

A **multi-threaded web scraper** for extracting **series metadata** (name, type, language, and publisher) from [Library Genesis (libgen.li)](https://libgen.li).  
Efficient, concurrent, and saves results continuously to a CSV file for easy data handling.

---

## 📌 Features
- 🚀 **Multi-threaded scraping** with configurable concurrency  
- 📊 **Live progress tracking** using `tqdm`  
- 💾 **Auto-save to CSV** as data is fetched  
- ⚡ Handles **hundreds of thousands of records** efficiently  
- 🔁 Automatically skips missing or invalid records  

---

## 📥 Installation

Ensure you have **Python 3.7+** installed, then install dependencies:

```bash
git clone https://github.com/adi8805/Libgen-Scraping-content
cd libgen-series-scraper
pip install -r requirements.txt
````

---

## ⚡ Usage

```bash
python3 scraper.py
```
### If you face issue of overwriting use sleep to overcome overwriting
By default, it scrapes IDs from **1** to **596,257** and saves the data into `libgen_series_basic.csv`.

---

### **Custom Ranges**

Scrape only a subset of IDs by modifying these variables in the script:

```python
START_ID = 1
END_ID = 1000
OUTPUT_CSV = "my_series_data.csv"
MAX_WORKERS = 20
```

---

## 🖥 Expected Output

```text
Fetching: 100%|███████████████████████████████████████████| 596257/596257 [10:25<00:00, 952.35it/s]
Scraping complete in 627s; data saved to libgen_series_basic.csv
```

---

## 📊 CSV Output Format

|series_id|series_name|series_type|language|publisher|
|---|---|---|---|---|
|1|Example Series|Fiction|English|Example Pub|
|2|Another Series|Non-Fiction|Russian|Library House|

---

## ⚙️ Script Overview

|Variable|Description|Default|
|---|---|---|
|`BASE_URL`|URL pattern for LibGen series pages|`https://libgen.li/series.php?id={}`|
|`OUTPUT_CSV`|Output CSV file name|`libgen_series_basic.csv`|
|`START_ID`|First series ID to scrape|`1`|
|`END_ID`|Last series ID to scrape|`596257`|
|`MAX_WORKERS`|Number of concurrent threads|`20`|
|`REQUEST_TIMEOUT`|Timeout in seconds for each request|`10`|

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, make your changes, and submit a pull request.

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**.  
Scraping websites without permission may violate their terms of service — use responsibly.
