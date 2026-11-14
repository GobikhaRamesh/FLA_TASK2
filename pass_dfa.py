import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# ==========================================
# PASSWORD VERIFICATION USING DFA
# ==========================================

# Step 1: Define DFA states
states = ["q0", "q1", "q2", "qdead"]

initial_state = "q0"
final_state = "q2"
dead_state = "qdead"


# Step 2: Define character categories
def is_letter(ch):
    return ch.isalpha()


def is_digit(ch):
    return ch.isdigit()


# Step 3: Password validation using DFA
# Rules:
# 1. Password must start with a letter.
# 2. Password must contain at least one digit.
# 3. Password must end with a digit.
# 4. Only letters and digits are allowed.

def validate_password(password):

    current_state = initial_state

    for ch in password:

        if current_state == "q0":

            if is_letter(ch):
                current_state = "q1"
            else:
                current_state = dead_state

        elif current_state == "q1":

            if is_letter(ch):
                current_state = "q1"

            elif is_digit(ch):
                current_state = "q2"

            else:
                current_state = dead_state

        elif current_state == "q2":

            if is_digit(ch):
                current_state = "q2"

            elif is_letter(ch):
                current_state = "q1"

            else:
                current_state = dead_state

        elif current_state == dead_state:
            break

    return current_state == final_state


# Step 4: Test password examples
test_passwords = [
    "hello123",
    "student25",
    "abc123",
    "123456",
    "helloabc",
    "@123456",
    "welcome1",
    "password9",
    "123abc",
    "abc@123"
]

print("\nPASSWORD DFA VALIDATION RESULTS")
print("--------------------------------")

for password in test_passwords:

    if validate_password(password):
        print(password, "- ACCEPTED")
    else:
        print(password, "- REJECTED")


# Step 5: Draw DFA transition diagram
fig, ax = plt.subplots(figsize=(13, 8))

positions = {
    "q0": (1, 3),
    "q1": (4, 3),
    "q2": (7, 3),
    "qdead": (4, 0.5)
}


# Draw states
for state, (x, y) in positions.items():

    if state == final_state:
        color = "lightgreen"

    elif state == dead_state:
        color = "lightcoral"

    else:
        color = "lightblue"

    circle = Circle(
        (x, y),
        0.45,
        facecolor=color,
        edgecolor="black",
        linewidth=2
    )

    ax.add_patch(circle)

    # Double circle for final state
    if state == final_state:

        inner_circle = Circle(
            (x, y),
            0.36,
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


# Function to draw arrows
def draw_arrow(start, end, label, curve=0):

    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=20,
        linewidth=2,
        color="black",
        connectionstyle=f"arc3,rad={curve}"
    )

    ax.add_patch(arrow)

    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2

    ax.text(
        mid_x,
        mid_y + 0.25,
        label,
        ha="center",
        fontsize=11,
        fontweight="bold"
    )


# Initial arrow
draw_arrow(
    (0.15, 3),
    (0.53, 3),
    "START"
)

# Main transitions
draw_arrow(
    (1.5, 3),
    (3.5, 3),
    "Letter"
)

draw_arrow(
    (4.5, 3),
    (6.5, 3),
    "Digit"
)

# Letter transition from q2 back to q1
draw_arrow(
    (6.65, 3.25),
    (4.35, 3.25),
    "Letter",
    curve=-0.45
)


# Self-loop function
def draw_loop(x, y, label, color="blue"):

    loop = FancyArrowPatch(
        (x - 0.25, y + 0.25),
        (x + 0.25, y + 0.25),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.8,
        color=color,
        connectionstyle="arc3,rad=-1.6"
    )

    ax.add_patch(loop)

    ax.text(
        x,
        y + 0.95,
        label,
        ha="center",
        fontsize=10,
        color=color,
        fontweight="bold"
    )


# Self loops
draw_loop(4, 3, "Letter")
draw_loop(7, 3, "Digit")

# Invalid transitions to dead state
draw_arrow(
    (1.2, 2.6),
    (3.65, 0.9),
    "Invalid input",
    curve=0.15
)

draw_arrow(
    (4, 2.5),
    (4, 0.95),
    "Invalid input"
)

draw_arrow(
    (6.8, 2.6),
    (4.35, 0.9),
    "Invalid input",
    curve=-0.15
)

# Dead state loop
draw_loop(4, 0.5, "Any input", color="red")

# Final state label
ax.text(
    7,
    2.25,
    "FINAL STATE",
    ha="center",
    fontsize=11,
    color="green",
    fontweight="bold"
)

# Diagram title
plt.title(
    "PASSWORD VERIFICATION - DFA TRANSITION DIAGRAM",
    fontsize=15,
    fontweight="bold",
    pad=20
)

# Diagram settings
plt.xlim(-0.5, 8.5)
plt.ylim(-0.8, 5)
plt.axis("off")

plt.tight_layout()

# Save diagram
plt.savefig(
    "Password_DFA.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nPassword DFA Diagram Saved Successfully!")

# Step 6: Custom password testing
password = input("\nEnter a password to validate: ")

if validate_password(password):
    print("PASSWORD ACCEPTED")
else:
    print("PASSWORD REJECTED")