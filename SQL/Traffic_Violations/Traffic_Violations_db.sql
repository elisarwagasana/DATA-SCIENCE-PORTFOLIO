Create database Traffic_Violations_Db;

#This code creates the drivers table in the database
CREATE TABLE Drivers
(driver_id SMALLINT UNSIGNED,
 driver_firstname VARCHAR(20),
 driver_lastname VARCHAR(20),
 driver_address VARCHAR(30),
 driver_licensenumber VARCHAR(20),
 driver_contact VARCHAR(20),
 drivers_TotalViolations VARCHAR(20),
 CONSTRAINT pk_drivers PRIMARY KEY (driver_id)
);

#This code creates the vehicles table in the database
CREATE TABLE Vehicles (
   vehicle_id SMALLINT UNSIGNED,
   vehicle_licenseplate VARCHAR(20),
   vehicle_color VARCHAR(20),
   vehicle_model VARCHAR(30),
   vehicle_make VARCHAR(20),
   vehicle_regnumber VARCHAR(20),
   vehicle_age VARCHAR(20),
   vehicle_mileage VARCHAR(20),
   driver_id SMALLINT UNSIGNED,
   CONSTRAINT pk_vehicles PRIMARY KEY (vehicle_id),
   CONSTRAINT fk_vehicles_driver_id FOREIGN KEY (driver_id)
       REFERENCES drivers (driver_id)
);

#This code creates the violations table in the database
CREATE TABLE Violations (
   violation_id INT UNSIGNED,
   driver_id SMALLINT UNSIGNED,
   vehicle_id SMALLINT UNSIGNED,
   violation_date DATE,
   violation_time TIME,
   violation_type VARCHAR(50),
   penalty DECIMAL(10, 2),
   violation_status VARCHAR(20),
   late_payment_fee DECIMAL(10, 2),
   CONSTRAINT pk_violations PRIMARY KEY (violation_id),
   CONSTRAINT fk_violations_driver_id FOREIGN KEY (driver_id)
       REFERENCES Drivers (driver_id),
   CONSTRAINT fk_violations_vehicle_id FOREIGN KEY (vehicle_id)
       REFERENCES Vehicles (vehicle_id)
);

#This code creates the officers table in the database
CREATE TABLE Officers (
   officer_id INT UNSIGNED PRIMARY KEY,
   vehicle_id SMALLINT UNSIGNED,
   violation_id INT UNSIGNED,
   officer_firstname VARCHAR(50),
   officer_lastname VARCHAR(50),
   total_violations INT,
   CONSTRAINT fk_officers_vehicle_id FOREIGN KEY (vehicle_id)
       REFERENCES Vehicles (vehicle_id),
   CONSTRAINT fk_officers_violation_id FOREIGN KEY (violation_id)
       REFERENCES Violations (violation_id)
);

#This code creates the DriverVehicles linking table in the database
CREATE TABLE DriverVehicles (
   DriverID SMALLINT UNSIGNED,
   VehicleID SMALLINT UNSIGNED,
   DriverFirstName VARCHAR(20),
   DriverLastName VARCHAR(20),
   VehicleMake VARCHAR(20),
   VehicleModel VARCHAR(30),
   PRIMARY KEY (DriverID, VehicleID),
   FOREIGN KEY (DriverID) REFERENCES Drivers(driver_id),
   FOREIGN KEY (VehicleID) REFERENCES Vehicles(vehicle_id)
);

#POPULATING THE TABLES:
#This code populates the drivers table
INSERT INTO Drivers (driver_id, driver_firstname, driver_lastname, driver_address, driver_licensenumber, driver_contact, drivers_TotalViolations)
VALUES
   (1, 'Mary', 'Becker', '123 Main St', 'ABC123', '123-500-7890', 1),
   (2, 'Ava', 'Smith', '456 Oak St', 'XYZ456', '987-654-6220', 1),
   (3, 'David', 'Johnson', '789 Pine St', 'LMN789', '555-123-4567', 1),
   (4,  'Tom', 'Carter', '987 Elm St', 'PQR321', '333-999-3880', 1),
   (5, 'Ellie', 'Smith', '500 Groove St', 'XRT760', '300-987-0932', 1);

