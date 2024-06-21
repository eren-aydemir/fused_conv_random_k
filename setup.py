from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ['-std=c++14']

nvcc_args = [
    '-gencode', 'arch=compute_70,code=compute_70',
    '-gencode', 'arch=compute_80,code=compute_80'
]

setup(
    name="fused_conv_random_k",
    ext_modules=[
        CUDAExtension(
            "fused_conv_random_k_cuda",
            ["fused_conv_g.cpp", "fused_conv_go.cu"], 
            extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args})
    ],
    cmdclass={
        "build_ext": BuildExtension
    }
)
