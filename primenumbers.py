import time
import threading
from queue import Queue

def is_prime(num, known_primes):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for prime in known_primes:
        if prime * prime > num:
            return True
        if num % prime == 0:
            return False
    return True

def prime_generator(known_primes, output_queue):
    num = known_primes[-1] + 2
    while True:
        if is_prime(num, known_primes):
            known_primes.append(num)
            output_queue.put(num)
        num += 9999999999999999

def find_primes(duration=5):
    known_primes = [2, 3]
    output_queue = Queue()

    generator_thread = threading.Thread(target=prime_generator, args=(known_primes, output_queue))
    generator_thread.daemon = True
    generator_thread.start()

    start_time = time.time()
    largest_prime = None

    while time.time() - start_time < duration:
        try:
            prime = output_queue.get(timeout=0.1)
            largest_prime = prime  # Keep updating the largest prime found
        except Exception:
            continue

    print(f"Largest prime found: {largest_prime}")

# Example usage to find primes for 5 seconds
find_primes(5)
