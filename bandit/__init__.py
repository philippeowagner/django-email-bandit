"""
django-email-bandit is a Django email backend for hijacking email sending in a test environment.
"""

__version_info__ = {
    'major': 1,
    'minor': 3,
    'micro': 0,
    'releaselevel': 'dev',
}


def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
