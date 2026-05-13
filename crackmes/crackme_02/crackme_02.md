# Crackme Analysis
## На начальном этапе провожу первичную проверку файла через VirusTotal для оценки потенциальной вредоносной активности, проверка производится как и в статике, так и динамике:
<img width="1846" height="665" alt="{37040A3A-DF7D-433B-81DA-D0D38711BF7C}" src="https://github.com/user-attachments/assets/79299f26-9d2d-4410-b44a-37cae4b5bccc" />
По результатам проверки большинство AV-движков не выявили признаков вредоносной активности. Один из движков пометил файл, что может быть связано с использованием анти-дебага

## Переходим к первичному осмотру бинарника через Detect It Easy:
<img width="768" height="525" alt="image" src="https://github.com/user-attachments/assets/76394757-5f27-447c-b67d-62b94e4ee66d" />
Ничего серьезного не наблюдаем, ни протектов, ни защиты.

## Переносим наш Бинарный файл в IDA Pro, и смотрим на ситуацию:
Как мы видим нас сразу встречает проверка на Дебаггер, которая реализуется через WinAPI функции IsDebuggerPresent, CheckRemoteDebuggerPresent
<img width="917" height="633" alt="{2BAC0187-142C-404F-9FA2-D7E4473DE679}" src="https://github.com/user-attachments/assets/003fc9f6-782f-4c75-a924-ed30e4197a71" />


После успешной проверки на дебаг - мы прыгаем в саму недрь программы:
<img width="1182" height="340" alt="{422921BC-0568-4753-B9AD-65F80A9F7B91}" src="https://github.com/user-attachments/assets/6485b334-b073-43bf-aa87-c6271f688215" />
<img width="1074" height="635" alt="{1738C560-0FBD-4C2F-B1E0-ECC0FC4721E7}" src="https://github.com/user-attachments/assets/1a21df00-7819-472c-acf5-ff9b78210f93" />

Нажимаем на Ф5, и смотрим декомпилерованную версию данного графа, нас встречает проверка логина и пароля с зашифрованной XOR`ом строками, которая имеет ключ 0x55:
<img width="880" height="674" alt="{E7A1104D-D58B-4612-86C9-BDEB38EF41D9}" src="https://github.com/user-attachments/assets/cb746b29-9fd8-41f0-9a43-c59790fa5b16" />

Решение довольно простое - Расшифровать имеющиеся XOR строки с ключом 0x55, для этого нам пригодится Python, пишем такой скрипт:
<img width="321" height="199" alt="{F07FA89F-4949-44FC-8E41-C17D53B4FE7E}" src="https://github.com/user-attachments/assets/62d04362-71db-46e5-abaa-486b9ba9abe4" />

На выходе получаем Login - secret, Password - bdhrlj.

CrackMe успешно решен.

# Вывод:
В процессе решения CrackMe были применены базовые техники reverse engineering:
- статический анализ в IDA Pro;
- анализ логики проверки данных;
- декодирование XOR-обфусцированных строк.
