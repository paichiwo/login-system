BEGIN TRANSACTION;

-- Create User Profile table
CREATE TABLE user_profile (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
);

-- Create Pet Profile table
CREATE TABLE pet_profile (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    breed VARCHAR(100),
    weight FLOAT,
    age INTEGER,
    medical_history TEXT[]
);

-- Create Feeding Schedule table
CREATE TABLE feeding_schedule (
    id SERIAL PRIMARY KEY,
    time_of_feeding TIMESTAMP,
    frequency VARCHAR(50),
    pet_ids INTEGER[] REFERENCES pet_profile(id)
);

-- Create Medication Schedule table
CREATE TABLE medication_schedule (
    id SERIAL PRIMARY KEY,
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    time_of_administration TIMESTAMP,
    pet_ids INTEGER[] REFERENCES pet_profile(id)
);

-- Create Appointment table
CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    appointment_name VARCHAR(100) NOT NULL,
    date_and_time TIMESTAMP,
    location VARCHAR(200),
    pet_ids INTEGER[] REFERENCES pet_profile(id)
);

