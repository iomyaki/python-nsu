def solve_quadratic_equation():
    print('Enter coefficients a, b, c of a quadratic equation ax^2 + bx + c = 0 (separated by a new line):')
    a, b, c = float(input()), float(input()), float(input())

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1, x2 = (-b + d ** .5) / (a * 2), (-b - d ** .5) / (a * 2)

        x1_print = int(x1) if x1 % 1 == .0 else x1
        x2_print = int(x2) if x2 % 1 == .0 else x2

        return f'Roots are {x1_print} and {x2_print}'

    elif d == 0:
        x0 = -b / (a * 2)

        x0_print = int(x0) if x0 % 1 == .0 else x0

        return f'The only root is {x0_print}'

    else:
        real, img = -b / (a * 2), abs((abs(d) ** .5) / (a * 2))

        real_print = int(real) if real % 1 == .0 else real  # to make roots like 2.0 -> 2
        img_print = int(img) if img % 1 == .0 else img

        if img == 1:
            return f'Roots are {real_print} + i and {real_print} - i'
        else:
            return f'Roots are {real_print} + {img_print}i and {real_print} - {img_print}i'


solve_quadratic_equation()
