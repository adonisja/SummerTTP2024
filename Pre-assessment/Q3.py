def main():
    heights = {"Robert Downey Jr.": 175.26, "Chris Evans": 182.88,
                  "Mark Ruffalo": 172.72, "Chris Hemsworth": 190.50,
                  "Scarlett Johansson": 160.02, "Tom Hiddleston": 187.96,
                  "Cobie Smulders": 172.72, "Samuel L. Jackson": 187.96,
                  "Clark Gregg": 175.26, "Stellan Skarsgård": 190.50,
                  "Jeremy Renner": 175.26}
    short = 200
    shortest = ""
    for key, value in heights.items():  
        if value < short:
            shortest = key
            short = value
    print(shortest)

if __name__ == "__main__":
    main()