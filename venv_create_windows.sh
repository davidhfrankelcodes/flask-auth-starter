#!/bin/bash

# Ask user for path, defaulting to current working directory
read -p "Enter the path (or leave blank for current working directory): " dir
if [ -z "$dir" ]; then
    dir=$(pwd)
fi

# Output the chosen path
echo "You chose $dir"

cd $dir
python -m virtualenv venv 
source venv/Scripts/activate
pip install -r requirements.txt
cd - >> /dev/null
deactivate
echo "Done."
