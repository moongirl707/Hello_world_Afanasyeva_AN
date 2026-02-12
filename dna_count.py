dna=input("Введите последовательность ДНК: ").upper()
count_A= dna.count("A")
count_T= dna.count("T")
count_G= dna.count("G")
count_C= dna.count("C")
length=len(dna)
percent_A=(count_A/length)*100
percent_T=(count_T/length)*100
percent_G=(count_G/length)*100
percent_C=(count_C/length)*100
print("Подсчет нуклеотидов: ")
print(f"A: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"Общая длина: {length} нуклеотидов")
print("Процентное содержание каждого нуклеотида:")
print(f"A: {percent_A}%\nT: {percent_T}%\nG: {percent_G}%\nC: {percent_C}%")

#*Вывод персонального задания ENSG00000148604*
#Подсчет нуклеотидов:
#A: 497
#T: 677
#G: 486
#C: 561
#Общая длина: 2221 нуклеотидов
#Процентное содержание каждого нуклеотида:
#A: 22.377307519135524%
#T: 30.481764970733906%
#G: 21.882035119315624%
#C: 25.258892390814946%
