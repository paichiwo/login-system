# Pet care tracker data types

## User Profile:
- Email: String (for authentication and communication)
- Password: String (securely hashed)
- 
## Pet Profile:
- Name: String
- Breed: String
- Weight: Float
- Age: Integer (in months or years)
- Medical History: String or Array of Strings (to store various medical records)

## Feeding Schedule:
- Time of Feeding: DateTime or Time
- Frequency: String or Enum (e.g., "Daily," "Twice a day," etc.)
- Pet(s) Associated: Array of references to Pet Profile(s)

## Medication Schedule:
- Medication Name: String
- Dosage: String or Float
- Frequency: String or Enum (e.g., "Once a day," "Twice a day," etc.)
- Time of Administration: DateTime or Time
- Pet(s) Associated: Array of references to Pet Profile(s)

## Appointment:
- Appointment Name/Title: String
- Date and Time: DateTime
-Location: String (address or description)
-Pet(s) Associated: Array of references to Pet Profile(s)

## Pet data
- Pet Name: String
- Breed: String
- Description: String
- Date Lost: DateTime
- Last Seen Location: String (address or description)
