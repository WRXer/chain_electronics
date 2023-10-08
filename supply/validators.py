import re
from rest_framework.exceptions import ValidationError

class SupplierValidator:
    """
    Валидатор на проверку поставщик-завод=организация производитель
    """
    def __call__(self, data):
        supplier = data.get('supplier')
        product = data.get('product')
        if supplier.node_type == 'Завод':
            if supplier != product.manufacturer:
                raise ValidationError("Поставщиком данного продукта может быть только организация-производитель.")


class PartnerValidator:
    """
    Валидатор на проверку разных организаций
    """
    def __call__(self, data):
        supplier = data.get('supplier')
        partner = data.get('partner')
        if supplier == partner:
            raise ValidationError("Организация не может быть одновременно поставщиком и заказчиком.")
