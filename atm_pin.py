import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# ==========================================
# ATM PIN VERIFICATION USING DFA
# ==========================================

# Step 1: Define DFA states
states = ["q0", "q1", "q2", "q3", "q4", "qdead"]

start_state = "q0"
final_state = "q4"

# Step 2: Define input symbols
digits = "0123456789"

# Step 3: Define transition table
# DIGIT means any number from 0 to 9
# OTHER means alphabet or special character

transitions = {
    "q0": {"DIGIT": "q1", "OTHER": "qdead"},
    "q1": {"DIGIT": "q2", "OTHER": "qdead"},
    "q2": {"DIGIT": "q3", "OTHER": "qdead"},
    "q3": {"DIGIT": "q4", "OTHER": "qdead"},
    "q4": {"DIGIT": "qdead", "OTHER": "qdead"},
    "qdead": {"DIGIT": "qdead", "OTHER": "qdead"}
}


# Step 4: PIN validation function
def validate_pin(pin):

    current_state = start_state

    print("\nDFA State Transitions:")
    print("Initial State:", current_state)

    for character in pin:

        if character in digits:
            symbol = "DIGIT"
        else:
            symbol = "OTHER"

        current_state = transitions[current_state][symbol]

        print(character, "->", current_state)

    if current_state == final_state:
        return True
    else:
        return False


# Step 5: Test cases
print("================================")
print(" ATM PIN VERIFICATION USING DFA")
print("================================")

test_cases = ["1234", "5678", "123", "12345", "12A4", "abcd"]

print("\nTest Case Results:")

for pin in test_cases:

    if validate_pin(pin):
        print(pin, "- ACCEPTED")
    else:
        print(pin, "- REJECTED")


# Step 6: Get user input
pin = input("\nEnter your 4-digit ATM PIN: ")

if validate_pin(pin):
    print("\nPIN ACCEPTED")
    print("Valid 4-digit ATM PIN.")
else:
    print("\nPIN REJECTED")
    print("Invalid ATM PIN.")


# ==========================================
# STEP 7: DRAW DFA TRANSITION DIAGRAM
# ==========================================

fig, ax = plt.subplots(figsize=(15, 7))

# State positions
positions = {
    "q0": (0, 1),
    "q1": (1.7, 1),
    "q2": (3.4, 1),
    "q3": (5.1, 1),
    "q4": (6.8, 1),
    "qdead": (3.4, -1.2)
}

radius = 0.30

# Draw states
for state, (x, y) in positions.items():

    circle = Circle(
        (x, y),
        radius,
        facecolor="lightgreen" if state == final_state else
                  "lightcoral" if state == "qdead" else "lightblue",
        edgecolor="black",
        linewidth=2
    )

    ax.add_patch(circle)

    # Double circle for final state
    if state == final_state:
        inner_circle = Circle(
            (x, y),
            radius - 0.07,
            fill=False,
            edgecolor="green",
            linewidth=2
        )
        ax.add_patch(inner_circle)

    ax.text(
        x, y, state,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold"
    )


# Draw initial arrow
ax.annotate(
    "",
    xy=(-radius, 1),
    xytext=(-1.0, 1),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=2,
        color="black"
    )
)

ax.text(-1.0, 1.25, "START", fontsize=11)


# Step 8: Draw digit transitions
for i in range(4):

    source = f"q{i}"
    destination = f"q{i+1}"

    x1, y1 = positions[source]
    x2, y2 = positions[destination]

    arrow = FancyArrowPatch(
        (x1 + radius, y1),
        (x2 - radius, y2),
        arrowstyle="-|>",
        mutation_scale=20,
        linewidth=2,
        color="black"
    )

    ax.add_patch(arrow)

    # Display actual digits instead of DIGIT
    ax.text(
        (x1 + x2) / 2,
        y1 + 0.18,
        "0,1,2,3,4,5,6,7,8,9",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )


# Step 9: Invalid input transition to dead state
x1, y1 = positions["q2"]
x2, y2 = positions["qdead"]

invalid_arrow = FancyArrowPatch(
    (x1, y1 - radius),
    (x2, y2 + radius),
    arrowstyle="-|>",
    mutation_scale=20,
    linewidth=2,
    color="red",
    connectionstyle="arc3,rad=0.25"
)

ax.add_patch(invalid_arrow)

ax.text(
    3.85, -0.05,
    "OTHER\n(from every state)",
    fontsize=10,
    color="red",
    ha="left"
)


# Step 10: Dead state self-loop
x, y = positions["qdead"]

loop = FancyArrowPatch(
    (x - 0.15, y - 0.25),
    (x + 0.15, y - 0.25),
    arrowstyle="-|>",
    mutation_scale=18,
    linewidth=2,
    color="red",
    connectionstyle="arc3,rad=-2.5"
)

ax.add_patch(loop)

ax.text(
    x + 0.45, y - 0.35,
    "0-9, OTHER",
    fontsize=10,
    color="red"
)


# Step 11: Final diagram settings
ax.set_title(
    "ATM PIN VERIFICATION - DFA TRANSITION DIAGRAM",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax.text(
    6.8, 0.45,
    "FINAL STATE",
    ha="center",
    color="green",
    fontsize=10
)

ax.text(
    3.4, -1.85,
    "Qdead = Invalid input state",
    ha="center",
    fontsize=11,
    color="red"
)

ax.set_xlim(-1.2, 8)
ax.set_ylim(-2.2, 2)
ax.axis("off")

plt.tight_layout()

# Step 12: Save diagram
plt.savefig(
    "ATM_PIN_DFA.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDFA Transition Diagram Saved Successfully!")

plt.show()