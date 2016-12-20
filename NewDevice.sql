-- Stored Procedure for checking if add a new device is available.
-- Return 1 is ok
-- Return 0 is fail

CREATE PROCEDURE NewDevice
  @Device_name varchar(32) = null,
  @Room_id int = null

AS

BEGIN
INSERT INTO [dbo].[devices] (Device_name, Room_id) VALUES (@Device_name, @Room_id);

END

