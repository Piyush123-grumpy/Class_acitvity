#Time if went from bus
Bus_Speed=int(input("Enter the bus speed:"))
Distance_from_bus=int(input("Enter the distance from bus:"))
Minutes_bus_stopped=int(input("Enter the number of minutes bus stopped at stops:"))
Total_time_from_bus=Distance_from_bus/(Bus_Speed/60)+Minutes_bus_stopped
print(f'The time from bus is:',Total_time_from_bus,"Mins")

#Time from jogging
jogging_speed=int(input("Enter the jogging speed:"))
Jogging_distance=int(input("Enter the jogging distance:"))
jogging_time=Jogging_distance/(jogging_speed/60)
print(f'The time from jogging',jogging_time,"Mins")

#Time from running
Running_speed=int(input("Enter the running speed:"))
Running_distance=int(input("Enter the running distance:"))
Running_time=Running_distance/(Running_speed/60)
print(f'The time from running',Running_time,"Mins")
Total_time_from_running_and_jogging=Running_time+jogging_time
print(f"The total time from running and jogging",Total_time_from_running_and_jogging,"Mins")

if Total_time_from_bus>Total_time_from_running_and_jogging:
    Time=Total_time_from_bus-Total_time_from_running_and_jogging
    print("Running and jogging is quicker than bus by",Time,"Mins")
else :
    Time=Total_time_from_running_and_jogging-Total_time_from_bus
    print("Bus is quicker than running and jogging by",Time,"Mins")