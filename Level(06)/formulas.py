def formulas(question):
    if question == "V":
        R=float(input("what is resistance value? "))
        I=float(input("what is I value? "))
        V=float(R*I)
        return print(V)
    elif question == "R":
        V=float(input("what is volt value? "))
        I=float(input("what is I value? "))
        R=float(V/I)
        return print(R)
    elif question == "I":
        question2=input("which datas you have?(write q and t or V and R) ")
        if question2 == "q and t":
            q=float(input("what is q value? "))
            t=float(input("what is t value? "))
            I=q/t
            return print(I)
        elif question2 == "V and R":
            V=float(input("what is Volt value?"))
            R=float(input("what is Resistance value?"))
            I=V/R
            return print(I)
        else:
            print("value is not correct.")
    else:
        print("This value is not valid.")
              