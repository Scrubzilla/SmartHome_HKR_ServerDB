-- Stored Procedure for checking if add a new device is available.
-- Return 1 is ok
-- Return 0 is fail

CREATE PROCEDURE NewDevice
  @Device_name varchar(32) = null,
  @Room_name varchar(32) = null,
  @Server_name varchar(32) = null,
  @Variable_of_device varchar(32) = null
  --@Room_id int = [dbo].[rooms](Room_id)

AS

  IF EXISTS(SELECT * FROM [homeserver] WHERE Server_name = @Server_name)
  BEGIN
       IF EXISTS(SELECT * FROM [rooms] WHERE Room_name = @Room_name)
       BEGIN
           --@Room_id = [dbo].[rooms](Room_id)
           IF EXISTS(SELECT * FROM [devices] WHERE Device_name = @Device_name)
           BEGIN
           RETURN 0--Device already exist

           END
           ELSE
           BEGIN
           INSERT INTO [dbo].[devices] (Device_name, Variable_of_device )
           VALUES (@Device_name, @Variable_of_device)
           RETURN 1
           END

       END
       ELSE
       BEGIN
       RETURN 0 --Room not exist
       END

  END
  ELSE
  BEGIN
  RETURN 0 --Homeserver not exist
  END