#This code populates the Vehicles table
INSERT INTO Vehicles (vehicle_id, driver_id, vehicle_licenseplate, vehicle_color, vehicle_model, vehicle_make, vehicle_regnumber, vehicle_age, vehicle_mileage)
VALUES
   (1, 1,'ABC123', 'Blue', 'Model S', 'Tesla', 'ABC-123', 2, 20000),
   (2, 2, 'XYZ456', 'Red', 'C-Class', 'Mercedes Benz', 'XYZ-456', 3, 30000),
   (3, 3, 'LMN789', 'Black', 'X5', 'BMW', 'LMN-789', 1, 15000),
   (4, 4, 'PQR321', 'Silver', 'Accord', 'Honda', 'PQR-300', 4, 25000),
   (5, 5, 'DEF789', 'White', 'Wrangler', 'Jeep', 'DEF-789', 2, 18000);

#This code populates the officers table
INSERT INTO Officers (officer_id, vehicle_id, violation_id, officer_firstname, officer_lastname, total_violations)
VALUES
   (1, 1, 1, 'Lydia', 'Smith', 1),
   (2, 2, 2, 'Gilbert', 'Cooper', 1),
   (3, 3, 3, 'Will', 'Rodriguez', 1),
   (4, 4, 4, 'Emma', 'Johnson', 1),
   (5, 5, 5, 'Jorge', 'Brown', 1),
   (6, 1, 6, 'Sam', 'Rogers', 1);

#This code populates the violations table
INSERT INTO Violations (violation_id, driver_id, vehicle_id, officer_id, violation_date, violation_time, violation_type, penalty, violation_status, late_payment_fee)
VALUES
   (1, 1, 1, 1, '2023-11-25', '06:30:00', 'Speeding', 100.00, 'Unpaid', 0),
   (2, 2, 2, 2, '2023-11-25', '09:15:00', 'Running Red Light', 150.00, 'Unpaid', 0),
   (3, 3, 3, 3, '2023-11-25', '00:50:00', 'Improper Passing', 75.00, 'Paid', 0),
   (4, 4, 4, 4, '2023-11-26', '12:30:30', 'Seatbelt Violation', 50.00, 'Paid', 0),
   (5, 5, 5, 5, '2023-11-26', '01:05:00', 'Speeding', 100.00, 'Unpaid', 0),
   (6, 1, 1, 3, '2023-11-25', '08:30:00', 'Speeding', 100.00, 'Unpaid', 0);


#This code adds foreign keys to the drivers table
ALTER TABLE Drivers
ADD COLUMN vehicle_id SMALLINT UNSIGNED,
ADD COLUMN violation_id INT UNSIGNED;

ALTER TABLE Drivers
ADD CONSTRAINT fk_drivers_vehicle_id
FOREIGN KEY (vehicle_id)
REFERENCES Vehicles (vehicle_id);

ALTER TABLE Drivers
ADD CONSTRAINT fk_drivers_violation_id
FOREIGN KEY (violation_id)
REFERENCES Violations (violation_id);

#This code adds foreign keys to the vehicles table
ALTER TABLE Vehicles
ADD COLUMN violation_id INT UNSIGNED;

ALTER TABLE Vehicles
ADD CONSTRAINT fk_vehicles_violation_id
FOREIGN KEY (violation_id)
REFERENCES Violations (violation_id);

#This code adds foreign keys to the violations table
ALTER TABLE Violations
ADD COLUMN officer_id INT UNSIGNED;

ALTER TABLE Violations
ADD CONSTRAINT fk_violations_officer_id
FOREIGN KEY (officer_id)
REFERENCES Officers (officer_id);

