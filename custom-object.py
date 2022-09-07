#Jennifer Cruz Custom Object

class Purchase(object):
	def_init_(self, amount):
	self.amount = amount

	def calculateTax(self, taxPercent):
		return self.amount * taxPercent/100.0

	def calculateTip(self, tipPercent):
		return self.amount * tipPercent/100.0 #Jennifer Cruz

	def calculateTotal(self, taxPercent, tipPercent):
		return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

purchase = Purchase(100.0)

taxPercent = 7.5
tipPercent = 20.0 # Jennifer Cruz

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print ('Tax: ',tax)
print ('Tip: ',tip)
print ('Total:', purchase.calculateTotal(taxPercent, tipPercent)

#Jennifer Cruz
