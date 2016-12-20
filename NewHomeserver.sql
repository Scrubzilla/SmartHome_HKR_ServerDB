-- Stored Procedure for checking if add a new device is available.
-- Return 1 is ok
-- Return 0 is fail

CREATE PROCEDURE NewHomeserver
  @Server_name varchar(32) = null,
  @User_id INT = null

AS
  DECLARE @Homeserver_id int

BEGIN
INSERT INTO [dbo].[homeserver] (Server_name) VALUES (@Server_name);

  SET @Homeserver_id = SCOPE_IDENTITY();

  INSERT INTO [dbo].[users_homeserver_maps] (User_id, Homeserver_id) VALUES (@User_id, @Homeserver_id)


END