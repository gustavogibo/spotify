# Spotify Data Analysis & Power BI Portfolio

## Overview
This repository hosts a data science and analysis project focused on Spotify data. The objective is to extract, process, and analyze music data to uncover insights, visualized through an interactive Power BI dashboard.

## Technologies
*   **Python**: Used for data collection (Spotify API), cleaning, and transformation.
*   **Pandas/NumPy**: Data manipulation libraries.
*   **Power BI**: Dashboarding and visualization.

## Project Structure
The project is organized as follows:

```text
├── data/               # Raw and processed datasets (csv, json)
├── src/                # Source code for data processing scripts
├── .gitignore          # Git ignore file
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites
*   Python 3.8+
*   Power BI Desktop

### Installation
1.  Clone the repository.
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
*   Run the scripts in `src/` to clean and process the data.
*   Open the `.pbix` file in Power BI to interact with the dashboard.


## 🧹 Data Cleaning & Transformation
Raw data often contains inconsistencies that can break Power BI models. I built a Python script (`data_cleaning.py`) to automate the ETL (Extract, Transform, Load) process.

**Key Cleaning Steps Performed:**
* **Standardization:** Converted all column headers to `snake_case` (e.g., `Track Name` → `track_name`) and removed special characters to ensure clean DAX references in Power BI.
* **Deduplication:** Scanned for and removed full-row duplicates to ensure stream counts remain accurate.
* **Data Quality Enforcement:** Removed records where critical identifiers (`track_name` or `album_name`) were null. 
    * *Note: These missing values represented <0.05% of the dataset, so dropping them preserved data integrity without skewing results.*
* **Output:** The script generates a clean file (`dataset-cleaned.csv`) ready for direct import into Power BI.

## License
MIT