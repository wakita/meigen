#include<cstdlib>
#include<iostream>
#include<map>
#include<string>

#include <cnpy.h>

#include <magma_v2.h>
#include <magma_operators.h>

int main(int argc, char *argv[]) {
  magma_init();
  magma_print_environment();

  std::string cmd = argv[0];
  if (argc < 2) {
    std::cout << "Usage: " << cmd << " dataset" << std::endl;
    exit(1);
  }
  std::string dataset = argv[1];

  cnpy::NpyArray B = cnpy::npy_load("data/enron-B.npy");
  double* loaded_data = reinterpret_cast<double*>(B.data);
  std::cout << "data/enron-B: " << B.shape[0] << 'x' << B.shape[1] << std::endl;

  std::string path = "data/"; path.append(dataset); path.append("-B2.npy");
  unsigned int shape2[] = { B.shape[0], B.shape[1] };
  cnpy::npy_save(path, loaded_data, shape2, 2, "w");

  magma_finalize();
  B.destruct();
}
