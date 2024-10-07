# Prime Number Generator

This project implements a multithreaded prime number generator in Python. It efficiently finds prime numbers within a specified duration by using a generator function that continuously produces primes and stores them in a list. The largest prime found during the execution is displayed at the end.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Features

- Multithreaded implementation for efficient prime generation.
- Uses a list of known primes to check for new primes, optimizing the checking process.
- Finds the largest prime within a specified time limit.

## How It Works

1. **Prime Checking**: The `is_prime` function checks if a number is prime by testing divisibility against known primes and basic conditions (like checking if it's less than or equal to 1).
  
2. **Prime Generation**: The `prime_generator` function runs in a separate thread. It generates potential prime candidates and checks if they are prime using the `is_prime` function. If a number is found to be prime, it adds it to the known primes list and puts it in an output queue.

3. **Finding Primes**: The `find_primes` function initializes the prime generator and runs it for a specified duration, constantly updating the largest prime found.

## Usage

To use the prime number generator, simply call the `find_primes` function with the desired duration (in seconds) as an argument. For example, to find primes for 5 seconds:

```python
find_primes(5)
