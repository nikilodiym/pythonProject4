countries = set()
add_country = set()
remove_country = set()
search_countries = set()
check_country = set()
while True:
    print("\nМеню:")
    print("1. Додати країну")
    print("2. Видалити країну")
    print("3. Пошук країн за символами")
    print("4. Перевірити наявність країни")
    print("5. Вийти")

    choice = input("Оберіть опцію (1-5): ")

    if choice == "1":
        country = input("Введіть назву країни, яку потрібно додати: ")
        countries.add(country)
    elif choice == "2":
        country = input("Введіть назву країни, яку потрібно видалити: ")
        countries.remove(country)
    elif choice == "3":
        query = input("Введіть символи для пошуку країн: ")
        seach = input("Введіть символ для пошуку країни: ")
        matching_countries = [c for c in countries if seach.lower() in c.lower()]
        if matching_countries:
            print(f"Знайдено країни які містять цей символ ")
            for country in matching_countries:
                print(country)
    elif choice == "4":
        country = input("Введіть назву країни для перевірки: ")
        if country in countries:
            print("True")
        else:
            print("False")
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Error")



#2
first = {"Київ", "Одеса", "Львів", "Харків", "Івано-Франківськ", "Запоріжжя"}
second = {"Львів", "Дніпро", "Івано-Франківськ", "Запоріжжя", "Одеса", "Харків"}
print(first | second)


#3
first = {"Київ", "Одеса", "Львів", "Харків", "Івано-Франківськ", "Запоріжжя"}
second = {"Львів", "Дніпро", "Івано-Франківськ", "Запоріжжя", "Одеса", "Харків"}
print(first - second)

#4
first = {"Київ", "Одеса", "Львів", "Харків", "Івано-Франківськ", "Запоріжжя"}
second = {"Львів", "Дніпро", "Івано-Франківськ", "Запоріжжя", "Одеса", "Харків"}
print(second - first)

#5
first = {"Київ", "Одеса", "Львів", "Харків", "Івано-Франківськ", "Запоріжжя"}
second = {"Львів", "Дніпро", "Івано-Франківськ", "Запоріжжя", "Одеса", "Харків"}
print(first ^ second)
#6
def sum_two_word(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    all_sumvol = set1.intersection(set2)

    result_str1 = ''.join(char for char in str1 if char not in all_sumvol)
    result_str2 = ''.join(char for char in str2 if char not in all_sumvol)

    result = result_str1 + result_str2

    return result

str1 = "hello"
str2 = "world"
result = sum_two_word(str1, str2)
print(result)
