#include <array>

int add(int i, int j) { return i + j; }

int segfault(int idx) {
  auto arr = std::array<int, 2>{ 1, 2 }; 
  return arr[idx]; 
}
