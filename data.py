names_1 = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

names_2 = [
    ['Никита', 'Лев', 'Яков', 'Александра', 'Анна', 'Владимир', 'София', 'Василий', 'Полина', 'Дмитрий', 'Яков'],
    ['Лев', 'Анна', 'Екатерина', 'Виктория', 'Яков', 'Мадина', 'Елисей', 'Дмитрий', 'Яков', 'Ксения'],
    ['Марк', 'Виктория', 'Александр', 'Егор', 'Андрей', 'Агата', 'Владислава', 'Александра', 'Денис', 'Лев', 'Алиса']
]

names_3 = [
    ['Никита', 'Лев', 'Яков', 'Александра', 'Анна', 'Владимир', 'София', 'Василий', 'Полина', 'Дмитрий', 'Яков',
     'Александра', 'Александра'],
    ['Лев', 'Анна', 'Екатерина', 'Виктория', 'Яков', 'Мадина', 'Елисей', 'Дмитрий', 'Яков', 'Ксения', 'Александра'],
    ['Марк', 'Виктория', 'Александр', 'Егор', 'Александра', 'Андрей', 'Агата', 'Владислава', 'Александра', 'Денис',
     'Лев', 'Алиса']
]


courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]


expect_1_test_1 = [
    "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим",
    "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман",
    "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений",
    "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим",
    "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений",
    "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"
]

exp_col_2_test_1 = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
exp_col_2_test_2 = 'Яков: 4 раз(а), Лев: 3 раз(а), Александра: 2 раз(а)'
exp_col_2_test_3 = 'Александра: 6 раз(а), Яков: 4 раз(а), Лев: 3 раз(а)'

exp_col_3_test_1 = ('Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, '
       'Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, '
       'Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий')

exp_col_3_test_2 = ('Уникальные имена преподавателей: Агата, Александр, Александра, Алиса, Андрей, Анна, Василий, Виктория, '
       'Владимир, Владислава, Денис, Дмитрий, Егор, Екатерина, Елисей, Ксения, Лев, Мадина, Марк, Никита, Полина, '
       'София, Яков')

exp_col_3_test_3 = ('Уникальные имена преподавателей: Агата, Александр, Александра, Алиса, Андрей, Анна, Василий, Виктория, '
       'Владимир, Владислава, Денис, Дмитрий, Егор, Екатерина, Елисей, Ксения, Лев, Мадина, Марк, Никита, Полина, '
       'София, Яков')