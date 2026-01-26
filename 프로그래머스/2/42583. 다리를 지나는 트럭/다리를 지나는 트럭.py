from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    sum_bridge = 0
    
    while trucks:
        time += 1
        if bridge:
            sum_bridge -= bridge.popleft()
            bridge.append(0)
        
        if trucks and sum_bridge + trucks[0] <= weight:
            sum_bridge += trucks[0]
            bridge[-1] = trucks.popleft()
            
    while any(bridge):
        time += 1
        bridge.popleft()
        bridge.append(0)
    
        
    return time