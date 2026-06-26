import time

name = "itik"

duck = r"""
    __
 __(o )>
 \ <_. )
  `---'
"""

print("=" * 30)
print("WELCOME TO RTWH Gen 6")
print("=" * 30)

time.sleep(1)
print(duck)

message = f"Hello, my name is {name}"

for letter in message:
    print(letter, end="", flush=True)
    time.sleep(0.08)

print("\nQwack to meet you!")
