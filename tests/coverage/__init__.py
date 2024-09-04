# # uncomment to use JAX backend for testing
# # TODO: switch between NumPy/SciPy and JAX
# import jax
# import jax.numpy as jnp
# import jax.scipy.linalg as jla
# import os
# import oqupy.config as oc
# import tensornetwork as tn
# jax.config.update('jax_enable_x64', True)
# oc.NUMERICAL_BACKEND_NUMPY = jnp
# oc.NumPyDtypeComplex = jnp.complex128
# oc.NumPyDtypeFloat = jnp.float64
# oc.NUMERICAL_BACKEND_LINALG = jla
# tn.set_default_backend('jax')
# os.environ['XLA_PYTHON_CLIENT_ALLOCATOR'] = 'platform'
# # os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '.5'