from django.contrib.contenttypes.fields import GenericForeignKey

from djangocms_versioning.models import Version
from filer.models import File, Image


def generic_foreignkey__get_(func):
    """
    in versioning filer, it force the version content of images to use `file` content type,
    that will lead to the ignore of field cache, and another error in `get_latest_draft_version`
    helper function in djangocms-versioning addon.

    so my temp patch is to pass the comparison of contenttype (version.content_type and the 
    content type of cached field), to correctly use the field cache.
    """
    def inner(self, instance, cls=None):
        if isinstance(instance, Version):
            content = self.get_cached_value(instance, default=None)
            if content and isinstance(content, Image):
                content.__class__ = File
                res = func(self, instance, cls)
                content.__class__ = Image
                return res
        return func(self, instance, cls)
    return inner


GenericForeignKey.__get__ = generic_foreignkey__get_(GenericForeignKey.__get__)
