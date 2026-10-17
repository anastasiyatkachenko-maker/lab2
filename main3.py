def find_common_products(stores_list):
    if not stores_list:
        print("Немає даних про магазини.")
        return

    # Беремо асортимент першого магазину за основу (множина A)
    set_A = stores_list[0].copy()
    
    # Перетинаємо множину А з асортиментом кожного наступного магазину
    for store_set in stores_list[1:]:
        set_A = set_A & store_set  # Залишаються лише спільні товари

    # Друк результату на екран
    if set_A:
        print("\nМножина А (товари, які є в УСІХ магазинах):", set_A)
    else:
        print("\nСпільних товарів у всіх магазинах немає (порожня множина).")

# Загальний набір продуктових товарів n (для прикладу)
n_products = {"хліб", "молоко", "сир", "масло", "яблука", "кава", "чай"}
print("Доступний набір товарів:", n_products)

# Введення кількості магазинів m
m = int(input("Введіть кількість магазинів (m): "))

stores = []
for i in range(m):
    items = input(f"Введіть товари для магазину №{i + 1} через пробіл: ").lower().split()
    # Перетворюємо введений список товарів на множину
    store_assortment = set(items)
    stores.append(store_assortment)

# Виклик функції
find_common_products(stores)