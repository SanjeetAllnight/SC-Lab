"""McCulloch-Pitts implementation of three-input logic gates.

Activation rule:
    output = 1, if sum(x_i * w_i) >= threshold
             0, otherwise
"""


def mcp_neuron(inputs, weights, threshold):
    """Return the output and weighted sum of one McCulloch-Pitts neuron."""
    if len(inputs) != len(weights):
        raise ValueError("The number of inputs and weights must be the same.")

    weighted_sum = sum(x * w for x, w in zip(inputs, weights))
    output = int(weighted_sum >= threshold)
    return output, weighted_sum


# Default weight and threshold values for three-input gates.
# Negative thresholds are valid here because the activation rule is >= threshold.
DEFAULT_PARAMETERS = {
    "AND": ((1, 1, 1), 3),
    "OR": ((1, 1, 1), 1),
    "NAND": ((-1, -1, -1), -2.5),
    "NOR": ((-1, -1, -1), -0.5),
}


def xor_gate(inputs):
    """Return x1 XOR x2 XOR x3 using a small MCP network.

    A single MCP neuron cannot implement XOR, so three hidden neurons detect
    whether at least 1, 2, or 3 inputs are 1.  The output neuron produces 1
    when the number of 1s is odd (one or three).
    """
    hidden_1, _ = mcp_neuron(inputs, (1, 1, 1), 1)  # at least one 1
    hidden_2, _ = mcp_neuron(inputs, (1, 1, 1), 2)  # at least two 1s
    hidden_3, _ = mcp_neuron(inputs, (1, 1, 1), 3)  # all three are 1

    output, weighted_sum = mcp_neuron(
        (hidden_1, hidden_2, hidden_3), (1, -1, 1), 0.5
    )
    return output, weighted_sum, (hidden_1, hidden_2, hidden_3)


def read_bit(name):
    """Read one binary input from the user."""
    while True:
        value = input(f"Enter {name} (0 or 1): ").strip()
        if value in ("0", "1"):
            return int(value)
        print("Please enter only 0 or 1.")


def read_parameters(gate_name, default_weights, default_threshold):
    """Use default gate parameters, or let the user enter w1, w2, w3, theta."""
    print(
        f"\n{gate_name} default: w1, w2, w3 = {default_weights}; "
        f"threshold = {default_threshold}"
    )
    use_default = input("Use these values? (Y/n): ").strip().lower()
    if use_default in ("", "y", "yes"):
        return default_weights, default_threshold

    weights = []
    for weight_name in ("w1", "w2", "w3"):
        weights.append(float(input(f"Enter {weight_name}: ")))
    threshold = float(input("Enter threshold: "))
    return tuple(weights), threshold


def main():
    print("McCulloch-Pitts Model: AND, OR, NAND, NOR and XOR (3 inputs)")
    print("Activation: output = 1 when weighted sum >= threshold\n")

    inputs = (read_bit("x1"), read_bit("x2"), read_bit("x3"))
    print(f"\nInputs: x1, x2, x3 = {inputs}")

    for gate_name, (default_weights, default_threshold) in DEFAULT_PARAMETERS.items():
        weights, threshold = read_parameters(
            gate_name, default_weights, default_threshold
        )
        output, weighted_sum = mcp_neuron(inputs, weights, threshold)
        print(
            f"{gate_name}: sum = {weighted_sum:g}, threshold = {threshold:g}, "
            f"output = {output}"
        )

    xor_output, xor_sum, hidden_outputs = xor_gate(inputs)
    print("\nXOR uses a multi-neuron MCP network (a single threshold neuron cannot do XOR).")
    print("Hidden outputs (at least 1, at least 2, at least 3) =", hidden_outputs)
    print("XOR output layer: weights = (1, -1, 1), threshold = 0.5")
    print(f"XOR: sum = {xor_sum:g}, output = {xor_output}")


if __name__ == "__main__":
    main()
