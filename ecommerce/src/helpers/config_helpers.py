import os


def get_base_url():

    env = os.environ.get('ENV', 'prod')

    if env.lower() == 'prod':
        return 'https://frontend.nopcommerce.com'
    else:
        raise Exception(f'Unknown environment: {env}')