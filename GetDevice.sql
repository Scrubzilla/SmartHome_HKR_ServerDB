CREATE PROCEDURE GetDevice
  @Room_id INT = NULL

AS

BEGIN

SELECT Device_name FROM devices WHERE Room_id = @Room_id

  END