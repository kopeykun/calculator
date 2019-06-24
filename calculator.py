answer = "Ответ: "

print("Привет, я калькулятор, пожалуйста, введи два числа и выбери, что надо сделать с ними.")
print("")
final_question = input("Какую операцию Вы желаете провести? +, -, *, /: ")
first_question = int(input("Введи первое число: "))
second_question = int(input("Введи второе число: "))


if final_question == ("+"):
	add = first_question + second_question
	print (answer + str(add))
elif final_question == ("-"):
	sub = first_question - second_question
	print (answer + str(sub))
elif final_question == ("*"):
	mult = first_question * second_question
	print (answer + str(mult))
elif final_question == ("/"):
	div = first_question / second_question
	print (answer + str(div))
elif final_question != ("+", "-", "*", "/"):
	print("Просьба выбрать из предложенных операций.")

