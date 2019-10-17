import json
import os
import shutil

from .log import logger

class Config:
    def __init__(self, path='config.json'):
        self.path = path
        self.default_values = {
            'songs_path': 'songs',
            'skin': 'default',
        }
        self.user_values = self.load()

    def get(self, key):
        if key not in self.default_values:
            raise KeyError('{} is not a config property'.format(key))
        return self.user_values.get(key, self.default_values.get(key))

    def set(self, key, value, save=True):
        if key not in self.default_values:
            raise KeyError('{} is not a config property'.format(key))
        self.user_values[key] = value
        if save:
            self.dump_config()

    def load(self):
        try:
            with open(self.path) as f:
                return json.loads(f.read())
        except FileNotFoundError:
            return self.new_config()
        except json.JSONDecodeError:
            backup_name = self.backup()
            logger.warning(
                '{} was malformed, copy made at {},'
                ' creating new config...'.format(self.path,backup_name
            ))
            return self.new_config()


    def save(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.user_values, indent='\t'))

    def new_config(self):
        self.user_values = {}
        self.save()
        return self.user_values

    def backup(self):
        file_format = self.path + '.{}.backup'
        i = 0
        while os.path.exists(file_format.format(i)):
            i += 1
        return shutil.copy(self.path, file_format.format(i))
