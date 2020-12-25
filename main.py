from datetime import datetime, timedelta
class TransdimensionalParticleSplitter(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 6, 12)  # Set Start Date
        self.SetEndDate(DateTime.Now) # Set End Date
        self.SetCash(10000)  # Set Strategy Cash
        self.AddEquity("SPY", Resolution.Minute)
        
        # define our 15 minute trade bar consolidator. we can
        # access the 15 minute bar from the DataConsolidated events
        fifteenMinuteConsolidator = TradeBarConsolidator(timedelta(minutes=15))
        
        # attach our event handler. The event handler is a function that will
        # be called each time we produce a new consolidated piece of data.
        fifteenMinuteConsolidator.DataConsolidated += self.FifteenMinuteBarHandler

    def FifteenMinuteBarHandler(self, sender, bar):
        '''This is our event handler for our 15-minute trade bar defined above in Initialize(). 
        So each time the consolidator produces a new 15-minute bar, this function will be called automatically. 
        The sender parameter will be the instance of the IDataConsolidator that invoked the event '''
        self.Debug(str(self.Time) + " " + str(bar))

    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)