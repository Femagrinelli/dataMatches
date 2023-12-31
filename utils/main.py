import configparser



if __name__ == '__main__':
    CONFIG = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    CONFIG.read('../Settings.ini')
    ACCESSKEY_PATH = CONFIG['AUTH_S3']['AccessKey']
    SECRETKEY_PATH = CONFIG['AUTH_S3']['SecretKey']

    RIOT_API_PATH = CONFIG['AUTH_RIOT_API']['ApiKey']

    with open(ACCESSKEY_PATH, 'r', encoding='utf-8') as f:
        ACC_KEY = f.read()

    with open(SECRETKEY_PATH, 'r', encoding='utf-8') as f:
        SEC_KEY = f.read()

    with open(RIOT_API_PATH, 'r', encoding='utf-8') as f:
        API_KEY = f.read()
