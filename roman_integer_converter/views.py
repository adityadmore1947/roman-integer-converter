# created manually
from django.http import HttpResponse
from django.shortcuts import render
from . import RomanNumerals

def index(request):
    return render(request, 'index.html')


def romanToInt(request):
    romanInput = request.GET.get('romanInput')
    romanNumerals = RomanNumerals.RomanNumerals()
    romanToInt = romanNumerals.from_roman(romanInput)

    params = {'function': 'output in number ', 'output':  romanToInt}
    return render(request, 'romanToInt.html', params)


def intToRoman(request):
    numberInput = int(request.GET.get('intToRoman'))
    intToRoman = RomanNumerals.RomanNumerals.to_roman(numberInput)

    params = {'function': 'output in roman', 'output': intToRoman}
    return render(request, 'intToRoman.html', params)