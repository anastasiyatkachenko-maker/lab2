# Просимо користувача ввести речення (повторюємо, поки не буде щонайменше 7 слів)
while True:
    sentence = input("Введіть речення (мінімум 7 слів): ")
    words = sentence.split()
    
    if len(words) >= 7:
        break
    print("Помилка! У реченні менше ніж 7 слів. Спробуйте ще раз.")

print("\nСлова, що закінчуються на 'ий':")
found = False

for word in words:
    # Очищуємо слово від можливих розділових знаків на кінцях
    clean_word = word.strip(".,!?;:\"'()")
    
    # Перевіряємо закінчення (переводимо в нижній регістр для точності)
    if clean_word.lower().endswith("ий"):
        print(clean_word)
        found = True

if not found:
    print("Таких слів у реченні немає.")