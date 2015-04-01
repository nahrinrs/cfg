from config.models import Config

def get_config(limit=None, **filters):
    """ simple service function for retrieving configs can be widely extended """
    if limit:
        return Config.objects.filter(**filters)[:limit]
    return Config.objects.filter(**filters)
