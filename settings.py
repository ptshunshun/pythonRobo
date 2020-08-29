import os
CSV_FILE_PATH = None
# TEMPLATE_PATH = '~/python3/src/roboter/roboter/templates/'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(base_dir, 'roboter/roboter/templates')