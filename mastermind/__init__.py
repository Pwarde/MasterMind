import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
sys.path.append(f"{BASE_DIR}")
print(sys.path)