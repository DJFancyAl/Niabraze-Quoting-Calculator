# Exit on error
set -o errexit

# Install Python dependencies
pip install requirements.txt

# Collect static assets
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate
