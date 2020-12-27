def generate(numRows):
    if numRows == 0:
        return []
    output = [[1]]
    if numRows == 1:
        return output
    i = 2
    input = [1]
    final_output = [[1]]
    while i <= numRows:
        o = [1] * i
        for j in range(1, len(o) - 1):
            o[j] = input[j - 1] + input[j]
        i += 1
        final_output.append(o)
        input = o
    return final_output


print(generate(5))