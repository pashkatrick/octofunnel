import json

with open('config.json', 'r') as f:
    config = json.load(f)


def get_chromium_path():
    return config['chromium_path']


def get_driver_path():
    return config['driver_path']


def get_sessions_path():
    return config['sessions_folder']
