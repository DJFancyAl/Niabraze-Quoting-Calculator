# Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Collect static assets
python manage.py collectstatic

# Run database migrations
python manage.py migrate
