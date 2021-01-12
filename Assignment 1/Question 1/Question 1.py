#Create a Temperature Converter to perform ◦C = (5/9)×(◦F−32). Prompt user for temperature to convert and read the supplied value, perform the
#conversion and report the result.
deg = eval(input('Enter the temperature: '))
temp = 5/9*(deg - 32);
print("Convert velue", round(temp,2))
