# **Snowpark Bulk Excel Loader**

This project provides a Python-based solution to load bulk Excel/CSV files into Snowflake using **Snowpark**. It automates the process of reading, transforming, and loading large datasets into Snowflake tables with minimal manual intervention, leveraging the Snowpark framework for scalability and performance.

## **Features**
- Bulk upload of CSV/Excel files into Snowflake tables.
- Utilizes **Snowpark** for seamless data transformation and integration with Snowflake.
- Automated data pipeline to handle multiple input files and output tables.
- Customizable for various data sources and Snowflake schema configurations.
- Error handling and logging to track pipeline execution and file loads.
  
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
