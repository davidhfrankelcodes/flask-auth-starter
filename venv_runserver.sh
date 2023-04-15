#!/bin/bash

# Function to deactivate virtual environment and change directory back to previous one
function finish {
  if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
  fi
  cd - >> /dev/null
}

# Ask user for path, defaulting to current working directory
read -p "Enter the path (or leave blank for current working directory): " dir
if [ -z "$dir" ]; then
    dir=$(pwd)
fi

# Output the chosen path
echo "You chose $dir"

# Activate virtual environment and run script, trapping interrupt signal
cd "$dir" && source venv/Scripts/activate && trap finish INT && python run.py

# Deactivate virtual environment and change directory back to previous one
finish
