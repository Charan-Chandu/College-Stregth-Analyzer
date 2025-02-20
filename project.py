
import matplotlib.pyplot as plt

def get_college_data():
    data = {}
    years = int(input("Enter the number of years of data: "))

    for _ in range(years):
        year = input("Enter  the year : ")
        data[year] = {}

        num_groups = int(input(f"Enter number of groups in {year}: "))
        for _ in range(num_groups):
            group_name = input("Enter the group name : ")
            section = input(f"Enter section for {group_name} : ")
            strength = int(input(f"Enter total strength of {group_name}-{section} in {year}: "))

         
            if group_name not in data[year]:
                data[year][group_name] = {}
            data[year][group_name][section] = strength 

    return data


def analyze_strength(data):
    year_strength = {}

    for year, groups in data.items():
        total_strength = sum(sum(sections.values()) for sections in groups.values())
        year_strength[year] = total_strength
    return year_strength


def give_suggestions(year_strength):
    years = sorted(year_strength.keys())
    for i in range(1, len(years)):
        if year_strength[years[i]] < year_strength[years[i-1]]:
            print(f"\n Strength decreased from {years[i-1]} to {years[i]}!")
            print(" Suggestions:")
            print("- Improve admission process")
            print("- Promote college through campaigns")
            print("- Improve infrastructure and faculty")
            print("- Introduce new courses and scholarships")


def plot_strength_graph(year_strength):
    years = list(year_strength.keys())
    strengths = list(year_strength.values())

    plt.figure(figsize=(8, 5))
    plt.plot(years, strengths, marker='o', linestyle='-', color='b', label="Total Strength")
    plt.xlabel("Year")
    plt.ylabel("Total Strength")
    plt.title("College Strength Analysis")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    college_data = get_college_data()
    year_strength = analyze_strength(college_data)
    give_suggestions(year_strength)
    plot_strength_graph(year_strength)
