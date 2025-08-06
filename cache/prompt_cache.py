import os
import json
import time
import hashlib

class PromptCache:
    def __init__(self, cache_dir='cache', ttl_seconds=None):
        self.cache_dir = cache_dir
        self.ttl_seconds = ttl_seconds  
        os.makedirs(self.cache_dir, exist_ok=True)

    def _generate_key(self, prompt: str, params: dict = None) -> str:
        payload = {'prompt': prompt}
        if params:
            payload.update(params)
        raw = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()

    def _get_file_path(self, key: str) -> str:
        return os.path.join(self.cache_dir, f'{key}.json')

    def save(self, prompt: str, response: str, params: dict = None):
        key = self._generate_key(prompt, params)
        data = {
            'response': response,
            'created_at': time.time()
        }
        with open(self._get_file_path(key), 'w') as f:
            json.dump(data, f)

    def get(self, prompt: str, params: dict = None):
        key = self._generate_key(prompt, params)
        path = self._get_file_path(key)
        if not os.path.exists(path):
            return None

        with open(path, 'r') as f:
            data = json.load(f)
            if self.ttl_seconds:
                age = time.time() - data.get('created_at', 0)
                if age > self.ttl_seconds:
                    return None
            return data['response']
