import math
convert_list = [1, 2, 0.5, 0.25]
rad_2_deg = lambda x: [y*180/math.pi for y in x]
#rad_2_deg = lambda x: list(map(lambda y: y*180/math.pi, x))
print(rad_2_deg(convert_list))
