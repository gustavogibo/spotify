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

## License
MIT