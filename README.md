Посортований масив:
        Вставками -> 0.0000971
        Злиттям -> 0.0008482
        Рекурсивний TimSort -> 0.0006447
        Ітеративний TimSort -> 0.0004466
        Вбудованою функцією sorted -> 0.0000192
        Вбудованою функцією sort -> 0.0000133

Майже посортований масив:
        Вставками -> 0.0001393
        Злиттям -> 0.0009239
        Рекурсивний TimSort -> 0.0006242
        Ітеративний TimSort -> 0.0002927
        Вбудованою функцією sorted -> 0.0000168
        Вбудованою функцією sort -> 0.0000097

Посортований в зворотньому порядку масив:
        Вставками -> 0.0035461
        Злиттям -> 0.0008824
        Рекурсивний TimSort -> 0.0014694
        Ітеративний TimSort -> 0.0015476
        Вбудованою функцією sorted -> 0.0000218
        Вбудованою функцією sort -> 0.0000247

масив з рандомними значеннями:
        Вставками -> 0.0020489
        Злиттям -> 0.0011645
        Рекурсивний TimSort -> 0.0015140
        Ітеративний TimSort -> 0.0009820
        Вбудованою функцією sorted -> 0.0000340
        Вбудованою функцією sort -> 0.0000280

Масив з однаковими значеннями:
        Вставками -> 0.0000893
        Злиттям -> 0.0010580
        Рекурсивний TimSort -> 0.0005661
        Ітеративний TimSort -> 0.0002430
        Вбудованою функцією sorted -> 0.0000188
        Вбудованою функцією sort -> 0.0000112

Великий масив:
        Вставками -> 0.2154512
        Злиттям -> 0.0170339
        Рекурсивний TimSort -> maximum recursion depth exceeded
        Ітеративний TimSort -> 0.0145542
        Вбудованою функцією sorted -> 0.0007309
        Вбудованою функцією sort -> 0.0006459

Вижче наведені результати тестів різних алгоритмів сортування на різних типах масивів.

 Ми виявили, що сортування алгоритмом TimSort, який поєднує сортування злиттям та сортування вставками є більш ефективним, але не у всіх випадках. 

 Як ми бачимо посортований масив та масив з одинаковими значеннями шивдше виконуєься алгоритмом вставками, а метод злиттям є ефективнішим у випадку посортованого в зворотньому порядку масиву. 

 У випадку великого масиву рекурсивний TimSort дає помилку максимальноїглибини рекурсії. 
 Для сортування масивів з довільними значеннями та великих масивів алгоритм ітеративний TimSort показує кращі результати.

 Та у всх випадках вбудовані функції sorted та sort працюють найшвидше.
 
 Висновок: Варто виористовувати вбудовані функції сортування Python і не паритись :-)