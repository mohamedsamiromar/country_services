from core.utils import get_config


class Configuration:
    def WEBSITE_URL():
        return str(get_config(
            key="WEBSITE_URL",
            type='string'
        ))
