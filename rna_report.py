# day 4 of python recap: basic input and output 

# ask the user for their name
name = input(“Enter your name: “)

# print a greeting
print(f”Hello, {name}. Nice to meet you!”)

# ask for age
age = int(input(“Please enter your age: “))

# calculate the year the user was born
current_year = 2024
birth_year = current_year - age

# print the birth year
print(f”You were born in {birth_year}. “)

# output formatting with print()
sample_name = “RNA_Sample_001”
quality_score = 98.54

print(f”Sample Name: {sample_name}, Quality Score = {quality_score:.2f}.”)

# ask the user for sample information input
sample_name = input(“Enter the RNA sample name: “)
total_reads = int(input(“Enter the total number of reads: “))
good_reads = int(input(“Enter the number of good reads: “))
low_quality_reads = int(input(“Enter the number of low-quality reads: “))

# calculate the %
percentage_good = (good_reads / total reads) * 100 
percentage_low = (low_quality_reads / total reads) * 100 

try: 
	total_reads = int(input(“Enter the total number of reads: “))
	good_reads = int(input(“Enter the number of good reads: “))

	percentage_good = (good_reads / total reads) * 100 
	percentage_low = (low_quality_reads / total reads) * 100 

except ValueError:
	print(“Please enter valid integer values for the reads.”) 

# print a formatted report 
print(“\n—- RNA Sample Quality Report —-“)
print(f”Sample Name: {sample_name}”) 
print(f”Total reads: {total_reads}”)
print(f”Good reads: {good_reads} ({percentage_good:.2f}%)”) 
print(f”Low Quality Reads: {low_quality_reads ({percentage_low:.2f}%)”)

# check quality criteria aka giving the user feedback 
if percentage_good >= 90 and percentage_low <=5:
	print(“Result: Excellent sample quality!”)
elif percentage_good > =80: 
	print(“Result: Good sample quality.”)
else:
	print(“Result: Poor sample quality.”) 
