def dice(outcomes):
    # Track current and longest sequence
    current_count = 1
    max_count = 1 
    
    for i in range(1, len(outcomes)):
        if outcomes[i] == outcomes[i - 1]:  # If current throw is the same as sequence
            current_count += 1      # Add to sequence length
        else:
            max_count = max(max_count, current_count)  # Update the maximum count
            current_count = 1  # Reset the counter
    
    max_count = max(max_count, current_count)
    return max_count


print(dice("5233165554211"))
print(dice("2133"))
