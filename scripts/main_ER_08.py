from src.attack import *
from src.create import *
from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N8000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn8000k4 = generate_pinf_ER(8000, 4, 10)
np.savetxt('./notebooks/results/1012/ERn8000k4.csv', ERn8000k4, delimiter=',')
