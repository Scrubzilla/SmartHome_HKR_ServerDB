CREATE PROCEDURE NewSensors
  @Sensor_type varchar(32) = null,
  @Device_id int = null,
  @Sensor_name varchar(32) = null

AS

BEGIN
INSERT INTO [dbo].[sensors] (Sensor_type, Device_id, Sensor_name) VALUES (@Sensor_type, @Device_id, @Sensor_name);

END