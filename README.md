# ArtSphere

Welcome to the repository for **ArtSphere**! This project demonstrates the integration of API data handling, in-memory operations, CRUD functionality, and cart management for an art collection. It showcases advanced skills in Flask development, data management, and seamless integration with a React-based frontend.

## 🚀 Overview

This project covers the complete development lifecycle of an art management system, from loading and modifying art data to providing user-friendly API endpoints for a React frontend. It is tailored for developers proficient in Flask, API integration, and frontend-backend communication.

### Key Sections
- **Data Loading** – A service to load initial art collection data from CSV files into memory for operations.
- **CRUD Operations** – Flask API endpoints for creating, reading, updating, and deleting art pieces.
- **Cart Management** – Functionality to manage a user cart, including adding, fetching, and removing items.
- **Search & Filter** – API for searching and filtering art pieces by attributes such as title, author, or location.
- **Profile View** – Endpoints for fetching detailed profiles of specific art pieces.
- **Frontend Integration** – Designed to seamlessly connect with a React-based frontend for user interaction.

## 🔧 Technologies Used

- **Flask** – Python-based micro-framework for developing the backend.
- **Pandas** – Data manipulation library for managing art collection data.
- **React** – Frontend framework for creating a dynamic user interface.


## ✨ Features

- **API Integration:** Seamless integration with a React frontend using RESTful API endpoints.
- **CRUD Operations:** Full control over the art collection, with endpoints for creating, reading, updating, and deleting art pieces.
- **Cart Management:** API endpoints for managing a cart of selected art pieces, including adding and removing items.
- **Search Functionality:** Powerful search and filter functionality to explore the art collection by various attributes.
- **Profile Views:** Dedicated endpoints for fetching detailed profiles of individual art pieces.
- **Frontend Compatibility:** Designed for easy integration with a React-based frontend, offering a seamless user experience.

## 📁 Project Structure

```bash
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── controllers/
│   │   ├── art_controller.py  # Art-specific API endpoints
│   ├── services/
│   │   ├── data_handler.py    # Load and save data logic
│   ├── models.py            # Data models for the art collection
│   ├── routes.py            # Centralized route management
│   └── test.py              # Unit tests for API endpoints
├── static/
│   ├── assets/              # Static files for visualizations
├── templates/
│   ├── index.html           # HTML templates (if used)
├── requirements.txt         # Python dependencies
└── README.md                # This file
