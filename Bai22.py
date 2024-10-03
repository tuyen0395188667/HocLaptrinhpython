a = int(input())
total = int(input())
def Assignment_Operator(a,total):
    total += a # Using += Operator
    print("The Value of the Total after using += Operator is:", total)
    total -= a # Using -= Operator
    print("The Value of the Total after using -= Operator is:", total)
    total *= a # Using *= Operator
    print("The Value of the Total after using *= Operator is:", total)
    total //= a # Using //= Operator
    print("The Value of the Total after using //= Operator is:", total)
    total **= a # Using **= Operator
    print("The Value of the Total after using **= Operator is:", total)
    total /= a # Using /= Operator
    print("The Value of the Total after using /= Operator is:", total)
    total %= a # Using %= Operator
    print("The Value of the Total after using %= Operator is:", total)
Assignment_Operator(a,total)