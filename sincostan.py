import math
def factorial(n):
    if n==0:
        return 1
    else:
        return n *factorial(n-1)
def sine_series(x,terms=10):
    sine_sum=0
    for n in range(terms):
        sign= (-1)**n
        sine_sum += sign*(x**(2*n+1))/factorial(2*n+1)
        return sine_sum
def cosine_series(x,terms=10):
    cosine_sum=0
    for n in range(terms):
        sign= (-1)**n
        cosine_sum += sign*(x**(2*n))/factorial(2*n)
        return cosine_sum
def tangent_series(x,terms=10):
    sin_val=sine_series(x,terms)
    cos_val=cosine_series(x,terms)
    if cos_val==0:
        return float('inf')
    return sin_val/cos_val

degrees=30
radians=math.radians(degrees)

sin_val=sine_series(radians)
cos_val=cosine_series(radians)
tan_val=tangent_series(radians)

print(f"sine({degrees}°)approx:{sin_val}")
print(f"cosine({degrees}°)approx:{cos_val}")
print(f"tangent({degrees}°)approx:{tan_val}")

print(f"\nActual math.sin({degrees}°):{math.sin(radians)}")
print(f"Actual math.cos({degrees}°):{math.cos(radians)}")
print(f"Actual math.tan({degrees}°):{math.tan(radians)}")
