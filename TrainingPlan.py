
# Marathon Training Plan Generator

weeks = int(input("How many weeks should the plan be? "))
starting_long_run = int(input("Starting long run mileage? "))

# Cycle of muscle groups
muscle_groups = ["Legs", "Shoulders", "Arms", "Chest", "Back"]

for week in range(1, weeks + 1):
    long_run = starting_long_run + week - 1

    # Pick muscle group (cycles through list)
    muscle = muscle_groups[(week - 1) % len(muscle_groups)]

    print(f"Week {week}:")
    print("- Easy run")
    print("- Tempo run")
    print(f"- Long run: {long_run} miles")
    print(f"- Weight training ({muscle})")
    print("- Yoga / mobility")
    print("- Rest day")
    print()
