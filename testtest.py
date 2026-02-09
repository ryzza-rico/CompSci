import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_HALF_UP

# to ensure that all 100 numbers of pi is read
getcontext().prec = 110 

# converting the ppi into string for accuracy
pi_string = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066"

# radius of the sphere
radius = Decimal("5")

def calculate_sphere_volume(pi_val, r):
    return (Decimal("4") / Decimal("3")) * pi_val * (r ** Decimal("3")) # formula for the volume of the sphere

# calculates the perfect volume using all 100 numbers
true_pi = Decimal(pi_string)
true_volume = calculate_sphere_volume(true_pi, radius)

intervals = [20, 40, 60, 100]
truncation_errors = []
rounding_errors = []

print("\n" + "="*120)
print(f"{'TRUNCATION RESULTS':^120}")
print("="*120)
print(f"{'Interval':<10} | {'Type':<12} | {'Volume (Truncated)':<25} | {'Error':<60}")
print("-" * 120)

for n in intervals:
    # for the truncated pi
    truncated_pi_str = pi_string[:2+n] 
    truncated_pi = Decimal(truncated_pi_str)
    
    vol_trunc = calculate_sphere_volume(truncated_pi, radius)
    err_trunc = abs(true_volume - vol_trunc)
    truncation_errors.append(err_trunc)
    
    print(f"{n:<10} | {'Truncation':<12} | {str(vol_trunc)[:20]}... | {err_trunc:.105f}")

print("\n" + "="*120)
print(f"{'ROUNDING RESULTS':^120}")
print("="*120)
print(f"{'Interval':<10} | {'Type':<12} | {'Volume (Rounded)':<25} | {'Error (Decimal Notation)':<60}")
print("-" * 120)

for n in intervals:
    # for the rounded pi
    rounded_pi = Decimal(pi_string).quantize(Decimal(f"1e-{n}"), rounding=ROUND_HALF_UP)
    
    vol_round = calculate_sphere_volume(rounded_pi, radius)
    err_round = abs(true_volume - vol_round)
    rounding_errors.append(err_round)

    print(f"{n:<10} | {'Rounding':<12} | {str(vol_round)[:20]}... | {err_round:.105f}")

# for the plotting of the graph
plt.figure(figsize=(10, 6))
plt.plot(intervals, truncation_errors, marker='o', linestyle='-', label='Truncation Error', color='red', linewidth=2)
plt.plot(intervals, rounding_errors, marker='s', linestyle='--', label='Rounding Error', color='blue', linewidth=2)

plt.yscale('log')
plt.title('Comparison of Truncation vs. Rounding Errors', fontsize=14, fontweight='bold')
plt.xlabel('Decimal Places (n)', fontsize=12)
plt.ylabel('Absolute Error', fontsize=12)
plt.xticks(intervals)
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()