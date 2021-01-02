import Grid

def main():
    x = Grid.GridBuilder()\
            .N(9)\
            .build()

    print(x.N, x.hooks)

if __name__ == "__main__":
    main()
