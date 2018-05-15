from distutils.core import setup
from Cython.Build import cythonize
import numpy
 
setup(
	name = "Off Diagonal Coefficients code",
    ext_modules = cythonize("Coefficients.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
	name = "RHS Diagonal code",
    ext_modules = cythonize("rhs_diagonal.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
	name = "Gating Coefficients Step",
    ext_modules = cythonize("gating_coefficients.pyx"),
    include_dirs=[numpy.get_include()]
)
setup(
    name = "Gating Time Step",
    ext_modules = cythonize("gating_time_step.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
	name = "Sdodium",
    ext_modules = cythonize("h_sodium_inactivation.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
	name = "Sdodium Activation",
    ext_modules = cythonize("m_sodium_activation.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
	name = "Potassium Activation",
    ext_modules = cythonize("n_potassium_activation.pyx"),
    include_dirs=[numpy.get_include()]
)
setup(
	name = "Tridiagonal Solve",
    ext_modules = cythonize("Tridiagonal_Solver.pyx"),
    include_dirs=[numpy.get_include()]
)


setup(
    name = "linear Tridiagonal Solve",
    ext_modules = cythonize("linear_tridiagonal_solve.pyx"),
    include_dirs=[numpy.get_include()]
)

setup(
    name = "Main",
    ext_modules = cythonize("main_conv_std.pyx"),
    include_dirs=[numpy.get_include()]
)