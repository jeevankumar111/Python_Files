import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics",help="physics marks")
    parser.add_argument("--chemistry",help="chemistry marks")
    parser.add_argument("--maths",help="maths marks")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    print("Result:",(
        int(args.physics)+int(args.chemitry) + int(args.maths)
    )/3)
