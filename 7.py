def infix_to_rpn(expression: str) -> list:
    """
    Преобразует инфиксное выражение в обратную польскую нотацию (ОПН).
    Поддерживает унарный минус.
    """
    tokens = tokenize(expression)
    output = []
    stack = []

    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '~': 3}
    right_assoc = {'~'}

    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()  # убираем '('
        elif token in prec:
            while (
                stack and
                stack[-1] != '(' and
                stack[-1] in prec and
                (prec[stack[-1]] > prec[token] or
                 (prec[stack[-1]] == prec[token] and token not in right_assoc))
            ):
                output.append(stack.pop())
            stack.append(token)
        else:
            raise ValueError(f"Unknown token: {token}")

    while stack:
        if stack[-1] in ('(', ')'):
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output
import re

def tokenize(expr: str) -> list:

    expr = expr.replace(' ', '')
    if not expr:
        return []

    tokens = []
    i = 0
    while i < len(expr):
        char = expr[i]

        if char.isdigit() or char == '.':

            start = i
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            tokens.append(expr[start:i])
            continue
        elif char in '+-*/()':

            if char == '-':

                if not tokens or tokens[-1] in ('(', '+', '-', '*', '/'):
                    tokens.append('~')  # унарный минус
                else:
                    tokens.append('-')
            else:
                tokens.append(char)
            i += 1
        else:
            raise ValueError(f"Invalid character: {char}")

    return tokens

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
def evaluate_rpn(rpn: list) -> float:
    """
    Вычисляет значение выражения в обратной польской нотации.
    """
    stack = []
    for token in rpn:
        if is_number(token):
            stack.append(float(token))
        elif token == '~':
            if len(stack) < 1:
                raise ValueError("Insufficient operands for unary minus")
            a = stack.pop()
            stack.append(-a)
        elif token in '+-*/':
            if len(stack) < 2:
                raise ValueError(f"Insufficient operands for operator '{token}'")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                res = a / b
            stack.append(res)
        else:
            raise ValueError(f"Unknown token in RPN: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    return stack[0]
def calculate(expression: str) -> float:
    """Полный калькулятор: инфикс → ОПН → результат."""
    try:
        rpn = infix_to_rpn(expression)
        result = evaluate_rpn(rpn)
        return result
    except Exception as e:
        raise ValueError(f"Error evaluating expression '{expression}': {e}")
if __name__ == "__main__":
    test_expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "-5 + 3",
        "(-2) * 3",
        "10 / (2 + 3)",
        "-(2 + 3) * -4",
        "2.5 + 3.14",
        "100 / 4",
    ]

    for expr in test_expressions:
        try:
            rpn = infix_to_rpn(expr)
            result = evaluate_rpn(rpn)
            print(f"{expr:20} → ОПН: {rpn} → Результат: {result}")
        except Exception as e:
            print(f"{expr:20} → Ошибка: {e}")