def read_value(message):
    while True:
        try:
            value = float(eval(input(message), {"__builtins__": {}}, {}))
            if 0 <= value <= 1:
                return value
            print("Membership value must be between 0 and 1.")
        except:
            print("Enter a valid value like 1/2, 3/4 or 0.75.")


def input_sets():
    print("\nEnter Fuzzy Set Details")

    n = int(input("Enter number of elements in the universe: "))

    universe = []
    A = []
    B = []

    print("\nEnter universe elements:")
    for i in range(n):
        element = input("Element " + str(i + 1) + ": ")
        universe.append(element)

    print("\nEnter membership values for Set A:")
    for i in range(n):
        value = read_value("A(" + universe[i] + ") = ")
        A.append(value)

    print("\nEnter membership values for Set B:")
    for i in range(n):
        value = read_value("B(" + universe[i] + ") = ")
        B.append(value)

    return universe, A, B


def display_set(name, universe, values):
    print("\n" + name)
    print("-" * 35)

    for i in range(len(universe)):
        print(universe[i], ":", round(values[i], 3))


def display_matrix(name, matrix):
    print("\n" + name)
    print("-" * 40)

    for row in matrix:
        print(" ".join(f"{value:.3f}" for value in row))


def union(A, B):
    return [max(a, b) for a, b in zip(A, B)]


def intersection(A, B):
    return [min(a, b) for a, b in zip(A, B)]


def complement(A):
    return [1 - a for a in A]


def difference(A, B):
    return [min(a, 1 - b) for a, b in zip(A, B)]


def algebraic_sum(A, B):
    return [a + b - a * b for a, b in zip(A, B)]


def algebraic_product(A, B):
    return [a * b for a, b in zip(A, B)]


def bounded_sum(A, B):
    return [min(1, a + b) for a, b in zip(A, B)]


def bounded_difference(A, B):
    return [max(0, a - b) for a, b in zip(A, B)]


def all_operations(universe, A, B):
    print("\n----- ALL FUZZY SET OPERATIONS-----")

    display_set("Set A", universe, A)
    display_set("Set B", universe, B)

    display_set("Union (A U B)", universe, union(A, B))
    display_set("Intersection (A n B)", universe, intersection(A, B))
    display_set("Complement of A", universe, complement(A))
    display_set("Complement of B", universe, complement(B))
    display_set("Difference (A - B)", universe, difference(A, B))
    display_set("Difference (B - A)", universe, difference(B, A))
    display_set("Algebraic Sum", universe, algebraic_sum(A, B))
    display_set("Algebraic Product", universe, algebraic_product(A, B))
    display_set("Bounded Sum", universe, bounded_sum(A, B))
    display_set("Bounded Difference (A - B)", universe, bounded_difference(A, B))
    display_set("Bounded Difference (B - A)", universe, bounded_difference(B, A))

    print("\n----- DE MORGAN'S LAWS -----")

    left1 = complement(union(A, B))
    right1 = intersection(complement(A), complement(B))

    left2 = complement(intersection(A, B))
    right2 = union(complement(A), complement(B))

    display_set("Complement of Union", universe, left1)
    display_set("Intersection of Complements", universe, right1)
    print("First De Morgan's Law:", left1 == right1)

    display_set("Complement of Intersection", universe, left2)
    display_set("Union of Complements", universe, right2)
    print("Second De Morgan's Law:", left2 == right2)


def input_relation(name):
    print("\nEnter details for Relation", name)

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):
        row = []
        print("Enter values for row", i + 1)

        for j in range(cols):
            value = read_value("Enter value: ")
            row.append(value)

        matrix.append(row)

    return matrix


def max_min_composition():
    print("\n----- MAX-MIN COMPOSITION -----")

    R = input_relation("R")
    S = input_relation("S")

    if len(R[0]) != len(S):
        print("\nComposition is not possible.")
        print("Columns of R must equal rows of S.")
        return

    rows = len(R)
    cols = len(S[0])
    common = len(S)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            maximum = 0
            for k in range(common):
                minimum = min(R[i][k], S[k][j])
                maximum = max(maximum, minimum)
            row.append(maximum)
        result.append(row)

    display_matrix("Relation R", R)
    display_matrix("Relation S", S)
    display_matrix("Max-Min Composition (R o S)", result)


def max_product_composition():
    print("\n------ MAX-PRODUCT COMPOSITION ------")

    R = input_relation("R")
    S = input_relation("S")

    if len(R[0]) != len(S):
        print("\nComposition is not possible.")
        print("Columns of R must equal rows of S.")
        return

    rows = len(R)
    cols = len(S[0])
    common = len(S)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            maximum = 0
            for k in range(common):
                # Multiply instead of taking the minimum
                product = R[i][k] * S[k][j]
                maximum = max(maximum, product)
            row.append(maximum)
        result.append(row)

    display_matrix("Relation R", R)
    display_matrix("Relation S", S)
    display_matrix("Max-Product Composition (R . S)", result)


def main():
    print("------ FUZZY SET OPERATIONS -----")

    universe, A, B = input_sets()

    while True:
        print("\n------ MAIN MENU ------")
        print("1. Display A and B")
        print("2. Union (Maximum)")
        print("3. Intersection (Minimum)")
        print("4. Complement of A and B")
        print("5. Difference (A - B)")
        print("6. Difference (B - A)")
        print("7. Algebraic Sum")
        print("8. Algebraic Product")
        print("9. Bounded Sum")
        print("10. Bounded Difference")
        print("11. All Set Operations")
        print("12. Max-Min Composition")
        print("13. Max-Product Composition")
        print("14. Enter New Sets")
        print("15. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            display_set("Set A", universe, A)
            display_set("Set B", universe, B)

        elif choice == '2':
            display_set("Union (A U B)", universe, union(A, B))

        elif choice == '3':
            display_set("Intersection (A n B)", universe, intersection(A, B))

        elif choice == '4':
            display_set("Complement of A", universe, complement(A))
            display_set("Complement of B", universe, complement(B))

        elif choice == '5':
            display_set("Difference (A - B)", universe, difference(A, B))

        elif choice == '6':
            display_set("Difference (B - A)", universe, difference(B, A))

        elif choice == '7':
            display_set("Algebraic Sum", universe, algebraic_sum(A, B))

        elif choice == '8':
            display_set("Algebraic Product", universe, algebraic_product(A, B))

        elif choice == '9':
            display_set("Bounded Sum", universe, bounded_sum(A, B))

        elif choice == '10':
            display_set("Bounded Difference (A - B)", universe, bounded_difference(A, B))
            display_set("Bounded Difference (B - A)", universe, bounded_difference(B, A))

        elif choice == '11':
            all_operations(universe, A, B)

        elif choice == '12':
            max_min_composition()

        elif choice == '13':
            max_product_composition()

        elif choice == '14':
            universe, A, B = input_sets()

        elif choice == '15':
            print("\nProgram terminated.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
