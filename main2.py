def sort_prime(num):
    prime_num1 = []
    prime_num2 = [True] * (num + 1)
    for i in range(2, num + 1):
        if prime_num2[i]:
            prime_num1.append(i)
            for j in range(2, int(num / i) + 1):
                prime_num2[i * j] = False
    return prime_num1


sort_prime(150)
