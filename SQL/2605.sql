SELECT products.name, providers.name from products
LEFT JOIN providers on products.id_providers = providers.id
WHERE products.id_categories = 6;