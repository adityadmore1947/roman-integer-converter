# roman to int and vice versa

class RomanNumerals:
    @staticmethod
    def from_roman(s):
        X = [dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])

    @staticmethod
    def to_roman(i, o=' I II III IV V VI VII VIII IX'.split(' ')):
        r = lambda n: o[n]if n < 10 else''.join(dict(zip('IVXLC', 'XLCDM'))[c]for c in r(n//10))+o[n % 10]
        return r(i)


if __name__=="__main__":

    print("Roman to int test cases")
    assert RomanNumerals.from_roman("I") == 1
    assert RomanNumerals.from_roman("XI") == 11
    assert RomanNumerals.from_roman("XXI") == 21
    assert RomanNumerals.from_roman("MMMCMXCIX") == 3999

    print("Int to roman tests")
    assert RomanNumerals.to_roman(1)=="I"
    assert RomanNumerals.to_roman(11)=="XI"
    assert RomanNumerals.to_roman(21)=="XXI"
    assert RomanNumerals.to_roman(3999)=="MMMCMXCIX"
