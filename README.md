# **Snowpark Bulk Excel Loader**

This project provides a Python-based solution to load bulk Excel/CSV files into Snowflake using **Snowpark**. It automates the process of reading, transforming, and loading large datasets into Snowflake tables with minimal manual intervention, leveraging the Snowpark framework for scalability and performance.

## **Features**
- Bulk upload of CSV/Excel files into Snowflake tables.
- Utilizes **Snowpark** for seamless data transformation and integration with Snowflake.
- Automated data pipeline to handle multiple input files and output tables.
- Customizable for various data sources and Snowflake schema configurations.

  
## **Prerequisites**
Ensure the following requirements are met:
- **Python 3.8+**
- **Snowflake Account** with necessary credentials.
- **Snowflake Warehouse**, **Database**, and **Schema** setup.
- **Snowpark Python Library** installed.

### **Required Python Packages**
Install the required packages:
```bash
pip install snowflake-snowpark-python pandas
```

### **Clone the Repository**
```bash
git clone https://github.com/your-repo/snowpark-bulk-excel-loader.git
```
```bash
cd snowpark-bulk-excel-loader
```

### **Modify the Config file**
- In the config.py, you can either manually define the input file path and Snowflake Table name, or you can create a function inside the config file that automatically creates input_files and output_files list based on logic specified

### **Snowflake Credentials**
- Update the Snowflake credentials in the snowpark_bulk_load_python_file.py script, replacing placeholders with your account details.
- If you are running in the Snowflake Notebook, use active session in the snowpark_bulk_load_.ipynb

### **Run the code**
```bash
python bulk_excel_to_snowflake.py
```
- Or you can run from Snowflake Notebook (use ipynb file)

### **Project Structure**
```bash
snowpark-bulk-loader/
│
├── snowpark_bulk_load_python_file.py   # Python script for loading data
├── snowpark_bulk_load_.ipynb           # Snowflake Notebook script for loading data
├── config.py                           # Configuration file for input/output and Snowflake settings
└── README.md                           # Documentation for the project
```

