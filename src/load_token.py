import yaml


def load_token():
    with open('../.token.yaml') as f:
        obj = yaml.safe_load(f)
        return obj['token']
