# Install Python dependencies
python -m pip install --upgrade pip
pip install requirements.txt

# Collect static assets
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate
