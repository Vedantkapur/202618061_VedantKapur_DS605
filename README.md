# Assignment Title

Web Scraping, Data Preprocessing and Analysis using Scrapy

## Student Details

Name: Vedant Kapur
Enrollment ID: 202618061

## Project Overview

This project demonstrates a complete data pipeline using Python and Scrapy. Book information was collected from the website Books to Scrape and then processed using Pandas. The cleaned dataset was analyzed through multiple visualizations, followed by data-driven insights.

---

## Objectives

- Scrape book information from five catalogue pages.
- Extract detailed information from each individual book page.
- Clean and preprocess the collected data.
- Generate useful visualizations.
- Interpret the results using statistical analysis.

---

## Technologies Used

- Python
- Scrapy
- Pandas
- Matplotlib
- WordCloud

---

## Dataset

Website:

https://books.toscrape.com/

Fields Collected

- Title
- Category
- Price
- Rating
- Availability
- Description
- UPC
- Number of Reviews
- Product URL

---

## Data Preprocessing

The preprocessing stage included:

- Removing duplicate books using UPC.
- Cleaning text fields.
- Handling missing descriptions.
- Converting prices into numeric values.
- Mapping ratings from text to integers.
- Extracting stock counts.
- Creating new features:
  - Description Word Count
  - Premium Book Indicator
  - Popularity Score

---

## Visualizations

The following plots were generated:

- Price Distribution
- Rating Distribution
- Average Price by Category
- Price vs Rating
- Word Cloud from Book Descriptions

---

## Key Insights

- Most books fall into the low to medium price range.
- Higher prices do not necessarily correspond to higher ratings.
- Some categories contain considerably more books than others.
- Most books remain available in stock.
- The cleaned dataset contained minimal missing values after preprocessing.

---

## Project Structure

bookscraper/

├── books.csv

├── books_cleaned.csv

├── preprocessing.py

├── visualization.py

├── README.md

├── bookscraper/

│ └── spiders/

│ └── books_spider.py

---

## Conclusion

The project successfully demonstrates the complete workflow of web scraping, data preprocessing, visualization, and exploratory data analysis using Python.
