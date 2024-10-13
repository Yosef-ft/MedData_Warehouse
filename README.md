# Building a Data Warehouse for Ethiopian Medical Business Data
## Overview
This project aims to create a robust data warehouse for storing and analyzing data related to Ethiopian medical businesses scraped from Telegram channels. The system is designed to enhance data analysis by centralizing information.

## Project Goals
1. Developing a Data Scraping and Collection Pipeline
    - Scraping relevant data and images from Telegram channels that focus on Ethiopian medical businesses.
2. Data Cleaning and Transformation
    - Using DBT (Data Build Tool) for data transformation and documentation.
3. Object Detection Using YOLO
    - You can open the note books here to see the perfomance of existing pretraind YOLOv5 moodels. <a href="https://colab.research.google.com/github/Yosef-ft/MedData_Warehouse/blob/main/notebooks/Yolo_Pretrained_models.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> 
    - From the above notebook we can see that there is a need to create a custom model based on our custom medicine data. You can find the details of training a custom model and see the results of the model here. <a href="https://colab.research.google.com/github/Yosef-ft/MedData_Warehouse/blob/main/notebooks/YOLO_Custom_model.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a> 
4. Data Exposure using fact API

## Getting Started
### Prerequisites
Make sure you have the following installed:
  * Python 3.x
  * Pip (Python package manager)

### Installation
Clone the repository:
```
git clone https://github.com/Yosef-ft/MedData_Warehouse.git
cd MedData_Warehouse
```
Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install the required packages:
```
pip install -r requirements.txt
```