#This codes updates foreign keys in the drivers table
UPDATE Drivers SET vehicle_id = (SELECT vehicle_id FROM Vehicles WHERE Vehicles.driver_id = Drivers.driver_id);
UPDATE Drivers SET violation_id = (SELECT violation_id FROM Violations WHERE Violations.driver_id = Drivers.driver_id);

#This codes updates foreign keys in the vehicles table
UPDATE Vehicles SET driver_id = (SELECT driver_id FROM Drivers WHERE Drivers.vehicle_id = Vehicles.vehicle_id);
UPDATE Vehicles SET violation_id = (SELECT violation_id FROM Violations WHERE Violations.vehicle_id = Vehicles.vehicle_id);

#This codes updates foreign keys in the officers table
UPDATE Officers SET vehicle_id = (SELECT vehicle_id FROM Vehicles WHERE Vehicles.vehicle_id = Officers.vehicle_id);
UPDATE Officers SET violation_id = (SELECT violation_id FROM Violations WHERE Violations.officer_id = Officers.officer_id);

#This codes updates foreign keys in the violations table
UPDATE Violations SET officer_id = (SELECT officer_id FROM Officers WHERE Officers.violation_id = Violations.violation_id);

#This code populates the drivervehicles linking table
INSERT INTO DriverVehicles (DriverID, VehicleID, DriverFirstName, DriverLastName, VehicleMake, VehicleModel)
VALUES
   (1, 1, 'Mary', 'Becker', 'Tesla', 'Model S'),
   (2, 2, 'Ava', 'Smith', 'Mercedes Benz', 'C-Class'),
   (3, 3, 'David', 'Johnson', 'BMW', 'X5'),
   (4, 4, 'Tom', 'Carter', 'Honda', 'Accord'),
   (5, 5, 'Ellie', 'Smith', 'Honda', 'Accord');

# This code creates a view that visualizes the total number of violations of each driver along with their names
CREATE VIEW TotalViolationsPerDriver AS
SELECT
    d.driver_id,
    d.driver_firstname,
    d.driver_lastname,
    COUNT(v.violation_id) AS total_violations
FROM
    Drivers d
LEFT JOIN Violations v ON d.driver_id = v.driver_id
GROUP BY
    d.driver_id, d.driver_firstname, d.driver_lastname;

#This code creates another view that displays information of each vehicle and their associated violations as well as corresponding drivers
CREATE VIEW VehicleViolation AS
SELECT
  v.vehicle_id,
  v.vehicle_licenseplate,
  v.vehicle_color,
  v.vehicle_model,
  v.vehicle_make,
  v.vehicle_regnumber,
  v.vehicle_age,
  v.vehicle_mileage,
  d.driver_id AS driver_id,
  d.driver_firstname,
  d.driver_lastname,
  vio.violation_id,
  vio.violation_date,
  vio.violation_time,
  vio.violation_type,
  vio.penalty,
  vio.violation_status,
  vio.late_payment_fee
FROM
  Vehicles v
LEFT JOIN
  Drivers d ON v.driver_id = d.driver_id
LEFT JOIN
  Violations vio ON v.vehicle_id = vio.vehicle_id;

#This code updates the total_violations field in the Drivers table
UPDATE Drivers
SET drivers_TotalViolations = (
 SELECT COUNT(*)
 FROM Violations
 WHERE Violations.driver_id = Drivers.driver_id
);

#This code updates the Late payment fee field in the Violations table based on the violation status and date
UPDATE Violations
SET late_payment_fee =
  CASE
    WHEN violation_status = 'Unpaid' AND DATEDIFF(NOW(), violation_date) <= 7 THEN 0.00  -- No late fee if a driver pays for unpaid violations within a week
    WHEN violation_status = 'Unpaid' AND DATEDIFF(NOW(), violation_date) > 7 THEN 100.00  -- $100 late fee for unpaid violations that goes beyond a week
    ELSE 0.00  -- No late fee for paid violations
  END;


