
from datamodel import OrderDepth, UserId, TradingState, Order, ConversionObservation
from typing import List
import string
import time

class Trader:
    def run(self, state: TradingState):

        #Measure the time it takes to run the trader
        start = time.time()

        # Initialize an empty dictionary to store the orders for each product
        result = {}
        
        # Iterate over each product in the order depths
        for product in state.order_depths:
            # Check if the product exists in conversionObservations
            if product in state.observations.conversionObservations:
                conversionObservation = state.observations.conversionObservations[product]
                # Print them off for json friendly output
                transportFees = conversionObservation.transportFees
                exportTariff = conversionObservation.exportTariff
                importTariff = conversionObservation.importTariff
                sunlight = conversionObservation.sunlight
                humidity = conversionObservation.humidity


                print("Transport Fees: " + str(transportFees))
                print("Export Tariff: " + str(exportTariff))
                print("Import Tariff: " + str(importTariff))
                print("Sunlight: " + str(sunlight))
                print("Humidity: " + str(humidity))
            else:
                print(f"No conversion observations found for product: {product}")

                #Print off what it does say though
                print("Conversion Observations: " + str(state.observations.conversionObservations))
                    
                # Get the order depth for the current product
                order_depth: OrderDepth = state.order_depths[product]
                
                #Json friendly
                print("Order Depth: " + str(order_depth.buy_orders))
                
                # Initialize an empty list to store the orders for the current product
                orders: List[Order] = []
            
            # Check if there are any sell orders for the current product
            if len(order_depth.sell_orders) != 0:
                # Get the best (lowest) ask price and the amount available at that price
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                # Append the information to the orders list
                #orders.append(Order(product, best_ask, best_ask_amount))
            
            # Check if there are any buy orders for the current product
            if len(order_depth.buy_orders) != 0:
                # Get the best (highest) bid price and the amount available at that price
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                # Append the information to the orders list
                #orders.append(Order(product, best_bid, best_bid_amount))
            
            # Store the orders for the current product in the result dictionary
            result[product] = orders
        
        # Set some sample trader data and the number of conversions
        traderData = "SAMPLE"
        conversions = 1

        #End
        elapsed_time_ms = (time.time() - start) * 1000

        print(f"Trader took {elapsed_time_ms} ms to run")
        
        # Return the result dictionary, the number of conversions, and the trader data
        return result, conversions, traderData