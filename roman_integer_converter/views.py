# created manually
from django.shortcuts import render
from . import RomanNumerals


def index(request):
    #render index page
    return render(request, 'index.html')


def romanToInt(request):
    # get input from number field
    romanInput = request.GET.get('romanInput')

    params = {'function': 'output in number- '}

    # Check if digit present
    hasDigit = False
    for char in romanInput:
        if char.isdigit():
            hasDigit = True
            break
    if hasDigit:
        params['output'] = "cannot be determined"
    else:
        try:
            romanToInt = RomanNumerals.RomanNumerals().from_roman(romanInput.upper())
            params['output'] = romanToInt
        except Exception as e:
            print("Something went wrong-", e)

    return render(request, 'romanToInt.html', params)


def intToRoman(request):

    # get number in string and convert it to number

    numberInput = int(request.GET.get('intToRoman'))

    intToRoman = RomanNumerals.RomanNumerals.to_roman(numberInput)
    params = {'function': 'output in roman', 'output': intToRoman}

    return render(request, 'intToRoman.html', params)
