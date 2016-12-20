CREATE PROCEDURE GetSensors
  @Device_id INT = NULL

AS

BEGIN

SELECT Sensor_type, Sensor_name FROM sensors WHERE Device_id = @Device_id

  END