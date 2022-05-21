# Patterns: Lightweight
12.2.2. Більшість автомобілів
складається з великої кількості деталей таких як двигун, колеса, кермо тощо.
Під час збірки автомобіля у нього встановлюють типові запчастини, що
повторюються у багатьох модифікаціях. Відповідно, програмуючи деяку гру чи
симулятор, що використовує подібні ієрархії класів можна суттєво заощадити
оперативну пам’ять та зменшити час створення об’єктів класу Car, якщо закешувати однакові деталі.
Нижче наведено просту ієрархію такого симулятора.

Приклад структури класів, написаної мовою
програмування Java та клієнтський код знаходиться за посиланням
github.com/krenevych/patterns/tree/main/Java/labs/lab12_Flyweight/task_2_2

Реалізуйте шаблон проектування Легковаговик для повторного
використання створених раніше об’єктів для різних частин автомобіля.