import pycuda.driver as cuda
import pycuda.autoinit
import pycuda.compiler
import numpy

a = numpy.random.randn(4,4).astype(numpy.float32)
a_gpu = cuda.mem_alloc(a.nbytes)
cuda.memcpy_htod(a_gpu, a)

mod = pycuda.compiler.SourceModule("""
  ___global__ void doublify(float *a)
  {
    int idx = threadIdx.x + threadIdx.y*4;
    a[idx] *= 2;
  }
""")

func = mod.get_function("doublify")
func(a_gpu, block=(4,4,1))


print a
