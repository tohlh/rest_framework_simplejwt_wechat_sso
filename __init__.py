from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("djangorestframework_simplejwt_wechat_sso").version
except DistributionNotFound:
    # package is not installed
    __version__ = None
