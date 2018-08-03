import sys


class LoanProcessor:

    def __init__(self, newLoan):
        self.currentAggregate = newLoan
        self.counter = 1

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
        self.counter += 1

    def getAggregateAmount(self):
        return self.currentAggregate.getAmount()

    def processNewLoan(self, newLoan, reducer=False):
        if(self.canBeAggregated(newLoan)):
            self.aggregate(newLoan)
        else:
            sys.stdout.write(self.displayCurrentAggregate(reducer) + '\n')
            self.updateInternalsWithNewLoanDetails(newLoan)
            # self.currentAggregate = newLoan

    def updateInternalsWithNewLoanDetails(self, newLoan):
        self.currentAggregate = newLoan
        self.counter = 1

    def displayCurrentAggregate(self, reducer=False):
        return(
            '{},{}'
            .format(
                self.currentAggregate.display(reducer),
                self.counter,
            )
        )
