## Case Test #1:
Input: 
    Is portability important? (y/n): y
    Do you need long battery life? (y/n): y
    Budget (low/medium/high): high
    Will you use this laptop for gaming? (y/n): n
    Will you do creative work? (y/n): y
    Will you mainly do office work? (y/n): y
    Preferred OS (windows/macos/linux): macos
    Do you need AI acceleration? (y/n): n
    Do you want a large screen? (y/n): n 
    Do you travel often? (y/n): y

Expected Output: 
    Recommendations:
    - recommend:premium_ultrabook

    Specifications:
    - spec:macos_required
    - spec:ram_16_plus

    Fired Rules:
    - Premium Ultrabook
    - Creative Work (Portable)
    - MacOS Preference

## Case Test 2:
Input:
    Is portability important? (y/n): n
    Do you need long battery life? (y/n): y
    Budget (low/medium/high): high
    Will you use this laptop for gaming? (y/n): y
    Will you do creative work? (y/n): n
    Will you mainly do office work? (y/n): n
    Preferred OS (windows/macos/linux): windows
    Do you need AI acceleration? (y/n): n
    Do you want a large screen? (y/n): y
    Do you travel often? (y/n): n

Expected Output:
    Recommendations:
    - recommend:high_end_gaming_laptop

    Specifications:

    Fired Rules:
    - High-End Gaming Laptop

## Test Case 3:
Input:
    Is portability important? (y/n): y
    Do you need long battery life? (y/n): y
    Budget (low/medium/high): high
    Will you use this laptop for gaming? (y/n): n
    Will you do creative work? (y/n): y
    Will you mainly do office work? (y/n): y
    Preferred OS (windows/macos/linux): macos
    Do you need AI acceleration? (y/n): y
    Do you want a large screen? (y/n): y
    Do you travel often? (y/n): y

Expected Output:
    Recommendations:
    - recommend:premium_ultrabook

    Specifications:
    - spec:macos_required
    - spec:ram_16_plus
    - spec:gpu_with_tensor_cores

    Fired Rules:
    - Premium Ultrabook
    - Creative Work (Portable)
    - MacOS Preference
    - AI Acceleration