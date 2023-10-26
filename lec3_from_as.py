from lec3_my_module import earth_mass as em 
from lec3_my_module import graviti_constant as G 
from lec3_my_module import sigma_steff_bolc as sigma 

g=500*G/10**2
print(g)

x=em*g*sigma 
print(x)