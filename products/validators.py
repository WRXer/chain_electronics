from rest_framework.exceptions import ValidationError

class ManufacturerValidator:
    """
    Валидатор на проверку является ли организация заводом
    """
    def __call__(self, data):
        manufacturer = data.get('manufacturer')
        if manufacturer.node_type != 'Завод':
            raise ValidationError("Только заводы могут создавать продукты.")
