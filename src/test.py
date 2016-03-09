"""
    Tests C functions defined in shared library object cmath.so
"""

# Import cytypes and custom library
import ctypes as C

cmath = C.CDLL("./cmath.so")

# --------------------------------------------------------------
# Returning


# Set up API for returning functions
cmath.add_int.argtypes = [C.c_int, C.c_int]
cmath.add_int.restype = C.c_int

cmath.add_float.argtypes = [C.c_float, C.c_float]
cmath.add_float.restype = C.c_float

# Call returning functions
print "El resultado de add_int es {}.".format(cmath.add_int(3,4))
print "El resultado de add_float es {}.".format(cmath.add_float(3,4))

# ----------------------------------------------------------------------
# By-reference

# Set up variables
tresint = C.c_int(3)
cuatroint = C.c_int(4)
resint = C.c_int()

tresfloat = C.c_float(3)
cuatrofloat = C.c_float(4)
resfloat = C.c_float()

# Call by-reference functions
cmath.add_int_ref(C.byref(tresint), C.byref(cuatroint), C.byref(resint))
cmath.add_float_ref(C.byref(tresfloat), C.byref(cuatrofloat), C.byref(resfloat))

# Print results
print "El resultado de add_int_ref es {}.".format(resint.value)
print "El resultado de add_float_ref es {}.".format(resfloat.value)

#----------------------------------------------------------------------
# Arrays
# Set up variables
Ai = (C.c_int *3) (1, 2, -5)
Bi = (C.c_int *3) (-1, 3, 3)
dim = C.c_int(3)
addres = (C.c_int *3) (0, 0, 0)

Af = (C.c_float *3) (1, 2, -5)
Bf = (C.c_float *3) (-1, 3, 3)

# Define returning type
cmath.dot_product.restype = C.c_float

# Call by reference and print it
cmath.add_int_array(C.byref(Ai), C.byref(Bi), C.byref(addres), dim)
print "El resultado de add_int_array es ({},{},{})".format(addres[0], \
    addres[1], addres[2])

# Oneliner call returning and print
print "El resultado de dot_product es {}".format(cmath.dot_product(\
    C.byref(Af),C.byref(Bf), dim))

# --------------------------------------------------------------------
# Test
# holder = C.c_int(0)
# cmath.add_int_ref.argtypes = [C.byref(C.c_int), C.byref(C.c_int), \
#     C.byref(C.c_int)]
# cmath.add_int_ref(3,4,holder)
# print holder.value
