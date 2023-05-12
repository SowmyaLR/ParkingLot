# ParkingLot Problem Statement
Given a parking lot with details about the vehicle types that can be parked, the number of
spots, and the fee model for the parking lot; compute the fees to be paid for the parked
vehicles when the vehicle is unparked.


# Commands used in this solution

1. SET_PLACE <mall|stadium|airport>
2. SET_CAPACITY <scooter|truck|car> <number>
3. PARK <scooter|truck|car> <entry_time in YYYY-MM-DD HH:MM:SS.ns>
4. UNPARK <scooter|truck|car> <ticket_no> <exit_time in YYYY-MM-DD HH:MM:SS.ns>
  
  Sample test case: <a href="https://github.com/SowmyaLR/ParkingLot/blob/parkinglot/inputs/case1">Case1</a>
  

 # Prerequisites
  Before running this solution make sure that python version above 3.9 is installed in your system
# Execution steps
  1. Clone this repo
  2. Navigate to the root directory ie.parkinglot
  3. Execute <b> python3 -m main <input_file_path> </b>
  4. To check for sample cases unit tests are written under tests package using unittest of python3.
  For quick test those test suits can be used
  
 # Coverage test file report
  
  <img width="1437" alt="Screenshot 2023-05-12 at 9 54 12 AM" src="https://github.com/SowmyaLR/ParkingLot/assets/15843240/df3b26b0-7523-4695-99f9-73835da89074">
