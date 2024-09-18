#include <iostream>
#include <random>

void generate_binary()
{
    std::mt19937 gen(std::random_device{}());

    for (int i = 0; i < 128; ++i)
    {
        std::cout << gen() % 2;
    }
}

int main()
{
    generate_binary();
    return 0;
}
