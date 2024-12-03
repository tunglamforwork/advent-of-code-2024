import re


def process_instructions(input_string):
    mul_enabled = True  # Initially, mul is enabled
    total_sum = 0  # To accumulate the sum of results

    mul_pattern = r"mul\(\d+,\d+\)"  # To match mul(a,b)

    # Split the string into instructions using regex
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_string)
    print(instructions)

    # Process each instruction
    for inst in instructions:
        if inst == "do()":
            mul_enabled = True
        elif inst == "don't()":
            mul_enabled = False
        elif re.match(mul_pattern, inst) and mul_enabled:
            # Extract the operands from mul(a,b)
            numbers = re.findall(r"\d+", inst)
            num1, num2 = int(numbers[0]), int(numbers[1])
            total_sum += num1 * num2

    return total_sum


# Input string (corrupted memory)
with open("example.txt", "r") as file:
    input_string = file.read()

# Process and output the result
result = process_instructions(input_string)
print("Sum of results:", result)
