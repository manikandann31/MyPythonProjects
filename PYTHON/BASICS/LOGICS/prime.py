        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        num1 = 29
        print(f"{num1} is {'a prime number' if is_prime(num1) else 'not a prime number'}")

        num2 = 407
        print(f"{num2} is {'a prime number' if is_prime(num2) else 'not a prime number'}")
