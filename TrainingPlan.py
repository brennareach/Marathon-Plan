
## Marathon Training Plan Generator

weeks = int(input("How many weeks should the plan be? "))
starting_long_run = int(input("Starting long run mileage? "))

for week in range(1, weeks + 1):
    long_run = starting_long_run + week - 1

    print(f"Week {week}:")
    print("- Easy run")
    print("- Tempo run")
    print(f"- Long run: {long_run} miles")
    print("- Weight training")
    print("- Yoga / mobility")
    print("- Track Workout")
    print("- Rest day")
    print()
