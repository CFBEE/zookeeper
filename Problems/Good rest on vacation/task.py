duration_in_days = int(input())
food_cost_per_day = int(input())
flight_cost = int(input())
hotel_night = int(input())

print((flight_cost * 2)+(food_cost_per_day * duration_in_days)+(
  hotel_night * (duration_in_days - 1)))
