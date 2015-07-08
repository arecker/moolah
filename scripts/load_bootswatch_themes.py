from authenticating.models import Theme


theme_list = [
    'Cerulean',
    'Cosmo',
    'Cyborg',
    'Darkly',
    'Flatly',
    'Journal',
    'Lumen',
    'Paper',
    'Readable',
    'Sandstone',
    'Simplex',
    'Slate',
    'Spacelab',
    'Superhero',
    'United',
    'Yeti'
]


def run(*args):
    """
    Loads bootswatch themes into Theme
    """
    if 'purge' in args:
        Theme.objects.all().delete()
    for n in theme_list:
        Theme(
            name=n,
            url='//bootswatch.com/{0}/bootstrap.min.css'.format(n.lower())
        ).save()
