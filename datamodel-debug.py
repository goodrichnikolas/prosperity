import json
from typing import Dict, List
from json import JSONEncoder
import jsonpickle

# Type aliases for clarity and readability
Time = int
Symbol = str
Product = str
Position = int
UserId = str
ObservationValue = int

class Listing:
    def __init__(self, symbol: Symbol, product: Product, denomination: Product):
        self.symbol = symbol  # The symbol of the listing
        self.product = product  # The product being listed
        self.denomination = denomination  # The denomination of the listing

class ConversionObservation:
    def __init__(self, bidPrice: float, askPrice: float, transportFees: float, exportTariff: float, importTariff: float, sunlight: float, humidity: float):
        self.bidPrice = bidPrice  # The bid price for the conversion
        self.askPrice = askPrice  # The ask price for the conversion
        self.transportFees = transportFees  # The transport fees associated with the conversion
        self.exportTariff = exportTariff  # The export tariff for the conversion
        self.importTariff = importTariff  # The import tariff for the conversion
        self.sunlight = sunlight  # The sunlight factor for the conversion
        self.humidity = humidity  # The humidity factor for the conversion

class Observation:
    def __init__(self, plainValueObservations: Dict[Product, ObservationValue], conversionObservations: Dict[Product, ConversionObservation]) -> None:
        self.plainValueObservations = plainValueObservations  # Plain value observations for each product
        self.conversionObservations = conversionObservations  # Conversion observations for each product

    def __str__(self) -> str:
        return "(plainValueObservations: " + jsonpickle.encode(self.plainValueObservations) + ", conversionObservations: " + jsonpickle.encode(self.conversionObservations) + ")"

class Order:
    def __init__(self, symbol: Symbol, price: int, quantity: int) -> None:
        self.symbol = symbol  # The symbol of the order
        self.price = price  # The price of the order
        self.quantity = quantity  # The quantity of the order

    def __str__(self) -> str:
        return "(" + self.symbol + ", " + str(self.price) + ", " + str(self.quantity) + ")"

    def __repr__(self) -> str:
        return "(" + self.symbol + ", " + str(self.price) + ", " + str(self.quantity) + ")"

class OrderDepth:
    def __init__(self):
        self.buy_orders: Dict[int, int] = {}  # Dictionary mapping price to quantity for buy orders
        self.sell_orders: Dict[int, int] = {}  # Dictionary mapping price to quantity for sell orders

class Trade:
    def __init__(self, symbol: Symbol, price: int, quantity: int, buyer: UserId = None, seller: UserId = None, timestamp: int = 0) -> None:
        self.symbol = symbol  # The symbol of the trade
        self.price: int = price  # The price of the trade
        self.quantity: int = quantity  # The quantity of the trade
        self.buyer = buyer  # The buyer's user ID
        self.seller = seller  # The seller's user ID
        self.timestamp = timestamp  # The timestamp of the trade

    def __str__(self) -> str:
        return "(" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ", " + str(self.timestamp) + ")"

    def __repr__(self) -> str:
        return "(" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ", " + str(self.timestamp) + ")"

class TradingState(object):
    def __init__(self, traderData: str, timestamp: Time, listings: Dict[Symbol, Listing], order_depths: Dict[Symbol, OrderDepth], own_trades: Dict[Symbol, List[Trade]], market_trades: Dict[Symbol, List[Trade]], position: Dict[Product, Position], observations: Observation):
        self.traderData = traderData  # Data specific to the trader
        self.timestamp = timestamp  # The current timestamp
        self.listings = listings  # Dictionary mapping symbols to their respective listings
        self.order_depths = order_depths  # Dictionary mapping symbols to their order depths
        self.own_trades = own_trades  # Dictionary mapping symbols to the trader's own trades
        self.market_trades = market_trades  # Dictionary mapping symbols to market trades
        self.position = position  # Dictionary mapping products to the trader's positions
        self.observations = observations  # The current observations

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class ProsperityEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__  # Default encoding for Prosperity objects