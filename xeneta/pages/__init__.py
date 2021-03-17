_global_driver = None
_global_site = None


def set_site(site):
    global _global_site
    _global_site = site


def get_site():
    return _global_site


def set_driver(driver):
    global _global_driver
    _global_driver = driver


def get_driver():
    return _global_driver
