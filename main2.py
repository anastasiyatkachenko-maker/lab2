def add_odd_index_elements(lst):
    # Вибираємо елементи з непарними індексами (1, 3, 5...)
    odd_elements = lst[1::2]
    
    # Доповнюємо список у кінці цими елементами
    lst.extend(odd_elements)
    
    # Друкуємо результуючий список на екран
    print("Результуючий список:", lst)

# Введення списку з клавіатури через пробіл
user_input = input("Введіть елементи списку через пробіл: ")
my_list = user_input.split()

# Виклик функції
add_odd_index_elements(my_list)