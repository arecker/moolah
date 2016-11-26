from django.db.models import BooleanField


class UniqueBooleanField(BooleanField):

    """http://stackoverflow.com/a/11752305"""

    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects
        # If True then set all others as False
        if getattr(model_instance, self.attname):
            objects.update(**{self.attname: False})
            # If no true object exists that isnt saved model, save as True
        elif not objects.exclude(id=model_instance.id)\
                        .filter(**{self.attname: True}):
            return True
        return getattr(model_instance, self.attname)
