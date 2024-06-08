# Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох
# текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох
# видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням).
# На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.


import timeit


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def search_boyer_moore(text, pattern):
    # Реалізація алгоритму Боєра-Мура
    n = len(text)
    m = len(pattern)
    if m == 0:
        return -1, None

    last_occurrence = {}
    for i, char in enumerate(pattern):
        last_occurrence[char] = i

    skip = {}
    for i in range(256):  # Assuming ASCII characters
        skip[i] = m

    for i in range(m - 1):
        skip[ord(pattern[i])] = m - 1 - i

    i = m - 1
    j = m - 1
    comparisons = 0
    while i < n:
        comparisons += 1
        if text[i] == pattern[j]:
            if j == 0:
                return comparisons, i
            else:
                i -= 1
                j -= 1
        else:
            i += skip.get(ord(text[i]), m)
            j = m - 1

    return comparisons, None


def search_knuth_morris_pratt(text, pattern):
    # Реалізація алгоритму Кнута-Морріса-Пратта
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def search_rabin_karp(text, pattern):
    # Реалізація алгоритму Рабіна-Карпа
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    d = 256  # Розмір алфавіту
    q = 101  # Просте число

    p = 0  # Хеш для підрядка
    t = 0  # Хеш для поточного вікна тексту
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1


def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


article1_text = load_text('test_files/article1.txt')
article2_text = load_text('test_files/article2.txt')

pattern1 = "some_pattern_that_exists"
pattern2 = "some_random_pattern"

# Вимірюємо час виконання кожного алгоритму для підрядка, що існує в тексті
time_bm_exists = measure_time(search_boyer_moore, article1_text, pattern1)
time_kmp_exists = measure_time(search_knuth_morris_pratt, article1_text, pattern1)
time_rk_exists = measure_time(search_rabin_karp, article1_text, pattern1)

# Вимірюємо час виконання кожного алгоритму для вигаданого підрядка
time_bm_random = measure_time(search_boyer_moore, article1_text, pattern2)
time_kmp_random = measure_time(search_knuth_morris_pratt, article1_text, pattern2)
time_rk_random = measure_time(search_rabin_karp, article1_text, pattern2)

# Виведемо результати для першої статті
print("Алгоритм Боєра-Мура для підрядка, що існує в першій статті:", time_bm_exists)
print("Алгоритм Кнута-Морріса-Пратта для підрядка, що існує в першій статті:", time_kmp_exists)
print("Алгоритм Рабіна-Карпа для підрядка, що існує в першій статті:", time_rk_exists)
print("Алгоритм Боєра-Мура для вигаданого підрядка в першій статті:", time_bm_random)
print("Алгоритм Кнута-Морріса-Пратта для вигаданого підрядка в першій статті:", time_kmp_random)
print("Алгоритм Рабіна-Карпа для вигаданого підрядка в першій статті:", time_rk_random)

# Повторимо вимірювання для другої статті
time_bm_exists = measure_time(search_boyer_moore, article2_text, pattern1)
time_kmp_exists = measure_time(search_knuth_morris_pratt, article2_text, pattern1)
time_rk_exists = measure_time(search_rabin_karp, article2_text, pattern1)
time_bm_random = measure_time(search_boyer_moore, article2_text, pattern2)
time_kmp_random = measure_time(search_knuth_morris_pratt, article2_text, pattern2)
time_rk_random = measure_time(search_rabin_karp, article2_text, pattern2)

# Виведемо результати для другої статті
print("\nДля другої статті:")
print("Алгоритм Боєра-Мура для підрядка, що існує:", time_bm_exists)
print("Алгоритм Кнута-Морріса-Пратта для підрядка, що існує:", time_kmp_exists)
print("Алгоритм Рабіна-Карпа для підрядка, що існує:", time_rk_exists)
print("Алгоритм Боєра-Мура для вигаданого підрядка:", time_bm_random)
print("Алгоритм Кнута-Морріса-Пратта для вигаданого підрядка:", time_kmp_random)
print("Алгоритм Рабіна-Карпа для вигаданого підрядка:", time_rk_random)

# Тепер зробимо загальний висновок
avg_time_bm_exists = (time_bm_exists + time_bm_exists) / 2
avg_time_kmp_exists = (time_kmp_exists + time_kmp_exists) / 2
avg_time_rk_exists = (time_rk_exists + time_rk_exists) / 2
avg_time_bm_random = (time_bm_random + time_bm_random) / 2
avg_time_kmp_random = (time_kmp_random + time_kmp_random) / 2
avg_time_rk_random = (time_rk_random + time_rk_random) / 2

print("\nСередні часи для кожного алгоритму:")
print("Алгоритм Боєра-Мура:", avg_time_bm_exists)
print("Алгоритм Кнута-Морріса-Пратта:", avg_time_kmp_exists)
print("Алгоритм Рабіна-Карпа:", avg_time_rk_exists)
