# FatSecret API Integration with FastAPI & OAuth 2.0

This is a simple FastAPI application that integrates with the FatSecret API to search for food items, using OAuth 2.0 for authentication.

## Features

- OAuth 2.0 authentication to interact with the FatSecret API.
- Search for food items by name with paginated results.
- Provides detailed nutritional information for foods.

## Requirements

Before you begin, make sure you have the following installed:

- Python 3.8 or higher
- FastAPI
- Uvicorn (for running the server)
- Requests library
- Python-dotenv (for managing environment variables)
- Postman (for testing the API)

## Installation

### Clone the Repository

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/zuberkhan01st/O-Auth.2.0_using_FastAPI.git


cd O-Auth.2.0_using_FastAPI


Create a Virtual Environment

Install Required Dependencies
fastapi==0.68.0
uvicorn==0.15.0
requests==2.26.0
python-dotenv==0.19.0


```
## Project Directory Structure

Below is the directory structure of this project:

```plaintext
your-repository/
│
├── app.py                 
├── .env               
├── requirements.txt       
├── assets/                   
│   └── images/             
│       └── Screenshot.png    
├── README.md                 
└── venv/                     
```

## Demo Screenshot

Here is a demo screenshot of the Postman request and response for the `/search_foods` endpoint:

![Demo Screenshot](assets/images/Screenshot%202025-01-29%20183411.png)

> Note: The screenshot is stored in the `assets/images/` folder in the repository.

