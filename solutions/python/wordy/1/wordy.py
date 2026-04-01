def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    expression = question[8:-1].strip()

    if not expression:
        raise ValueError("syntax error")

    # Replace words
    expression = expression.replace("multiplied by", "*")
    expression = expression.replace("divided by", "/")
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")

    tokens = expression.split()

    # ✅ Special case: 2 tokens
    if len(tokens) == 2:
        try:
            int(tokens[0])
        except:
            raise ValueError("syntax error")

        if tokens[1] in {"+", "-", "*", "/"}:
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")

    # ❗ Must be odd length
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    # Validate pattern STRICTLY
    for i in range(len(tokens)):
        if i % 2 == 0:
            # must be number
            try:
                int(tokens[i])
            except:
                raise ValueError("syntax error")
        else:
            # must be operator
            if tokens[i] not in {"+", "-", "*", "/"}:
                raise ValueError("syntax error")  # 🔥 CHANGED HERE

    # Now check unknown operation separately
    for word in expression.split():
        if word not in {"+", "-", "*", "/"}:
            try:
                int(word)
            except:
                raise ValueError("unknown operation")

    # Calculate
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        op = tokens[i]
        value = int(tokens[i + 1])

        if op == "+":
            result += value
        elif op == "-":
            result -= value
        elif op == "*":
            result *= value
        elif op == "/":
            result //= value

    return result