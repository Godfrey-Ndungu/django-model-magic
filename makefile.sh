#!/bin/bash

# Script for Django project setup

set -e

# Install the latest Python version
echo "Installing Python..."
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.10

# Install build tools, setup tools, pip, and venv
echo "Installing build tools and dependencies..."
sudo apt-get install -y build-essential python3.10-dev python3.10-venv python3.10-distutils

# Install pip
echo "Installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.10 get-pip.py
rm get-pip.py

# Create and activate a virtual environment
echo "Creating and activating virtual environment..."
python3.10 -m venv venv
source venv/bin/activate

# Install project dependencies
echo "Installing project dependencies..."
pip install -r requirements.txt

# Migrate the Django project
echo "Running database migrations..."
python manage.py migrate

# Start the development server
echo "Starting the development server..."
python manage.py runserver
