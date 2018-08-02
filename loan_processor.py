class LoanProcessor:

    def __init__(self, newLoan):
        self.currentAggregate = newLoan

    def canBeAggregated(self, newLoan):
        ans = False
        if(
            self.currentAggregate.getNetwork() == newLoan.getNetwork()
            and self.currentAggregate.getProduct() == newLoan.getProduct()
            and self.currentAggregate.getMonth() == newLoan.getMonth()
        ):
            ans = True
        return ans

    def aggregate(self, newLoan):
        self.currentAggregate.updateAmount(newLoan.getAmount())

    def getAggregateAmount(self):
        return self.currentAggregate.getAmount()

    def processNewLoan(self, newLoan):
        if(self.canBeAggregated(newLoan)):
            self.aggregate(newLoan)
        else:
            print(self.currentAggregate.display())
            self.currentAggregate = newLoan
