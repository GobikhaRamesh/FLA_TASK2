import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# ==========================================
# EMAIL FORMAT VALIDATION USING DFA
# ==========================================

# Step 1: Define DFA states
states = ["q0", "q1", "q2", "q3", "q4", "q5", "qdead"]

initial_state = "q0"
final_state = "q5"
dead_state = "qdead"


# Step 2: Define character categories
def is_letter(ch):
    return ch.isalpha()

def is_digit(ch):
    return ch.isdigit()

def is_alphanumeric(ch):
    return ch.isalnum()


# Step 3: Email validation using DFA
def validate_email(email):

    current_state = initial_state

    for ch in email:

        if current_state == "q0":
            if is_alphanumeric(ch):
                current_state = "q1"
            else:
                current_state = dead_state

        elif current_state == "q1":
            if is_alphanumeric(ch) or ch in "._-":
                current_state = "q1"
            elif ch == "@":
                current_state = "q2"
            else:
                current_state = dead_state

        elif current_state == "q2":
            if is_alphanumeric(ch):
                current_state = "q2"
            elif ch == ".":
                current_state = "q3"
            else:
                current_state = dead_state

        elif current_state == "q3":
            if is_letter(ch):
                current_state = "q4"
            else:
                current_state = dead_state

        elif current_state == "q4":
            if is_letter(ch):
                current_state = "q5"
            else:
                current_state = dead_state

        elif current_state == "q5":
            if is_letter(ch):
                current_state = "q5"
            else:
                current_state = dead_state

        elif current_state == dead_state:
            break

    return current_state == final_state


# Step 4: Test email addresses
test_emails = [
    "abc@gmail.com",
    "user123@yahoo.in",
    "student@srm.edu",
    "test@outlook.com",
    "a1@college.edu",
    "abcgmail.com",
    "@gmail.com",
    "abc@.com",
    "abc@gmail",
    "abc@gmail.c"
]

print("\nEMAIL DFA VALIDATION RESULTS")
print("--------------------------------")

for email in test_emails:
    if validate_email(email):
        print(email, " - ACCEPTED")
    else:
        print(email, " - REJECTED")


# Step 5: Draw DFA transition diagram

fig, ax = plt.subplots(figsize=(15, 8))

positions = {
    "q0": (1, 3),
    "q1": (3, 3),
    "q2": (5, 3),
    "q3": (7, 3),
    "q4": (9, 3),
    "q5": (11, 3),
    "qdead": (5, 0.7)
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
        0.38,
        facecolor=color,
        edgecolor="black",
        linewidth=2
    )

    ax.add_patch(circle)

    # Double circle for final state
    if state == final_state:
        inner_circle = Circle(
            (x, y),
            0.30,
            fill=False,
            edgecolor="green",
            linewidth=2
        )
        ax.add_patch(inner_circle)

    ax.text(
        x, y, state,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold"
    )


# Function to draw arrows
def draw_arrow(start, end, label, curve=0):

    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.8,
        color="black",
        connectionstyle=f"arc3,rad={curve}"
    )

    ax.add_patch(arrow)

    # Transition label
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2

    ax.text(
        mid_x,
        mid_y + 0.22,
        label,
        ha="center",
        fontsize=10,
        fontweight="bold"
    )


# Initial arrow
draw_arrow((0.25, 3), (0.60, 3), "START")

# Main transitions
draw_arrow((1.4, 3), (2.6, 3), "L, D")
draw_arrow((3.4, 3), (4.6, 3), "@")
draw_arrow((5.4, 3), (6.6, 3), ".")
draw_arrow((7.4, 3), (8.6, 3), "L")
draw_arrow((9.4, 3), (10.6, 3), "L")


# Self-loop transitions
def draw_loop(x, y, label):

    loop = FancyArrowPatch(
        (x - 0.22, y + 0.22),
        (x + 0.22, y + 0.22),
        arrowstyle="-|>",
        mutation_scale=16,
        linewidth=1.6,
        color="blue",
        connectionstyle="arc3,rad=-1.7"
    )

    ax.add_patch(loop)

    ax.text(
        x,
        y + 0.95,
        label,
        ha="center",
        fontsize=9,
        color="blue",
        fontweight="bold"
    )


draw_loop(3, 3, "L, D, ., _, -")
draw_loop(5, 3, "L, D")
draw_loop(11, 3, "L")


# Invalid input transition to dead state
draw_arrow(
    (5, 2.6),
    (5, 1.1),
    "Invalid input"
)

# Dead state self-loop
draw_loop(5, 0.7, "All inputs")

# Final state label
ax.text(
    11,
    2.35,
    "FINAL STATE",
    ha="center",
    fontsize=10,
    color="green",
    fontweight="bold"
)

# Explanation
ax.text(
    5.5,
    -0.15,
    "L = Letter     D = Digit     "
    "@ = At symbol     . = Dot",
    ha="center",
    fontsize=11
)

# Diagram title
plt.title(
    "EMAIL FORMAT VALIDATION - DFA TRANSITION DIAGRAM",
    fontsize=15,
    fontweight="bold",
    pad=20
)

plt.xlim(-0.5, 12)
plt.ylim(-0.7, 5)
plt.axis("off")

plt.tight_layout()

# Step 6: Save diagram
plt.savefig(
    "Email_DFA.png",
    dpi=300,
    bbox_inches="tight"
)



print("\nDFA Transition Diagram Saved Successfully!")


# Step 7: Custom email testing
email = input("\nEnter an email address to validate: ")

if validate_email(email):
    print("EMAIL ACCEPTED")
else:
    print("EMAIL REJECTED")