from loader import load_config
from system import run_system

print("\n Config Driven App Online")

config = load_config()
run_system(config)
