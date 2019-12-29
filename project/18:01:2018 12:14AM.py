class messages():
  

# this function just print a secret message to the console
  def secretMsg(self):
    print("You have found the secret message!!")
#------------------------------------------------------
    

# this function is to calculate bmi using meters and
# kilograms
  def bmi_calc_meters(self, weight, height):
    bmi = weight / height ^ 2
    return bmi
#------------------------------------------------------
  
  
# this function is to calculate bmi using feet and lbs
  def bmi_calc_feet(self, weight, height):
    bmi = 703 * weight / height ^ 2
    return bmi
#------------------------------------------------------
